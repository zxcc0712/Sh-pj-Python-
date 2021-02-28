import requests
from lxml import etree
from fake_useragent import UserAgent
class qidian(object):
    def __init__(self):
        self.url = 'https://book.qidian.com/info/1020580616#Catalog'
        ua = UserAgent(verify_ssl=False)
        # 随机产生user-agent,随机产生一百种不同的请求头
        for i in range(1, 100):
            self.headers = {
                'User-Agent': ua.random
            }
    def get_html(self,url):
        '''发送请求，获取网页'''
        response=requests.get(url,headers=self.headers)
        html=response.content.decode('utf-8')
        return html
    def parse_html(self,html):
        # 初始化一个对象
        target=etree.HTML(html)
        # 获取链接
        links=target.xpath('//ul[@class="cf"]/li/a/@href')
        for link in links:
            host='https:'+link
            #解析链接地址
            res=requests.get(host,headers=self.headers)
            c=res.content.decode('utf-8')
            target=etree.HTML(c)
            # 获取每一章的名字
            names=target.xpath('//span[@class="content-wrap"]/text()')
            results=target.xpath('//div[@class="read-content j_readContent"]/p/text()')

            with open('大周仙吏.txt', 'a') as f:
                for name in names:
                    #print(result)
                    f.write(name+'\n')
                    for result in results:
                        f.write(result)
    def main(self):
        url=self.url
        html=self.get_html(url)
        self.parse_html(html)
if __name__ == '__main__':
    spider=qidian()
    spider.main()

