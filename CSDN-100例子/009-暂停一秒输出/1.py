# 使用time模块的sleep（）函数
import time
for i in range(4):
    print(str(int(time.time()))[-2:1])
    time.sleep(1)