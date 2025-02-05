# -*- coding: utf-8 -*-
"""
@author: jimmyc
"""

def make_square(im):
    size = im.size
    if size[0] > size[1]:
        im = im.crop((0, 0, size[1], size[1]))
        return im
    elif size[1] > size[0]:
        im = im.crop((0, 0, size[0], size[0]))
        return im