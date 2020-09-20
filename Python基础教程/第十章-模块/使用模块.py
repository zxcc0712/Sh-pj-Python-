# import  sys ,pprint
#
# pprint.pprint(sys.path)
#
import  copy

print([n for n in dir(copy) if not n.startswith('_')])
print(copy.__all__)
# 使用help获取帮助
help(copy.copy)
# 获取文档
print(range.__doc__)
# 获取源代码
print(copy.__file__)