# 模块sys让你能够访问与python解释器紧密相关的变量和函数
import  sys
sys.argv            #包含传递给Python解释器的参数，其中包括脚本名

sys.exit()          #退出当前程序

sys.modules         #将模块名映射到模块

sys.path            #它是一个字符串列表，其中的每个字符串都是一个目录名，执行import语句语句命令是将在这些目录中查找模块

sys.platfrom()      #运行解释器的“平台”名称
#一个例子
import sys
args = sys.argv[1:]
args.reverse()
print(''.join(args))