# 模块socket
# 网络编程中的一个基本组件是套接字（socket）
# 套接字分为两种：服务器套接字和客户端套接字。
# 套接字是模块socket中socket类的实例。实例化套接字时最多可指定三个参数：一个地址族；是流套接字还是数据报套接字；协议

import socket
s = socket.socket()

host = socket.gethostname()
port = 1234
s.bind((host,port))

s.listen(5)
while True:
    c,addr = s.accept()
    print('Got connection from',addr)
    c.send('Thank you for connecting')
    c.close()