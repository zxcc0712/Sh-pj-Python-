# 模块time包含用于获取当前时间、操作时间和日期、从字符串中读取的日期、将日期格式化为字符串的函数
import  time
time.asctime()              #将当前时间转化为字符串
time.localtime()            #将一个实数转换为日期元组（本地时间）
time.mktime()               #将日期元组转换为从新纪元后的秒数
time.sleep()                #让解释器等待指定的秒数
time.strptime()             #将一个字符串转换为日期元组
time.time()                 #返回当前的国际标准时间，以从新纪元开始的秒数表示
