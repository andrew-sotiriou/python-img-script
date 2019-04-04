import sys
from PIL import Image, ImageFont, ImageDraw

def imgCropWidth(img):
	basewidth = 292
	wpercent = (basewidth/float(im.size[0]))
	hsize = int((float(im.size[1])*float(wpercent)))
	img = im.resize((basewidth,hsize), Image.ANTIALIAS)
	return img

def imgCropHeight(img):
	baseheight = 106
	hpercent = (baseheight / float(img.size[1]))
	wsize = int((float(img.size[0]) * float(hpercent)))
	img = img.resize((wsize, baseheight), Image.ANTIALIAS)
	return img

def fullCrop(im):
	postop = int(((im.size[1] - 106))/2)
	posleft = int(((im.size[0] - 292))/2)
	left = posleft
	top = postop
	box = (left, top, 292+left, 106+top)
	area = im.crop(box)
	return area

def addLayer(im,yaxis):
	overlay = Image.open("overlay.png")
	overlay = overlay.convert("RGBA")
	mask=Image.new('RGBA', im.size, color=(100,100,100,100))
	background =im.paste(overlay,(0,yaxis),mask)
	return im

def writeText(im,text):
	font = ImageFont.truetype("helvetica_neue_bold.ttf", 12)
	lines = []
	words = text.split()
	if len(stringer) >= 42:
		current_string = ""
		for word in words:
			if (len(current_string) + len(word)) <= 42:
				current_string += ' ' + word
			else:
				lines.append(current_string.lstrip(' '))
				current_string = word                    
		if current_string: lines.append(current_string)
	else:
		lines.append(stringer)
	if len(lines) > 1:
		yxis = 82 - (10*(len(lines)-1))
		addLayer(im,yxis)
	else:
		addLayer(im,82)
	draw = ImageDraw.Draw(im)
	yaxis = 85
	if len(lines) == 1:
		draw.text((5, yaxis),lines[0],(255,255,255),font=font)
	else:
		counter = len(lines)-1
		while counter >=0:
			sample = lines[counter]
			draw.text((5, yaxis),sample,(255,255,255),font=font)
			counter=counter-1
			yaxis=yaxis-12
	return (im)

im = Image.open('test.jpg')

if (float(im.size[1]) * 2.75472)/292 > (float(im.size[0]) * 0.363013)/106:
	newimg = imgCropWidth(im)
	newimg2 = fullCrop(newimg)
else:
	newimg = imgCropHeight(im)
	newimg2 = fullCrop(newimg)

stringer = "Text for overlay"

newimg2 = writeText(newimg2,stringer)

newimg2.save('new.png')
