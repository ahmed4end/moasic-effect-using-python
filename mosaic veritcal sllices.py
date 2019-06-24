from PIL import Image
import numpy as np
import glob
import os 

Image.MAX_IMAGE_PIXELS = 100000000  # For PIL Image error when handling very large images

os.chdir("./data/output/")


imgs = glob.glob("*.jpg")

concatenated = Image.fromarray(
  np.concatenate(
    [np.array(Image.open(x)) for x in [str(i)+".jpg" for i in range(1,len(imgs))]],
    axis=0
  )
)

concatenated.save("output.jpg")
