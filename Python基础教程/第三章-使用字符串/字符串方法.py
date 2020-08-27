# center :通过在两边添加填充字符（默认为空格）让字符居中
print('The Middle by Jimmy Eat World'.center(39,'*'))

# find：在字符串中查找子串，找到就返回子串的第一个字符的索引，否则返回-1
print('The Middle by Jimmy Eat World'.find('by'))

# join:是一个非常重要的字符串方法，其作用与split相反，用于合并序列的元素[合并序列必须是字符串]
dir = '','usr','bin','env'
print('/'.join(dir))
print('C:'+'\\'.join(dir))

# lower:返回字符串中的小写版本
# replace：将指定子串都替换为另一个子串，并返回替换后结果
print('This is a test'.replace('is','eea'))

# split:是一个非常重要的字符串方法，用于字符串拆分成序列
print('1=2=3=4=5'.split('='))
# strip：将字符串开头和末尾的空白（不包括中间的空白）删除，并返回删除后的结果
print('     internal whitspace is krpt        '.strip())
# translate:同样是替换字符串的特定部分，但不同的是它只能进行单字符的替换，首先必须先创建一个转换表（maketrans）
table = str.maketrans('cs','kz')
print(table)
print('this is an incredible test'.translate(table))
