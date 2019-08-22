参数

[XGBoost 重要关键参数及调优步骤](https://baijiahao.baidu.com/s?id=1613550753243799306&wfr=spider&for=pc)

### 1 常规参数General Parameters (booster,slient,nthread)
booster[default=gbtree]:选择基分类器，可以是：gbtree,gblinear或者dart。gbtree和draf基于树模型，而gblinear基于线性模型。
slient[default=0]：是否有运行信息输出，设置为1则没有运行信息输出。
nthread[default to maximum number of threads available if not set]：线程数，默认使用能使用的最大线程数。


### 2 模型参数Booster Parameters (eta,min_child_weight,max_depth,max_leaf_nodes,gamma,max_delta_step,subsample,colsample_bytree,lambda,alpha)
eta[default=0.3]:收缩参数，也即学习率。用于更新叶节点权重时，乘该系数，避免步长过大。参数值越大，越可能无法收敛。把eta设置的小一些，小的学习率可以使后面的学习更加仔细。
min_child_weight[default=1]:每个叶子里面的h的和至少是多少，这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数越小，越容易过拟合。权重和，引进的新方法，是在用于求分位数的时候引进的权重
max_depth[default=6]:每棵树的最大深度，该参数设置越大，越容易过拟合。
max_leaf_nodes:最大叶节点数，和max_depth类似。
gamma[default=0]:后剪枝时，用于控制是否后剪枝。
max_delta_step[default=0]:该参数可以使得更新更加平缓，如果取0表示没有约束，如果取正值则使得更新步骤更加保守，防止更新时迈的步子太大。
subsample[default=1]:样本随机样本，该参数越大，越容易过拟合，但设置过大也会造成过拟合。
colsample_bytree[default=1]:列采样，对每棵树生成时用的特征进行列采样，一般设置为0.5-1
lambda[default=1]:模型的L2正则化参数，参数越大，越不容易过拟合。
alpha[default=0]:模型的L1正则化参数，参数越大，越不容易过拟合。
scale_pos_weight[default=1]:如果取值大于0，在类别样本偏斜时，有助于快速收敛。


### 3 参数调优的一般步骤

- 1. 确定学习速率和提升参数调优的初始值
- 2. max_depth 和 min_child_weight 参数调优
- 3. gamma参数调优
- 4. subsample 和 colsample_bytree 参数优
- 5. 正则化参数alpha调优
- 6. 降低学习速率和使用更多的决策树
