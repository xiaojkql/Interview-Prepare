学习资料
[苏剑林1](https://kexue.fm/archives/4819)
[胶囊网络Capsule Networks学习资源汇总](https://zhuanlan.zhihu.com/p/34336279)
[慢学NLP / Capsule Net 胶囊网络](https://zhuanlan.zhihu.com/p/56296828)
[Hinton大神的Capsule网络是什么](https://zhuanlan.zhihu.com/p/31728352)
[如何看待Hinton的论文《Dynamic Routing Between Capsules》？](https://www.zhihu.com/question/67287444/answer/251460831)

capsule 是一种新的 vector in vector out的传递方案

一种新的、基于聚类思想来代替池化完成特征的整合的方案，这种新方案的特征表达能力更加强大

每一个胶囊表示一个属性，而胶囊的向量则表示这个属性的“标架”。也就是说，我们以前只是用一个标量表示有没有这个特征（比如有没有羽毛），现在我们用一个向量来表示，不仅仅表示有没有，还表示“有什么样的”（比如有什么颜色、什么纹理的羽毛），如果这样理解，就是说在对单个特征的表达上更丰富了。可以类别NLP中的词向量，以前的词向量时one-hot仅仅表示有没有；后来的分布式表示的词向量可以表示某个特征的多个方面。

Capsule的核心思想就是输出是输入的某种聚类结果。当作为文本分类的顶层的时候作用就是将多个顶层的输出进行聚类找到当前的文本内容的聚合中心然后在进行分类

squashing: 胶囊的模长能够代表这个特征的概率，也即特征的显著程度

动态路由求权重,此权重不是后向传播学习出来的,而是经过轮轮迭代出来的。为了得到各个vj，一开始先让它们全都等于ui的均值，然后反复迭代就好。说白了，输出是输入的聚类结果，而聚类通常都需要迭代算法，这个迭代算法就称为“动态路由”。


### 与max-pooling相比的作用
max-pooling具有invariance的特性(不变性)
capsule具有Equipvariance的特性(同变性)
对于某些变化很小的地方能否捕捉出来
