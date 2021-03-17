import re
string = 'apythonhellomypythonhispythonourpythonend'
pattern = '.python.'
# 字符串的开头进行匹配
result = re.match(pattern,string)
# 字符串的全文进行匹配
result2 = re.search(pattern,string)
print(result)
print(result2)
# 全局匹配函数
pattern1 = re.compile(pattern)
result3 = pattern1.findall(string)
print(result3)
# 替换函数
result4 = re.sub(pattern,'php',string)
print(result4)