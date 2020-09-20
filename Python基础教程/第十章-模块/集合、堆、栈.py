# 1、集合
# 由模块sets中的set类实现的，



# 2、堆
# 是一种优先队列。模块名称为heapq
from heapq import *
from random import shuffle
data = list(range(10))
shuffle(data)
heap = []
for n in data:
    heappush(heap,n)
print(heap)
#位置i处的元素总是大于位置i//2处的元素，这是底层堆算法的基础，称为堆特征


