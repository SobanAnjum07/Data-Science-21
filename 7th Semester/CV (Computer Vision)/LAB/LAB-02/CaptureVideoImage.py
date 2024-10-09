# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:59:23 2024

@author: HP
"""

import cv2
capture=cv2.VideoCapture(0) 
while True:
    ret,frame=capture.read() 
    cv2.imshow('Color',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #quits with q
        cv2.imwrite("me.JPG",frame) 
        break
capture.release() 
cv2.destroyAllWindows()
