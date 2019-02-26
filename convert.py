#!/usr/bin/env python

from PIL import Image

im = Image.open("selfie-200.png")   

out = Image.new('I', im.size, 0xffffff)

width, height = im.size

i=1

for x in range(width):

    for y in range(height):

        #r,g,b = im.getpixel((x,y))
        print(i)
        print(im.getpixel((x,y)))

        #if b < g and b < r or r==g==b:

        i += 1

        out.putpixel((x,y), 0)

#            #out.putpixel((x,y), 0)

#out.save('bar.png')
