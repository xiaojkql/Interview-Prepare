## 1 deque
from collections import deque
d = deque(iterable=None,maxlen=None)
d.append(value)  d.appendleft(value)
d.copy() == copy.copy(d) --> 浅; copy.deepcopy(d)
d.count(value)
d.extend(seq) d.extendleft(seq)
d.insert(index,value)
d.pop() d.popleft() 有返回
d.index(value) d.remove(value) 第一个匹配项
elem in d; len(d)
