import urllib.request

# keywd = 'hello'
keywd = input('搜索关键字：')
url = 'http://www.baidu.com/s?wd='+keywd
req = urllib.request.Request(url)
data = urllib.request.urlopen(req).read()
fhandle = open('4.html','wb')
fhandle.write(data)
fhandle.close()