blog
[张俊林0]()
[张俊林1](https://zhuanlan.zhihu.com/p/65470719)
[张俊林2](https://zhuanlan.zhihu.com/p/68446772)
[Bert As Service](https://github.com/hanxiao/bert-as-service)
[awesome-bert-nlp](https://github.com/cedrickchee/awesome-bert-nlp)

### 预训练
- word2vec,glove,ELMO都输feature-based即预训练作为额外的输入特征向量，还需要特定的任务相关的神经网络结构来解决相应的问题
- GPT,BERT是fine-tuning模式，即仅仅需要一个简单任务相关的变化，而不需要任务相关的设计，简化了过程


### 1 model architecture
Transformer结构的理解

### 2 input representation
两种输入形式：一是单个句子的输入形式，二是句子对的形式
中文输入是单个字,英文输入是每个英文单词
词的嵌入由三部分组成：
- 本身的一个向量
- 位置嵌入
- 句子种类的嵌入(第一个句子的嵌入表示，第二个句子的嵌入表示)
特殊点：
- 首位置增加一个[cls]用于分类
- 两个句子之间用了一个[sep]嵌入
- 总的句子长度为512长

### 3 两个训练任务
标记语言模型（deep bidirectional）
mask的缺陷：训练与真实使用情况的差异
mask策略：
总体15%拿来作标记
从此15%中抽取80%来进行真正的[mask]代替
从此15%中10%用随机的词汇进行替代，增加多样性，但同时又不会破坏语言特性(仅1.5%)
从此15%中10%保持不变
另外每次仅有15%用来预测，相对于从左到右，从右到左的语言模型，收敛较慢。

第二个训练任务是下一个句子的预测
用来捕捉句子之间的关系

### 4 预训练流程
句子是document-level形式上的sentence(即多个句子组成一个句子)，这样可以学习长序列依赖关系
目标函数：标记语言模型的似然函数，预测问题的似然函数
使用的是cross-domain语料库

### 5 与GPT的比较
- 更大的语料库(多了wiki)
- 两个新的训练任务(Bert的主要创新点)
- [sep] [cls]的使用时期不一样，Bert在训练时期就使用，GPT是在微调时使用
- GPT微调用一样的学习率，Bert用任务导向性的学习率
- Bert使用的结构是transformer的Encoder部分，GPT使用的transformer的Decoder部分
- 对于下游任务，Bert更加简单，一个仅仅需要作出与任务相关的一个层，而GPT需要改变的多一些


### 6 分类任务的预训练
可以使用的数据集(清华news)
三种策略：
- 直接微调
- 先继续在与任务相关的数据集(in domain)或者(任务的数据集上)进行预训练，然后任务导向的微调
- multi-task学习

#### 6.1 具体的方法
长文本的处理：
文本的关键信息，主要信息主要是在head,tail
- 使用head
- 使用tail
- 使用head+tail

层次相关的学习率
层次低表示的是一些通俗的语言信息，而层次高的表示更多的是与任务有关的信息

学习率不能过高，过高会导致大量遗忘预训练模型，特别是低的层，低层用低的学习率

in-domain 和 task pretraining效果好于直接微调

预训练模型能在数据集很小的时候带来精度的大幅度提高。


### 7其他相关结构
[1](https://zhuanlan.zhihu.com/p/76724992)
