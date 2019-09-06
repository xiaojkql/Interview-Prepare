测试预测目标向量值与文中各个单词的关联程度,然后将它们的和作为最终的预测输出

Seq2Seq的翻译的不足, 人类翻译的过程, 更加进行对齐的操作 -- 源词与目标词的相关性
Bahdanau使用了前馈神经网路来计算权重
Luong几种计算权重方式(dot,general,concat)

basic attention
multi-head attention
Hierachical attention
self attention
attention 用于阅读理解

soft/hard attention soft (权重在0-1之间) hard(权重取0或者1)
global/local attention
