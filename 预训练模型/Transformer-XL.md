[github](https://github.com/kimiyoung/transformer-xl)

[xlnet 论文和代码实现的差别](https://zhuanlan.zhihu.com/p/71735221)

原始Transformer
固定的长度,造成了长距离依赖不好,特别是每一段文本的首尾的依赖非常不足

解决了两个问题
- 长距离依赖
- 文本碎片化,即给一段文字提供了上下文

解决方针
- 递归式的Transformer 依赖长度变为N*L (N为结构的层度,L为文本段的长度)
- 创新发明了一种新的相对位置信息
