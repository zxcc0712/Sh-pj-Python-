import fileinput
fileinput.input()               #返回一个可在for循环中进行迭代的对象
fileinput.filename()            #返回当前文件的文件名
fileinput.lineno()              #返回当前行的编号
fileinput.filelineno()          #返回当前行在当前文件中的行号
fileinput.isfirstline()         #在当前行为当前文件中的第一行时返回True，否则返回False
fileinput.isstdin()             #当前文件为sys.stdin时返回True，否则返回False
fileinput.nextfile()            #关闭当前文件并跳到下一个文件，且计数时忽略跳过的行。
fileinput.close()               #关闭整个文件链并结束迭代

#例子
for line in fileinput.input(inplace=True):
    line = line.rstrip()
    num = fileinput.lineno()
    print('{:<50}#{:2d}'.format(line,num))