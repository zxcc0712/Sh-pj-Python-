import urllib.request
import urllib
import re
import ssl

# 2. 表示忽略未经核实的SSL证书认证
context = ssl._create_unverified_context()

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/54.0.2840.99 Safari/537.36"}

url = "https://read.douban.com/provider/all"

request = urllib.request.Request(url, headers = headers)

data=urllib.request.urlopen(request,context=context).read()
data=data.decode("utf-8")
pat='="name">(.*?)<'
mydata=re.compile(pat).findall(data)
print(mydata)
file=open("fh.txt","w")
for i in range (len(mydata)):
    file.write(mydata[i]+"\n")
file.close()

