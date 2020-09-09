# 初始化
def init(data):
    data['first']={}
    data['middle'] = {}
    data['last'] = {}

# 获取人员姓名
def lookup(data,label,name):
    return data[label].get(name)

# 储存人员姓名
def store(data,full_name):
    # 将人员名字进行分割
    names = full_name.split()

    if len(names)==2:
        # 第二个位置插入空白项
        names.insert(1,'')
    labels = 'first','middle','last'
    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=full_name