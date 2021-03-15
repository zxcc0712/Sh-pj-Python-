import urllib.request
import ssl

#全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

file = urllib.request.urlopen('http://www.baidu.com')
data = file.read()
dataline = file.readline()
# print(data)
# print(dataline)
fhandle = open('/Users/shihe/Downloads/Sh-pj-Python-/精通Python网络爬虫/第四章-Urllib库与URLError异常处理/1.html', 'wb')
fhandle.write(data)
fhandle.close()
# filename = urllib.request.urlretrieve('https://edu.51cto.com',
#                                       filename='/Users/shihe/Downloads/Sh-pj-Python-/精通Python网络爬虫/第四章-Urllib库与URLError异常处理/2.html')
urllib.request.urlcleanup()
file.info()
print(file.getcode())

# 对网址进行编码
a=urllib.request.quote('http://www.sina.com.cn')
print(a)
# 对网址进行解码
b=urllib.request.unquote('http%3A//www.sina.com.cn')
print(b)