#字符串的基本操作
#设置字符串的格式：精简版
format = 'Hello ,%s. %s enough for ya '
values = ('world','Hot')
print(format % values)
#第二种方式设置字符串
from string import Template
tmpl = Template('Hello ,$who! $what enough for ya')
print(tmpl.substitute(who='Mary',what = 'Dusty'))
