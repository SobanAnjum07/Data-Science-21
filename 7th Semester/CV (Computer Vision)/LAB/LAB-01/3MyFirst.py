# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:51:26 2024

@author: HP
"""
import numpy as np
import matplotlib.pyplot as plt

print ("My First Python Program")
f = np.arange(12).reshape(3,4) 
print(f)
plt.imshow(f, cmap='gray', interpolation='nearest')
plt.axis('off')
plt.show() 
