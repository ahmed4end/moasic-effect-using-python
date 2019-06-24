import numpy as np 
from PIL import Image
import glob, os,random

try:
	os.makedirs("./data/output/")
except:
	pass
os.chdir("./data/")

#im = Image.open("a.jpg").resize((100,100)).save("a.png")


imgs = glob.glob("*.jpg") + glob.glob("*.png")

try:
	imgs.remove("target.png")
except:
	pass



for i in imgs:
    im = Image.open(i).resize((20, 20))
    im.save(i[:-4]+".jpg")

imgs = glob.glob("*.jpg") + glob.glob("*.png")

try:
	imgs.remove("target.png")
except:
	pass

for i in imgs:
    if imgs.count(i) >= 2:
        os.remove(i)

imgs = glob.glob("*.jpg")

try:
	imgs.remove("target.png")
except:
	pass

def add_order(imgs): # naming the image used in order 1,2,3....(.jpg) only use it once when starting .
    n = random.randint(1,10000)
    for i in range(len(imgs)):
        os.rename(imgs[i], str(i+n)+".jpg")


add_order(imgs)
