# -*- coding: utf-8 -*-
"""
@author: jimmyc
"""

from PIL import Image
import os

os.chdir(r"Labs\Lab4")

blank = Image.new('RGB', (1000, 360), 'black')

im1 = Image.open('1.jpg')
im2 = Image.open('2.jpg')
im3 = Image.open('3.jpg')
im4 = Image.open('4.jpg')
im5 = Image.open('5.jpg')
im6 = Image.open('6.jpg')

a,y1 = im1.size
b,y2 = im2.size
c,y3 = im3.size
d,y4 = im4.size
e,y5 = im5.size
f,y6 = im6.size

im1 = im1.resize((int((a*256)/y1), 256))
im2 = im2.resize((int((b*256)/y2), 256))
im3 = im3.resize((int((c*256)/y3), 256))
im4 = im4.resize((int((d*256)/y4), 256))
im5 = im5.resize((int((d*256)/y5), 256))
im6 = im6.resize((int((d*256)/y6), 256))

a,y1 = im1.size
b,y2 = im2.size
c,y3 = im3.size
d,y4 = im4.size
e,y5 = im5.size
f,y6 = im6.size

blank.paste(im1, (31, 20))
blank.paste(im2, (41+a, 60))
blank.paste(im3, (51+a+b, 20))
blank.paste(im4, (61+a+b+c, 60))
blank.paste(im5, (71+a+b+c+d, 20))
blank.paste(im6, (81+a+b+c+d+e, 60))

blank.show()