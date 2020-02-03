from PIL import	Image

def load_and_cut_pic(path):
	image=Image.open(path)
	width,height=image.size
	every_width=int(width/3)
	every_height=int(height/3)
	lis=[]
	for i in range(0,3):
		for j in range(0,3):
			item=(j*every_width,i*every_height,(j+1)*every_width,(i+1)*every_height)
			lis.append(item)

	image_list=[image.crop(i) for i in lis]

	return image_list

def save(image_list):
	count=1;
	for item in image_list:
		item.save(str(count)+'.jpg')
		count+=1

if __name__ == '__main__':
	path=r'F:\Chorm download\桌面背景\456.jpg'
	image_list=load_and_cut_pic(path)

	save(image_list)


from PIL import	Image,ImageDraw

def load_and_cut_and_save_pic(path,width_num,height_num):
	"""
	width_num:横着分几份
	height_num:竖着分几份
	"""
	image=Image.open(path)
	width,height=image.size
	draw = ImageDraw.Draw(image)
	every_width=int(width/width_num)
	every_height=int(height/height_num)
	for i in range(1,width_num):
		draw.line((0,every_width*i,height,every_width*i),'white',width=5)

	for i in range(1,height_num):
		draw.line((every_height*i,0,every_height*i,width),'white',width=5)
	image.save('res1.jpg')

if __name__ == '__main__':
	path=r'F:\Chorm download\桌面背景\456.jpg'
	image_list=load_and_cut_and_save_pic(path,3,3)


