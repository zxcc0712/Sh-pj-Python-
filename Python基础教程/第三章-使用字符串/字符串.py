#字符串的基本操作
#设置字符串的格式：精简版
format = 'Hello ,%s. %s enough for ya '
values = ('world','Hot')
print(format % values)
#第二种方式设置字符串
from string import Template
tmpl = Template('Hello ,$who! $what enough for ya')
print(tmpl.substitute(who='Mary',what = 'Dusty'))
#完整版字符串格式
# 1、替换字段名，向format提供要设置其格式的未命名的参数
'{foo}{}{bar}{}'.format(1,2,bar=6,foo=0)
# 二进制转换.基本转换
print('The number is {num:b}'.format(num=42))
# 设置宽度、精度和千位分隔符
print('One googol is {:,}'.format(10**100))
# 字符串左对齐、右对齐、居中分别是<、>和^
# 最后一个要素是井号（#）
# 根据指定的宽度打印格式良好的价格列表
width = int(input('Please enter width:'))

price_width = 10
item_width = width-price_width
#要在最终结果中包含花括号，可在格式字符串中使用两个花括号来指定
header_fmt = '{{:{}}}{{:>{}}}'.format(item_width,price_width)
print(header_fmt)
fmt        = '{{:{}}}{{:>{}.2f}}'.format(item_width,price_width)
print(fmt)
print('='*width)

print(header_fmt.format('Item','Price'))

print('-'*width)

print(fmt.format('Apple',0.4))
print(fmt.format('Pears',0.5))
print(fmt.format('Cantaloupes',1.92))
print(fmt.format('Dried Apricots(16 oz.)',8))
print(fmt.format('Prunes(4 lbs.)',12))

print('='*width)