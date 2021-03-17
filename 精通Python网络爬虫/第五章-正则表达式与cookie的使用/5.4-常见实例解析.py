# 实验1：匹配.com或.cn后缀的URL网址
import re
patten = '[A-Za-z]+://[^\s]*[.com|.cn]'
string = "<a href='http://www.baidu.com'>百度首页</a>"
result = re.search(patten,string)
print(result)

# 实验2：匹配电话号码
patten = '\d{4}-\d{7}|\d{3}-\d{8}' #匹配电话号码的正则表达式
string = '021-234445363246242562522343562'
result = re.search(patten,string)
print(result)