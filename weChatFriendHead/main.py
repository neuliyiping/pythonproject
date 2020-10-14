import itchat
import os

import PIL.Image as Image
import random

friends_header_image_dir = './friends_list/'
friends_header_image={}

image_pool=[]


def write_image(name, image):
    if not os.path.exists(friends_header_image_dir):
        os.mkdir(friends_header_image_dir)

    with open(friends_header_image_dir + name + '.jpg', "wb") as f:
        f.write(image)



def getImage():
    print("can login in successfully")
    friends_list = itchat.get_friends()
    for item in friends_list:
        # > file  将个性签名重定向到一个文本文件
        print(item['Signature'])
        write_image(item['NickName'],itchat.get_head_img(item['UserName']))


def login():
    itchat.auto_login(hotReload=True, loginCallback = getImage)

def readsource():
    #将上一步保存的图片添加到一个列表
    for item in os.listdir(friends_header_image_dir):
        image_pool.append(item)

def puzzle():

    #每行几个，每列几个，建议自己根据好友数量手算一下
    row = 15
    col = 19

    print(row, col)
    num = 0
    base_image = Image.new('RGB',(row * 128, col * 128))

    for r in range(1, row+1):
        for c in range(1, col+1):
            image = Image.open(friends_header_image_dir + image_pool[num]).resize((128,128), Image.ANTIALIAS)
            #将每一个压缩过后的图像沾到base image上
            base_image.paste(image, ((r - 1) * 128, (c - 1) * 128))
            num += 1
            if num == len(image_pool):
                num = random.randint(0,len(image_pool))

    base_image.save('./puzzle.jpg')

if __name__ == '__main__':
    login()
    readsource()
    puzzle()
