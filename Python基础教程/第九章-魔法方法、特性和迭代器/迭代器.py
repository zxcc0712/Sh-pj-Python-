# 迭代器以及可迭代的对象，方法__iter__

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
    def __iter__(self):
        return self
fibs = Fibs()
for f in fibs:
    if f > 10:
        print(f)
        break