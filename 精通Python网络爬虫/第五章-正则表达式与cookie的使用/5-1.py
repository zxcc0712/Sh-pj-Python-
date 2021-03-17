import re
pattern = 'yue'
string = 'http://yum.iqianyue.com'
result1 = re.search(pattern,string)
print(result1)