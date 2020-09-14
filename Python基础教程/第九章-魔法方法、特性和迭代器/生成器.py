# 相对较新的Python概念，也被成为“简单生成器”，是一种使用普通函数预发定义的迭代器
# 创建生成器
nested = [[1,2],[3,4],[5]]
# 按照顺序提供这些数字
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
for num in flatten(nested):
    print(num)
# 第二种表达方式:递归式生成器
def flatten(nested):
    try:
        for sublist in nested:
            for element in sublist:
                yield element
    except TypeError:
        yield nested

def flatten1(nested):
    try:
        # 不迭代类似于字符串的对象
        try:
            nested +''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested:
            for element in flatten1(sublist):
                yield element
    except TypeError:
        yield nested
