# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:59:36 2024

@author: HP
"""

from PIL import Image

filename = "cat_hat.jpg"
with Image.open(filename) as image:
    width, height = image.size
print(image.size)
print(width,height)
#Image.size gives  2-tuple and the width, height can be obtained

