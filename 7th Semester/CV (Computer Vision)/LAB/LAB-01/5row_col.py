# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import imageio as io
import matplotlib.pyplot as plt


img = io.imread('book_gray.png')
print(img.shape)

r,c = img.shape[0],img.shape[1]



print ('Image has ', r , 'rows and ', c, 'cols')
#print all values of image
print(img)
# =============================================================================
#Print all values of image
# for i in range (r):
#     for j in range (c):
#         print (i,j)
# 
# =============================================================================


plt.hist(img,bins=10)
plt.show()
plt.close()
 
