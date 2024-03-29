
分类问题可以看成症状--病因问题
输入变量是症状，因为它是我们的观察值，我们可以观察到，所以是症状，但是这个症状是由什么引起的呢？这就要找病因了，这个症状最有可能是什么引起的。这就要进行推断了。

极大似然的观点就是我这个症状既然发生了，那么我就要求它出现的机会最大，即在什么病因里面它的概率最大。

最大后验概率，这个症状最大可能来源于那个病因。需要应用先验知识

最大后验概率估计(MAP)
$$ P(Y|X) $$
后验概率：该症状发生的情况下，每个原因发生的概率。
先验概率：普通情况下，每个原因发生的概率。
为什么要用最大后验概率估计呢？
因为我们通常是能观察到X的，即能观察到症状，此时我们要找发生的原因，即找最大后验概率的原因。而最大后验概率是条件概率，即一个边缘分布除以另外一个边缘分布。需要转很多个弯才能求出，为什么要这么多的转换呢？因为输入，输出之间通常不是独立的，所以不能直接求。

分类器用的是最大后验概率。

极大似然估计
$$ P(X|Y) $$


联合概率分布
# 1 有什么作用
知道联合概率分布，我们可以求其中任意随机变量的边缘分布，可以求任意组合变量的边缘分布。那么求这些又有什么用？可以用于概率推断。即求条件概率，一件事发生了，那么最能引起它发生的概率是啥。  
在机器学习中体现为，(X,Y)知道了他们的联合概率分布，接下来我们给出新的值X要求Y的值，怎样做？概率推断，最大后验概率，即症状X发生的情况下，最大可能的原因是啥？明显的条件概率！所以可以先求出输入与输出之间的联合概率分布，然后再应用该联合概率分布求边缘分布，求条件概率。

# 2 求联合概率分布的方法

对于离散变量，是直接求分布律。此时又有两种方法，一是极大似然方法，一是最大后验概率。

## 2.1 极大似然估计

第一种方法，直接求，即求每一种联合的值的概率。

第二种方法，
假设各个因素发生的
