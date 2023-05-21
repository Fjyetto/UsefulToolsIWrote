import PIL
from PIL import Image
import numpy as np
import colorsys
import random

rgb_to_hsv = np.vectorize(colorsys.rgb_to_hsv)
hsv_to_rgb = np.vectorize(colorsys.hsv_to_rgb)

# this takes an image and makes a gif of it with its hue shifting

def shift_hue(arr, hout):
    r, g, b, a = np.rollaxis(arr, axis=-1)
    h, s, v = rgb_to_hsv(r, g, b)
    h+= hout
    r, g, b = hsv_to_rgb(h, s, v)
    arr = np.dstack((r, g, b, a))
    return arr

def colorize(image, hue):
    """
    Colorize PIL image `original` with the given
    `hue` (hue within 0-360); returns another PIL image.
    """
    img = image.convert('RGBA')
    arr = np.array(np.asarray(img).astype('float'))
    new_img = Image.fromarray(shift_hue(arr, hue/360.).astype('uint8'), 'RGBA')

    return new_img

direc = input("Image file directory:")
im = Image.open(direc)
fps = int(input("Input FPS : "))
dur = 1/fps

#create the actual gif
Frames = []
for x in range(90):
	Frames.append(colorize(im,4*x))
	print(x)
	
Frames[0].save("RAINBOW"+str(random.randint(1,65536))+".gif",transparency=0,save_all=True,append_images=Frames[1:],optimize = False, duration=dur, loop=0)