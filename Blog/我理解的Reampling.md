---
title: 我理解的cross validation
categories:
- machine learning
tags:
- machine learning
- cross validation
- error
- bias variance
date: 2019-03-23 00:34:01
---

# 1 resampling概念
从训练数据集中不断的采样形成新的样本。它目的是从现有的数据构造性的数据集，新的随机噪声pattern。
常用的有Cross-Validation和bootstrap。前者可以用来评估模型(model assessment)和选择模型(model selection)。后者往往可以对一些模型中的参数进行很好的估计。

做模型选择时我们会将分为三部分，training set, validation set, test set。分别用来训练模型，选择模型的参数，测试模型的误差。

# 2 Validation set approach
再训练模型时，我们用训练集误差来作为我们评估模型的好坏的指标。在最后评估模型的预测能力时用测试集误差来评估模型的表现。但是现实中常常面临一个问题，那来测试集数据。整个测试集误差是整个样本空间的误差。解决的办法就是从原始的训练数据集中预留一部分，不让模型看到，将这一预留的部分作为我们评估模型表现的测试集，这样便可以对测试集误差一个很好的估计了。这种方法就称为验证集。
<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190321180055.png)
</center>

但是这个方法会带来两个问题
- 训练集数据量减少，就会增大偏差，导致对真实的测试误差过高的估计。
- 由于在每次划分数据集都是随机的，所以每次计算都是不一样，这样测试的方差就会增大，即每一次的判断模型好坏时都是随机的。这个模型好不好全凭你的运气，划分数据集好不好。造成这样的原因训练的数据集少了，学习不完系统的pattern,而随机的pattern占比增加，每一划分时随机的pattern就不一样，所以学习到的模型不一致。
- 由于每一次的结果都不一样，所以选择调参时，模型的好坏全凭你的运气。
<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190321180340.png)
</center>

# 3 leave-one-out Cross validation
这种方法就是只留一个作为评估模型的数据，其他的都作为训练的数据，进行训练模型。
$$ CV_{n}=\frac{1}{n}\sum_{i=1}^{n}MSE_i $$

<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190321180435.png)
</center>
优点：
- 包含了更多的训练数据，能更好的拟合系统的pattern，噪声引起的Pattern作用很小(忽略)，所以是对test error的更好的估计。(unbiased estimate)
- 由于划分数据集的唯一性，没有随机因素，所以得到结果总是唯一的，而不是变化的。
- 划分的唯一性，所以选择的模型的参数也是唯一的。没有凭借运气这一点。

缺点：
- 求解时间过长，特别是当n很大的时候。
替代方案：用short cut formula。

# 4 k-fold Cross-Validation
$$ CV_{k}=\frac{1}{k}\sum_{i=1}^{k}MSE_i $$

<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190321180650.png)
</center>
实际中通常使用k=10或者5。
优点
- 大大的缩短了计算时间。
- 相比validation set而言，数据量的用的多了，降低了偏差，同时也降低验证集误差的变化。
- 涉及了bias-variance trade-off

<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190321180626.png)
</center>
由于我们在实际使用CV方法时，通常有两个目的，多个模型中那个模型做好，第二个就是调超参数。所以我们并不需要真实的test error,但是我们要知道test error最小时出现的地方在那，此时各个参数是啥。即test error曲线的形状，由上图可知，CV的error曲线和真实的error曲线基本一致，所以我们可以用CV来估计test error的最低点。

<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190321180711.png)
</center>

k-Fold CV的bias-variance trade-off分析
由于k-Fold CV的训练数据集比Validation set方法中多，所以能看到更多的系统pattern，所以降低了拟合的bias。loocv降低偏差的效果最好，K-fold次子，validation set 最差。这是由于训练数据量的影响。

但是LOOCV的方差相比k-fold方法来说就要大一些，因为LOOCV训练的模型的相关性很高，而k-fold训练出的模型相关性很低。相关性很高的模型，方差就会大，相关性低的模型的方差就会小一些。

**部分分析有误**
LOOCV比k-Fold有更大的方差。因为在做LOOCV时，我们使用的数据集合基本一致，即存在相关性，那么这些数据集中由噪声产生的pattern就基本一致。在学习时候，首先，系统的pattern是一致的，噪声error一致，所以LOOCV最后学习到的模型也基本一致，所以实际上，我们在学习一个模型。但是这时候由于噪声pattern的单一性，而这个pattern又具有随机性，所以在其他的数据集上就不一样，这时将模型应用在其他数据集上时，就会产生很大的误差。所以方差增大。

相反k-fold CV，由于在每一次训练时候数据集都存在差异，里面的随机噪声产生的pattern就会不一致。在每次学习时，首先学习了系统的pattern，但是随机噪声pattern的不一致导致了模型之间的差异。所以就学到多个模型，由于随机噪声是均值为0产生的，所以将这些模型进行均匀化时就中和了随机pattern，受到的随机就减少，接近系统pattern。用在测试数据集上时，误差变化就小一些。降低了方差。
**部分分析有误**

所以k越大方差越大，偏差越小，在做一个bias-variance trade-off。需要选择合适的k，实际中通常选择5或者10，此时即不受到大的偏差影响，也不受到大的方差影响。

# 4 bootstrap
自助采样方法，不断从原始的训练数据集中采集样本，由于训练数据集的不一样，所以里面的随机噪声产生的pattern就不一样，所以在拟合的时候模型对随机pattern的拟合就不一样，在综合时就会将拟合出来的随机pattern进行综合，降低了模型的不确定度，即降低了方差。
<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190321180754.png)
</center>

# 5 总结
- Validation set 偏差大(数据少)，验证的误差具有很大的波动。
- LOOCV 偏差最小，但是方差大(相关性)。
- K-fold 偏差次之，方差也会减小，模型的相关性低。
- 与真实误差形状基本保持一致，选择最小的就好。
- 用5-fold来选单个模型的参数，或者多个模型中的一个。然后用选出来的模型在整个training上训练，给出最后的测试误差。

reference
[1] Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani, An Introduction to Statistical Learning
