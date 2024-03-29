两阶段模式:预训练阶段+finetuning阶段
非监督表示学习
- 以自回归语言模型为优化目标或者以自编码语言模型为优化目标


## 2 张俊林系列博客
### 2.1 从Word Embedding到Bert模型—自然语言处理中的预训练技术发展史
自然语言的训练过程
feature-based fine-tuning
pre-trained fine-tuning
#### 图像领域的预训练
Frozen或者finetuning
预训练优点：a.弥补训练数据的不足;b.加快模型的收敛;c.更好的初始点
为什么可行？ 底层特征都是一些可复用的特征(线段,图形框),高层特征才是与任务相关的特征.
#### word embedding
- 最基础: 语言模型 预训练的目标  (语言模型: 一句话出现的概率,具体求时将求整句话的概率转换成了基于前面的词汇预测后面词汇的概率)
- 原始: NNLM (最古老的神经网络语言模型) 功能:a.根据上文预测下文(主要,解决语言模型的一个网络结构,一定要上文预测下文,对于预测的时候就是这样来做的,不能随心所欲的改变训练流程);b.产生一个副产品词向量.
- 闪亮登场: word2vec CBOW(窗口小,有上下文)和skip-gram两种训练方式;功能:获取词向量-最主要的功能,而基础是语言模型,在类似语言模型的基础上改变训练的方式.加快了获取词向量的速度
- 登场: 使用word2vec, 可以将word2vec看成one-hot层到embedding层网络参数的初始化. 两种方式: a.frozen;b.fine-tuning.
- 缺点: 不能解决词的多义,静态的,所以NLP下游任务的效果并不是被提的很高

#### ELMO
原来的word embedding是学到了就把它取出来,看成是每个单词的一个固定的词向量代表
ELMO不再将底层的One-hot到embedding层的权重矩阵取出来赋予给每个单词,而是在其上加上一层网络学习它的上下文信息
ELMO: 底层表示一个词的主要语义信息(一个词的主要意思), 上层混入了上下文信息(所以可以混入该词所处的环境,句法信息,语法信息,根据上下文而来的词义信息)
三层网络: 单词特征+句法特征+语义特征
使用:用加权的方式将三层的向量进行加权求和
缺点:使用的双向LSTM,训练速度慢,特征抽取能力弱于Transformer(拼接方式的硬核式双向弱于transfomer)

word embedding 和 ELMO都需要外加一些任务相关的网络结构,而不是像图像领域的预训练模式

#### GPT
现代NLP预训练的开山鼻祖
新的NLP预训练模式,一个大网络,改造下游任务的输入形式形成GPT的输入形式
缺点：是单向的

#### Bert
(4大任务:序列标注,序列分类,序列关系,序列生成) bert原始论文没有做序列生成类任务
集大成者
- 使用了GPT的预训练模式
- 主要创新点:使用了双向,即引进了新的任务,即将双向引入到了训练过程中,使用了上下文信息
- 双向语言模型起到绝对核心的作用
- 预测下一个句子起到了一定的影响力作用

#### word embedding和ELMO和GPT和Bert的关系
Bert,ELMO是双向的
BERT和GPT都使用了Transfomer作为特征提取器(更深,更好)
BERT借鉴了Word embedding中的CBOW的语言模型上下文信息

#### 总结
ELMO,GPT,BERT开创了将语言学先验知识引入任务的方法



### 3 效果惊人的GPT 2.0模型：它告诉了我们什么
改进点
- 更大的模型,Transformer结构的参数增多
- 更多的网页数据,覆盖范围广,通用性强,并做了一定数据筛选工作保证了数据质量.
- 改变了第二个过程,即从有监督的fine-tuning转换成了无监督的fine-tuning


### 4 Bert时代的创新：Bert应用模式比较及其它
BERT的应用前兆
各种使用/应用BERT解决各种任务的探讨
- Bert应用框架
- Bert应用模式
#### 4.1 特征集成(feature ensemble),微调(fine-tuning) 到底使用哪一种呢？
两种解决NLP下游任务的使用方案
[To Tune or Not to Tune? Adapting Pre-trained Representations to Diverse Tasks]()
[Understanding the Behaviors of BERT in Ranking]()
ELMO: 使用特征集成的方式来解决下游任务效果更加好
BERT: 使用微调(fine-tuning)的方式来解决下游任务效果更好

#### 4.2 是仅仅使用最高层的输出作为整个的输出？还是使用多个层的结合作为最后输出呢？
句子匹配问题:a.使用[cls]来作为输出(效果最好);b.将最高层的输出进行集成;c.将各个层进行集成然后作为最终的输出.
序列标注:a.使用最高层;b.使用多层(权重相同);c.使用attention来学习各个层的权重(效果更好,序列标注问题倾向于将各个层的特征进行融合后进行输出)

#### 4.3 BERT带来的东西,指明的NLP发展方向
就是通过预训练的模式，充分使用大量的无标注语言数据，利用自监督模型，发挥Transformer特征吸收能力强的特点，来对语言知识进行特征编码。用这些知识来促进很多下游NLP任务的效果，以弥补有监督任务往往训练数据规模不够大，无法充分编码语言知识的困境。

### 5 Bert时代的创新（应用篇）：Bert在NLP各领域的应用进展
Bert是否可以广阔的取解决NLP各个领域的任务(生成任务除外)？怎样使用Bert来解决NLP任务?
