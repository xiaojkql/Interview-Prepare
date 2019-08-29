---
title: 我理解的LDA QDA 贝叶斯角度
categories:
- machine learning
tags:
- machine learning
- LDA
- QDA
- dimension ruduction
date: 2019-03-23 16:23:00
---

动机：在高斯贝叶斯里面提到了，由于协方差矩阵中参数数量庞大，不易计算。为了减少计算量，将各个类别中的协方差举矩阵进行统一，即协方差矩阵都用一个矩阵，即从全局数据集中计算。

# 1 LDA为什么是线性
输入变量$\bold{X}=(x_1,x_2,...,x_n)$为连续实值变量，输出变量为$Y$为类别变量。为了达到输入一个$X_i$的实例就可以预测出它的类别，此时我们需要用到贝叶斯分类器
$$
\begin{aligned}
y=\underset{K}{\arg\max} \ \ P(Y=k|\bold{X}=\bold{X}_i)
\end{aligned}
$$
我们这里不是去估计$P(Y|X)$，而是去估计$P(X|Y)$，然后再用贝叶斯定律求前者。
$$
\begin{aligned}
y&=\underset{K}{\arg\max} \ \ P(Y=k|\bold{X}=\bold{X}_i)\\
&=\underset{K}{\arg\max} \ \ P(\bold{X}=\bold{X}_i|Y=k)P(Y=k)
\end{aligned}
$$
这里$P(\bold{X}|Y=k)$表示每一个类别中$\bold{X}$的分布。可以假设为多维高斯分布，然后用极大似然估计进行求解。  

假设$(\bold{X}|Y=k)$为一个多维高斯分布的变量，
$$
\begin{aligned}
P(\bold{X}|Y=k)=\frac{1}{(2\pi)^{1/n}||\Sigma||^{1/2}}\exp \left( -\frac{1}{2}(\bold{X}-\bold{\mu}_k)^T\Sigma^{-1}(\bold{X}-\bold{\mu}_k) \right)
\end{aligned}
$$
其中
$$
\begin{aligned}
\mu_k&=\frac{1}{\# \{ i;y_i=k \}}\sum_{i;y_i=k}\bold{X}_i\\
\Sigma&=\frac{1}{R}\sum_{i=1}^{R}(\bold{X}_i-\frac{1}{R}\sum_{i=1}^{R}\bold{X}_i)(\bold{X}_i-\frac{1}{R}\sum_{i=1}^{R}\bold{X}_i)^T
\end{aligned}
$$

$P(Y=k)$表示每一个类别的概率。可以先假设为多项分布，然后用极大似然估计进行估计
$$
\begin{aligned}
P_k&=P(Y=k)\\
&=\frac{\# \{ i;y_i=k \}}{R}
\end{aligned}
$$

求出了上面的两个分布我们就可以用贝叶斯分类器
$$
\begin{aligned}
P(Y=k|\bold{X}=\bold{X}_0)=\frac{1}{(2\pi)^{1/n}||\Sigma||^{1/2}}\exp \left( -\frac{1}{2}(\bold{X}_0-\bold{\mu}_k)^T\Sigma^{-1}(\bold{X}_0-\bold{\mu}_k) \right)P_k
\end{aligned}
$$
将与$k$无关的项记为$C$
$$
\begin{aligned}
P(Y=k|\bold{X}=Cexp \left( -\frac{1}{2}(\bold{X}_0-\bold{\mu}_k)^T\Sigma^{-1}(\bold{X}_0-\bold{\mu}_k) \right)P_k
\end{aligned}
$$
等式两边取对数
$$
\begin{aligned}
\log(P(Y=k|\bold{X})=\log(C)+\log(P_k) -\frac{1}{2}(\bold{X}_0-\bold{\mu}_k)^T\Sigma^{-1}(\bold{X}_0-\bold{\mu}_k)
\end{aligned}
$$
因为对所有类别$\log(C)$是一样的，所以可以忽略。在应用贝叶斯分类器时等于求上面的最大值
$$
\begin{aligned}
y&=\underset{K}{\arg\max} \ \ \log(P_k) -\frac{1}{2}(\bold{X}_0-\bold{\mu}_k)^T\Sigma^{-1}(\bold{X}_0-\bold{\mu}_k)\\
&=\underset{K}{\arg\max} \ \ \log(P_k) -\frac{1}{2}(\bold{X}_0^T\Sigma^{-1}\bold{X}_0+\mu_k^T\Sigma^{-1}\mu_k)+\bold{X}_0^T\Sigma^{-1}\mu_k
\end{aligned}
$$
因为对于每一个类别$k$，$\bold{X}_0$和$\Sigma$是一样的，所以将其剔除
$$
\begin{aligned}
y&=\underset{K}{\arg\max} \ \ \log(P_k) -\frac{1}{2}\mu_k^T\Sigma^{-1}\mu_k+\bold{X}_0^T\Sigma^{-1}\mu_k
\end{aligned}
$$
令$\delta_k=\log(P_k) -\frac{1}{2}\mu_k^T\Sigma^{-1}\mu_k+\bold{X}_0^T\Sigma^{-1}\mu_k$，则

$$
\begin{aligned}
y=\underset{K}{\arg\max} \ \ \delta_k
\end{aligned}
$$
那么分类边界就为$\delta_k=\delta_l$，即

$$
\begin{aligned}
\log(P_k) -\frac{1}{2}\mu_k^T\Sigma^{-1}\mu_k+\bold{X}_0^T\Sigma^{-1}\mu_k=\log(P_l) -\frac{1}{2}\mu_l^T\Sigma^{-1}\mu_l+\bold{X}_0^T\Sigma^{-1}\mu_l
\end{aligned}
$$
上面的式子定义了一个分界超平面，关于变量$\bold{X}$是线性的，所以该分类器称为线性判别器。

下图是一个输入变量为二维，输出变量有三个类别，用LDA作出的分类边界线
<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190324000356.png)
</center>

# 2 QDA
当协方差矩阵不假设为全局统一时，即各个类别中$(\bold{X}|Y)$都有一个协方差矩阵，此时求出的分类边界线就不再是线性的，而是二次的。所以是QDA。

下图是LDA，bayes classifier, QDA三者分类边界线的对比
<center>

![](https://raw.githubusercontent.com/xiaojkql/Picture/master/img/deeplearning/RNN/20190324000915.png)
</center>


reference
[1] 李航 《统计学习方法》
[2] 周志华 《机器学习》
[3] PPT from Andrew W. Moore in CMUhttp://www.cs.cmu.edu/~awm/tutorials
[4] PPT from course STATS 202 of Jonathan Taylor ]
[5] Alaa Tharwa et.al. Linear discriminant analysis: A detailed tutorial
