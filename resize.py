import PIL
import os
import os.path
from PIL import Image

f = 'output'

for file in os.listdir(f):
    
    f_img =  f+"/"+file
    img = Image.open(f + "/" + file)
    
    # crop a square at the centre
    width, height = img.size
    size = min(width, height)
    left = (width - size) / 2
    top = (height - size) / 2
    right = (width + size) / 2
    bottom = (height + size) / 2
    img = img.crop((left, top, right, bottom))
    img.resize((500,500))
    img.save(f_img)
 # ffmpeg -framerate 10 -i out%4d.png Project.mp4