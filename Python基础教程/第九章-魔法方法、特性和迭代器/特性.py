class Rectangle:
    def __init__(self):
        self.width = 0
        self.height = 0
    def set_size(self,size):
        self.width,self.height = size
    def get_size(self):
        return self.width,self.height
    # 函数property
    size = property(get_size,set_size)

r = Rectangle()
r.width = 3
r.height = 5
print(r.size)

# 静态方法和类方法（使用场景还没有具体找到）
class MyClass:
    # 静态方法
    @staticmethod
    def smeth():
        print('This is a static method')

    # 类方法
    @classmethod
    def cmeth(cls):
        print('This is a class method of',cls)
