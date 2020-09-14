# 迭代器以及可迭代的对象，方法__iter__

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a
    def __iter__(self):
        return self
fibs = Fibs()
for f in fibs:
    if f > 10000:
        print(f)
        break

# 从迭代器创建序列
class TestIterator:
    value = 0
    def __next__(self):
        self.value +=1
        if self.value >10:
            # 停止迭代
            raise StopIteration
        return self.value
    def __iter__(self):
        return self
