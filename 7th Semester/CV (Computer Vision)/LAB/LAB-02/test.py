import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'me.JPG'  # Replace with your image path
image = cv2.imread(image_path)

# Perform flips
horizontal_flip = cv2.flip(image, 1)  # Flip horizontally
vertical_flip = cv2.flip(image, 0)    # Flip vertically
both_flip = cv2.flip(image, -1)       # Flip both horizontally and vertically

# Plot the images using Matplotlib
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Original image
axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

# Horizontal flip
axs[0, 1].imshow(cv2.cvtColor(horizontal_flip, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('Horizontally Flipped Image')
axs[0, 1].axis('off')

# Vertical flip
axs[1, 0].imshow(cv2.cvtColor(vertical_flip, cv2.COLOR_BGR2RGB))
axs[1, 0].set_title('Vertically Flipped Image')
axs[1, 0].axis('off')

# Both flips
axs[1, 1].imshow(cv2.cvtColor(both_flip, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('Both Flipped Image')
axs[1, 1].axis('off')

# Show the plot
plt.show()