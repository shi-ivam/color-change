from itertools import count
from turtle import color
import cv2
import numpy as np
import json
from PIL import Image
from math import sqrt




# Config Start

loop_constant = 80000
number_of_different_colors = 15

# Config End


COLORS = [
    [3,43,80],[1,128,214],[2,70,143]
]
def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

img = Image.open('resize.png')
img = img.convert('RGB')
print(img.mode)


# list of unique colors
colors = []

# for c in img.getcolors():
#     if c not in 


max_length = loop_constant
long_list = img.getdata()
spacing = len(long_list) // max_length

if spacing == 0:
    spacing = 1

# type of long_list
# skip values to make the length max_length
long_list2 = list(long_list)[::int(spacing)]
count=0
for pixel in long_list2:
    print(str(count) + '/' + str(len(long_list2)),end="\r")
    count+=1
    found = False
    index = None
    # find if the color is in the list
    for index,color in enumerate(colors):
        color_value = color['color']
        if color_value == pixel:
            found = True
            index = index

    if found:
        # print('increasing')
        colors[index]['count'] += 1
    else:
        obj = {
            "color":pixel,
            "count":1
        }
        if obj not in colors:
            colors.append(obj)
# get the top 10 most common colors
colors.sort(key=lambda x: x["count"], reverse=True)
colors = colors[:number_of_different_colors]

# get color values
colors_values = []
for color in colors:
    colors_values.append(color['color'])

COLORS = colors_values.copy()

print(COLORS)

width = img.size[0] 
height = img.size[1] 




for i in range(0,width):# process all pixels
    for j in range(0,height):
        data = img.getpixel((i,j))
        #print(data) #(255, 255, 255)
        if  not (data == (14,14,14)):
            close = closest_color(data)
            img.putpixel((i,j),(close[0],close[1],close[2]))
img.show()