# 而当目标网站使用的是自签名的证书时就会抛出一个
# urllib2.URLError: < urlopen
# error[SSL: CERTIFICATE_VERIFY_FAILED]
# certificate
# verify
# failed(_ssl.c: 581) > 的错误消息，
#
# 解决方案包括下列两种方式：
#
# 1.
# 使用ssl创建未经验证的上下文，在urlopen中传入上下文参数

import ssl
import urllib.request

context = ssl._create_unverified_context()
print(urllib.request.urlopen("https://www.12306.cn/mormhweb/", context=context).read())
# 2.
# 全局取消证书验证

import ssl
import urllib.request

ssl._create_default_https_context = ssl._create_unverified_context

print(urllib.request.urlopen("https://www.12306.cn/mormhweb/").read())

# 注意：在全全局请求文件导入import
# ssl

import ssl

ssl._create_default_https_context = ssl._create_unverified_context
# 至此，问题圆满解决！

