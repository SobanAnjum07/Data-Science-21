# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:36:10 2024

@author: HP
"""

import matplotlib.pyplot as plt 
from skimage import data 
from skimage.color import rgb2gray 
original = data.cat() 
grayscale = rgb2gray(original) 
fig, axes = plt.subplots(1, 2, figsize=(8, 4)) 
ax = axes.ravel() 
ax[0].imshow(original) 
ax[0].set_title("RGB") 
ax[1].imshow(grayscale, cmap=plt.cm.gray) 
ax[1].set_title("Grayscale") 
fig.tight_layout() 
plt.show()
