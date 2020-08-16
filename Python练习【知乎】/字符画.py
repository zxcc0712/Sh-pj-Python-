from  PIL import Image

# 其实原理非常简单，首先，要准备一个字符集
char_set = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. '''
# 其次，要将图片转成灰度图，所谓灰度图就是黑白照片，
# 这个过程中还要缩小图片，每张图片缩小的比例都不尽相同，
# 要根据图片的实际情况来决定，这样就得到了一张缩小后的黑白照片
im = Image.open('qq.png')
im = im.resize((80, 50), Image.ANTIALIAS)
im = im.convert('L')    # 转为黑白图, 每个像素都一个灰度值,从0到255, 0是黑色, 255是白色
im.save('t.jpeg')   # 保存图片只是为了演示黑白照片

# 看起来有一些丑陋，这张黑白照片一共有80*50个像素，
# 每个像素点都可以通过im.getpixel方法获得灰度值，
# 这个值的范围是从0到255，0是黑色，255是白素，
# 中间就是从黑到白的灰色。
#
# 接下来要做的事情就是把4000个灰度值转成字符
def get_char(gray):
    if gray >= 240:
        return ' '
    else:
        return char_set[int(gray/((256.0 + 1)/len(char_set)))]
# 灰度值大于240的，我都转成空字符串，这样看着舒服，其余的，按比例映射到字符集上。
#
# 强调一点，生成的txt文件不要打开查看，那样你看不到一个完整的字符画，
# 在浏览器里打开字符画，这样才可以看到完整的，如果你把缩小的比例再放大一点，
# 生成的字符画就会失去很多细节，一般来说，宽80就可以了，高度看情况调整。
text = ''
for i in range(im.height):
    for j in range(im.width):
        gray = im.getpixel((j, i))      # 返回值可能是一个int, 也可能是一个三元组
        if isinstance(gray, tuple):
            gray = int(0.2126 * gray[0] + 0.7152 * gray[1] + 0.0722 * gray[2])

        text += get_char(gray)
    text += '\n'

with open('pic.txt', 'w')as f:
    f.write(text)