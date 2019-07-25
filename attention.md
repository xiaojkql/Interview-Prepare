学习博客
[Attention? Attention! survey](https://lilianweng.github.io/lil-log/2018/06/24/attention-attention.html)
[CSDN BLOG](https://blog.csdn.net/yujianmin1990/article/details/81432851)

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
