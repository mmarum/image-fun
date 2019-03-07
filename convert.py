#!/usr/bin/env python

#import os
#import json

from PIL import Image

#image_name = "livi-100.jpg"
image_name = "selfie-100.png"

im = Image.open(image_name)

#out = Image.new('I', im.size, 0xffffff)
out = Image.new('P', im.size, 0xffffff)

width, height = im.size

i=1
pixel_colors = []

for y in range(height):
    for x in range(width):
    
        if image_name.endswith('png'):
            r,g,b,a = im.getpixel((x,y))
        else:
            r,g,b = im.getpixel((x,y))

        pixel_color_tuple = (r, g, b)

        p = im.getpixel((x,y))

        print(i)
        print(p)
        print(x)
        print(y)

        out.putpixel((x,y), g)

        pixel_colors.append(str(pixel_color_tuple))

        i += 1

out.save('bar.png')

f = open('bar.json', "w")
f.write('bar_pixels='+str(pixel_colors))
f.close()
