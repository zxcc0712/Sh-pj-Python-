#填充字典
responses = {}
#设定一个标志
polling_active = True

while polling_active:
    name = input('你的名字是?： ')
    response = input('你喜欢爬的山是什么？： ')

    #将答案填充进字典
    responses[name] = response
    #询问是否还有人继续加入问卷
    repeat = input('你是否愿意加入问卷调查(yse/no)?: ')
    if repeat == 'no':
        polling_active = False
#显示调查结果
print('-------显示调查结果-------')
for name,response in responses.items():
    print(name+'喜欢去爬'+response+'.')