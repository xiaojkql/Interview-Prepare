学习博客
[Attention? Attention! survey](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)
[CSDN BLOG](https://blog.csdn.net/yujianmin1990/article/details/81432851)
[深度学习中的注意力模型（2017版）](https://zhuanlan.zhihu.com/p/37601161)
[浅谈Attention注意力机制及其实现](https://zhuanlan.zhihu.com/p/67909876)
[深度学习attention机制中的Q,K,V分别是从哪来的？](https://www.zhihu.com/question/325839123)
[综述：注意力机制在自然语言处理中的应用](https://zhuanlan.zhihu.com/p/54057012)
[Attention Model(注意力模型)](https://zhuanlan.zhihu.com/p/61816483)
[完全解析RNN, Seq2Seq, Attention注意力机制](https://zhuanlan.zhihu.com/p/51383402)
[请问注意力机制中生成的类似热力图或者柱状图是如何生成的？](https://www.zhihu.com/question/274926848/answer/473562723)
[浅谈Attention机制的理解](https://zhuanlan.zhihu.com/p/35571412)
[自然语言处理中注意力机制综述](https://zhuanlan.zhihu.com/p/54491016)

2014:
传统Encoder-Decoder模型结构的缺点：
- 长距离依赖关系学习能力弱，记忆力弱
- 没有明显的单词对齐方式，没有聚焦，
语境向量
对齐函数(刻画输出单词与输入词之间的相似程度)
soft alignment(软对齐方式)
注意力分数，权重：表示相似程度，匹配程度

## basic
一些向量的权重
作用：从一个序列中抽取重要的部分
基础的attention没法满足复杂了任务，所以设计出了很多变体attention，以便适应各个问题
- 基础attention: 从一个序列当中提取重要的部分，给每个term一个权重分数，然后进行合成
- 多维度的attention
- 等级attention
- 自我(内部)attention：句子的内部依赖关系，自适应模式下学习语境化的词向量
- 基于记忆力的attention
- 任务导向的attention
