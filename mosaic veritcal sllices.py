from PIL import Image
import numpy as np
import glob
import os 

Image.MAX_IMAGE_PIXELS = 100000000  # For PIL Image error when handling very large images

os.chdir("./data/output/")


#imgs = sorted(glob.glob("*.jpg"))[:50]

imgs = glob.glob("*.jpg")

concatenated = Image.fromarray(
  np.concatenate(
    [np.array(Image.open(x)) for x in imgs],
    axis=0
  )
)

concatenated.save("finale.jpg")