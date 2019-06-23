import numpy as np 
from PIL import Image
import glob, os

os.chdir("./data/")

im = Image.open("a.jpg").resize((100,100)).save("a.png")

'''
imgs = glob.glob("*.jpg")[:-1]

for i in imgs:
	im = Image.open(i).resize((50, 50))
	im.save(i[:-4]+".png")
	os.remove(i)'''