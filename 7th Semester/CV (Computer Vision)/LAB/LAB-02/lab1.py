import cv2
import matplotlib.pyplot as plt

image = cv2.imread(r'image.png', cv2.IMREAD_COLOR)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
weightedSum = cv2.add(gray, 90)
weightedSubtract = cv2.subtract(gray, 90)
weightedMultiply = cv2.multiply(gray, 1.5)
invert = cv2.bitwise_not(gray)

fig = plt.figure(figsize=(9, 9))

fig.add_subplot(3, 3, 1)
plt.title('Original')
plt.imshow(image)

fig.add_subplot(3, 3, 2)
plt.title('Gray')
plt.imshow(gray, cmap=plt.cm.gray)

fig.add_subplot(3, 3, 3)
plt.title('Add')
plt.imshow(weightedSum, cmap=plt.cm.gray)

fig.add_subplot(3, 3, 4)
plt.title('Sub')
plt.imshow(weightedSubtract, cmap=plt.cm.gray)

fig.add_subplot(3, 3, 5)
plt.title('Multiply')
plt.imshow(weightedMultiply, cmap=plt.cm.gray)

fig.add_subplot(3, 3, 6)
plt.title('Invert')
plt.imshow(invert, cmap=plt.cm.gray)

plt.show()
