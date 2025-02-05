# -*- coding: utf-8 -*-
"""
@author: jimmyc
"""

from check2_helper import make_square
from PIL import Image 
import os 
os.chdir(r"Labs\Lab4")

blank = Image.new('RGB', (512, 512), 'white')

im = Image.open('im.jpg')
im = make_square(im)
im = im.resize((256, 256))
ca = Image.open('ca.jpg')
ca = make_square(ca)
ca = ca.resize((256, 256))
hk = Image.open('hk.jpg')
hk = make_square(hk)
hk = hk.resize((256, 256))
bw = Image.open('bw.jpg')
bw = make_square(bw)
bw = bw.resize((256, 256))

blank.paste(im, (0, 0))
blank.paste(ca, (256, 0))
blank.paste(hk, (0, 256))
blank.paste(bw, (256, 256))
blank.show()