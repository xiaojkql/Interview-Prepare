[LightGBM——提升机器算法（图解+理论+安装方法+python代码）](https://blog.csdn.net/huacha__/article/details/81057150)
[Lightgbm 直方图优化算法深入理解](https://blog.csdn.net/anshuai_aw1/article/details/83040541)
[LightGBM核心解析与调参](https://juejin.im/post/5b76437ae51d45666b5d9b05)
## 1 直方图求最佳分裂点
(for leaf (for features (for data, for bins)))
- 减少内存
- 减少计算信息增益的计算量
## 2 leaf-wise
- level-wise for xgboost
- 选择信息增益最大的，但是容易导致过拟合，所以用了max_depth变量来作为树的限制

## 3 直方图加速
- 直到父节点和一个兄弟节点，变可以直到其节点的直方图


## 4 并行方式
- 数据并行，每个worker计算直方图
- 特征并行，每个worker计算最佳分割点，最后进行合并找到全局的最佳分割点

## 5 调参
[LightGBM 调参方法（具体操作）](https://www.imooc.com/article/43784?block_id=tuijian_wz)

#### 正则化项
- lambda叶子的二次方正则
- min_gain_in_leaf 分裂节点的最小阀值

### 加快速度
- bagging，bagging_freq 每次迭代时使用的数据量
- feature_fraction
- max_bin 最少的仓库量

### 更好的精度
- 大的max_bin
- 小的learning_rate
- 大的iteration
- 使用大的num_leaves叶子数

### 防止过拟合
- 小max_bin
- Use small num_leaves
- Use min_data_in_leaf and min_sum_hessian_in_leaf
Use bagging by set bagging_fraction and bagging_freq
Use feature sub-sampling by set feature_fraction
- Use bigger training data
- Try lambda_l1, lambda_l2 and min_gain_to_split for regularization
- Try max_depth to avoid growing deep tree
