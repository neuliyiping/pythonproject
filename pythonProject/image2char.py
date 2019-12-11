from PIL import Image
import argparse
#设置命令行参数
parser=argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o','--output')
parser.add_argument('--width',type=int)
parser.add_argument('--height',type=int)

#获取参数
args=parser.parse_args()

image=args.file
width=args.width
height=args.height
output=args.output

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
# 将256灰度映射到70个字符上
def get_char(r,g,b,alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':
    im = Image.open(image)
    if width and height:
        im = im.resize((width,height), Image.NEAREST)
    else:
        width,height=im.size
        im = im.resize((width, height), Image.ANTIALIAS)
    txt = ""
    #将图片看成由像素点组成的二维数组，i代表每一行，j代表每一列
    for i in range(height):
        for j in range(width):
            #getpixel()函数的参数是由每个像素点在图片中的相对位置（w，h）组成的元组
            #返回值是一个代表图片像素值的(r,g,b,alpha)元组
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)
    #字符画输出到文件
    if output:
        with open(output,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)