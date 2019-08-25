Transformer [Pytorch](https://github.com/huggingface/pytorch-transformers)
Blog:
[illustrated-transformer](https://jalammar.github.io/illustrated-transformer/)
[有了Transformer框架后是不是RNN完全可以废弃了？](https://www.zhihu.com/question/302392659/answer/551542493)
[较好的一个博客](https://juejin.im/post/5b9f1af0e51d450e425eb32d#heading-13)
[和RNN,CNN的对比](https://zhuanlan.zhihu.com/p/54743941)
[细枝末节](https://zhuanlan.zhihu.com/p/58969651)


## 1 Transformer
- solving sequence to sequence problem using attention mechanism
- 没有循环连接，仅仅用了全局的attention，可以学习长距离依赖关系
- 在输入与输出都添加了embedding作为输入，且增添了一个位置embedding来捕捉位置信息
- Encoder-Decoder architecture
- a new neural network
- 可以通用化的用到其他任务上
- 捕捉全局依赖
- 特征提取器替代RNN

### 1.2 attention mechanism
可以得到长距离依赖关系
attention function：additive attention; dot product attention(更加快速和省内存)
scaled dot-product attention
scaled 的作用，当维数很大时，内积就会变得很大，使得softmax后各个成分的概率值差异很少，减弱了attention的作用，所以进行了缩放
multi-head attention
作用：可以将输入的不同维度进行不同加权方式组合，而single所有维度的加权组合方式一致，增加了多样性
三种不同的使用方式

### 1.3 嵌入层
将嵌入词向量进行了缩放

### Beam search
[知乎 seq2seq 中的 beam search 算法过程是怎样的？](https://www.zhihu.com/question/54356960)


### 1.4 training
#### Regularization
1 layer output dropout
2 embedding dropout
3 label smoothing
#### learning rate
warmup_steps + decaying rate
#### optimizer
Adam


自注意力机制(内部注意力机制)：对序列的不同位置建立关系，从而获得序列的一个表示
端到端记忆网络

Encoder:map a sequence of symbol representation to a sequence of continuout representation
Decoder:autoregressive

layers:self-attention + fully point-wise feedforward 



## https://wenku.baidu.com/view/97d228975ff7ba0d4a7302768e9951e79b8969eb.html

### 与RNN、CNN的对比
NLP特征提取器：RNN,CNN,Transformer
**一个特征抽取器是否适配问题领域的特点，有时候决定了它的成败，而很多模型改进的方向，其实就是改造得使得它更匹配领域问题的特性**
NLP数据的特点：a.顺序很重要；b.长距离依赖关系很重要

RNN衰落：
- 后面的模型更加优秀
- RNN并行能力差(提取依赖关系的代价)


### tricks
- Weight Tying, 即目标语言与源语言共用一个embedding
- point-wise feed forward: 增加维度大小能提高Bleu, 且是大多数的非线性变换的来源
- positional embedding
- Scaled Dot-Product Attention
- Layer Normalization:先使用均值 [公式] 和方差 [公式]对 [公式] 进行分布调整。如果将其理解成正态分布，就是把“高瘦”和“矮胖”的都调整回正常体型（深粉色），把偏离x=0的拉回中间来（淡紫色）
- warmup learning
