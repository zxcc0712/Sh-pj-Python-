import urllib.request
import ssl

#全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://blog.csdn.net/weiwei_pig/article/details/51178226'
file = urllib.request.urlopen(url)
headers = ('User-Agent',' Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()
fhandle = open('/Users/shihe/Downloads/Sh-pj-Python-/精通Python网络爬虫/第四章-Urllib库与URLError异常处理/3.html','wb')
fhandle.write(data)
fhandle.close()