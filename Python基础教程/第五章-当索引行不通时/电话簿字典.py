# 一个简单的数据库
# 一个将人名用做键的字典，每个人都用一个字典表示
# 字典包含键‘phone’和‘addr’，他们分别与电话号码和地址相关联
people = {
    'Alice':{
        'phone':'2345',
        'addr':'qwe'
    },
    'Beth': {
        'phone': '1122',
        'addr': 'asd'
    },
    'Cecil':{
        'phone':'9988',
        'addr':'zcc'
    },
}
# 电话号码和地址的描述标签，供打印输出时使用
labels = {
    'phone':'phone number',
    'addr':'address'
}
name = input('Name: ')
request = input('Phone number(p) or address(r)')
if request == 'p':
    key = 'phone'
if request == 'r':
    key = 'addr'
if name in people:
    print("{}'s {} is {}.".format(name,labels[key],people[name][key]))
