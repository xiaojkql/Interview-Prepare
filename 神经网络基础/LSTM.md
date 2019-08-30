## 1 理解RNN,LSTM和GRU
入门深度学习系列
[零基础入门深度学习(1) - 感知器](https://www.zybuluo.com/hanbingtao/note/433855)
[零基础入门深度学习(2) - 线性单元和梯度下降](https://www.zybuluo.com/hanbingtao/note/448086)
[零基础入门深度学习(5) - 循环神经网络](https://zybuluo.com/hanbingtao/note/541458)

[Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)

[慢学NLP / 图解LSTM结构](https://zhuanlan.zhihu.com/p/57575597)
[RNN](https://mp.weixin.qq.com/s?__biz=MzIwNzc2NTk0NQ==&mid=2247484682&idx=1&sn=51520138eed826ec891ac8154ee550f9&chksm=970c2ddca07ba4ca33ee14542cff0457601bb16236f8edc1ff0e617051d1f063354dda0f8893&scene=21#wechat_redirect)
[RNN 中为什么要采用 tanh，而不是 ReLU 作为激活函数？](https://www.zhihu.com/question/61265076)
[为什么相比于RNN，LSTM在梯度消失上表现更好？](https://www.zhihu.com/question/44895610)
[Tips for Training Recurrent Neural Networks](https://danijar.com/tips-for-training-recurrent-neural-networks/)
[你在训练RNN的时候有哪些特殊的trick？](https://www.zhihu.com/question/57828011)
[如何有效的区分和理解RNN循环神经网络与递归神经网络？](https://www.zhihu.com/question/36824148)
[RNN 中学习长期依赖的三种机制: 怎样学习长期依赖的一些RNN设计](https://zhuanlan.zhihu.com/p/34490114)


## 2 梯度消失的问题
- MLP梯度消失和RNN梯度消失的不同
- LSTM缓解梯度消失的解释
- 怎样从训练的角度缓解梯度消失(MLP,RNN中的方法)
[RNN梯度消失和爆炸的原因](https://zhuanlan.zhihu.com/p/28687529)
[LSTM如何解决梯度消失问题](https://zhuanlan.zhihu.com/p/28749444)
[从反向传播推导到梯度消失and爆炸的原因及解决方案（从DNN到RNN，内附详细反向传播公式推导）](https://zhuanlan.zhihu.com/p/76772734)
[LSTM如何来避免梯度弥散和梯度爆炸？](https://www.zhihu.com/question/34878706)
[详解深度学习中的梯度消失、爆炸原因及其解决方法](https://zhuanlan.zhihu.com/p/33006526)
[Why LSTMs Stop Your Gradients From Vanishing: A View from the Backwards Pass](https://weberna.github.io/blog/2017/11/15/LSTM-Vanishing-Gradients.html#fn:3)


## 3 训练时的tricks
- gate权重初始化 (orthogonal初始化)
- 梯度剪切
- dropout
