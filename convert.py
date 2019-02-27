#!/usr/bin/env python

#import os
#import json

from PIL import Image

im = Image.open("selfie-100.png")   

#out = Image.new('I', im.size, 0xffffff)
out = Image.new('P', im.size, 0xffffff)

width, height = im.size

i=1
pixel_colors = []
for x in range(width):
    for y in range(height):
        r,g,b,a = im.getpixel((x,y))

        pixel_color_tuple = (r, g, b)

        p = im.getpixel((x,y))

        print(x)
        print(y)
        print(i)
        print(p)

        out.putpixel((x,y), g)

        pixel_colors.append(str(pixel_color_tuple))

        i += 1

out.save('bar.png')

f = open('bar.json', "w")
f.write('bar_pixels='+str(pixel_colors))
f.close()
