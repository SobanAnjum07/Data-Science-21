#from PIL import Image



import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread("cameraman.png")
# Read the image

# Window name in which image is displayed
window_name = 'CameraMan'

cv.imshow(window_name,image)
print(image.shape)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv.waitKey(0)

# closing all open windows
cv.destroyAllWindows()

f = np.arange(12).reshape(3,4) 
plt.imshow(f, cmap='gray', interpolation='nearest')
plt.show() 
print(f.shape) 
####################################

f = plt.imread('peppers.png') 
plt.imshow(f) 
plt.show()
print(f.shape) 

