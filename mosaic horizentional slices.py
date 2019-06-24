import numpy as np 
from PIL import Image 
import glob
import os 
import random
import time
#import shelve



Image.MAX_IMAGE_PIXELS = 100000000  # For PIL Image error when handling very large images

################################### changing case ###############################################
os.chdir("./data/")
imgs = glob.glob("*.jpg")
#d = shelve.open("temp")
#################################################################################################


target =  np.array(Image.open("target.png"))




def dc(filename): # returns the dominant color of an image.
    #Resizing parameters
    width, height = 150,150
    image = Image.open(filename)
    image = image.resize((width, height),resample = 0)
    #Get colors from image object
    pixels = image.getcolors(width * height)
    #Sort them by count number(first element of tuple)
    sorted_pixels = sorted(pixels, key=lambda t: t[0])
    #Get the most frequent color
    dominant_color = sorted_pixels[-1][1]
    return dominant_color

################################### Option HERE ##########################################

def find_close(target, dict): #finds the closed rgb  to the rgb target 
	dict_values = dict.values()
	randoms = list(map(lambda x: ((target[0] - x[0])**2+(target[1] - x[1])**2+(target[2] - x[2])**2),dict_values))
	return list(dict.items())[randoms.index(min(randoms))]

def find_closeV2(target, dict): #finds the closed rgb  to the rgb target 
	dict_values = dict.values()
	randoms = list(map(lambda x: sum((2+(0.5*(target[0]+x[0])),4,3-(0.5*(target[0]+x[0])))*(np.array(list(target))-x)**2)**0.5,dict_values))
	return list(dict.items())[randoms.index(min(randoms))]
##########################################################################################



############################### STOP POINT ########################
""" if u used find_close() fuction us the first next line of code and disable the one below it otherwise do the opposite."""
#dict = {i:dc(i) for i in imgs}
dict = {i:np.array(list(dc(i))) for i in imgs}
###################################################################


############################# Combining images ####################
n = 0
for i in target:
	n += 1
	finale = [find_close(j, dict)[0] for j in i]


	concatenated = Image.fromarray(
	  np.concatenate(
	    [np.array(Image.open(x)) for x in finale],
	    axis=1
	  )
	)

	concatenated.save(f"./output/{str(n)}.jpg")
