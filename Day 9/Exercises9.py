#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 12:04:17 2019

@author: nada
"""

#Exercises DAY Nine
print('-------------Exercise 1------------------')
import statistics as st

x=[3,1.5,4.5,6.75,2.25,5.75,2.25]

print(st.mean(x))
print(st.harmonic_mean(x))
print(st.median(x))
print(st.median_low(x))
print(st.median_high(x))
print(st.median_grouped(x))
print(st.mode(x))
print(st.pstdev(x))
print(st.pvariance(x))
print(st.stdev(x))
print(st.variance(x))

print('-------------Exercise 2------------------')

import random

print( random.random())
print ( random.randrange(10))
print ( random.choice(['Ali', 'Khalid', 'Hussam']))
print ( random.sample(range(1000), 10))
print ( random.choice('Orange Academy') )

e2 = [1,5,8,9,2,4]
random.shuffle(e2)
print( e2 )

print ( random.randint(20, 30))
print ( random.randrange(1000, 2111, 5))
print ( random.uniform(10000, 11000))


print('-------------Exercise 3------------------')

import math
print ('pi: %.10f' % math.pi)
print(math.cos(200))
print(math.sin(30))
print(math.tan(180))

print(math.floor(10.8))
print(math.ceil(10.8))

print('-------------Exercise 4------------------')

from PIL import Image , ImageFilter
from PIL import ImageDraw 

img=Image.open("1.jpg")

print(img.format,img.size,img.mode)
img.show()

e4=img.transpose(Image.FLIP_TOP_BOTTOM)
e4.show()

e41=img.convert('L')
e41.show()

croped=img.crop((0,0,50,50))
croped.show()


draw=ImageDraw.Draw(img)
draw.line((0,0)+img.size, fill=(255,255,255))
draw.line((0, img.size[1], img.size[0],0),fill=(255,255,255))
img.show()


newimage=img.filter(ImageFilter.EDGE_ENHANCE)
newimage1=img.filter(ImageFilter.FIND_EDGES)
newimage2=img.filter(ImageFilter.SMOOTH)
newimage3=img.filter(ImageFilter.SHARPEN)

newimage.show()
newimage1.show()
newimage2.show()
newimage3.show()

alpha=0.5
imge1=Image.open('1.jpg')
imge2=Image.open('2.jpg').resize(imge1.size)

Image.blend(imge1,imge2,alpha).save("new.jpg".format(alpha))

im=Image.open("new.jpg")
im.show()



e42=img.filter(ImageFilter.BLUR)
e42.show()



size=(128,128)
img.thumbnail(size)
img.show()

e43=img.rotate(90)
e43.show()


imge1=Image.open('1.jpg')
imge2=Image.open('2.jpg').resize(imge1.size)
mask=Image.open('mask_tril_01.jpg')
mask=mask.resize(imge1.size)

Image.composite(imge1,imge2,mask).save('Image_composite_01.jpg')\

im=Image.open('Image_composite_01.jpg')

im.show()