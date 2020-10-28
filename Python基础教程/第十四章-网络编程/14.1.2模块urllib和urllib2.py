
from urllib.request import urlopen
import re
webpage = urlopen('http://www.python.org')

text = webpage.read()
m = re.search(b'<a href="([^"]+)" .*?>about</a>',text.re.IGNORECASE)

urlretrieve('http://www.python.org','D://python_webpage.html')