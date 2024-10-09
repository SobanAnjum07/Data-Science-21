import cv2
import matplotlib.pyplot as plt

# Load the image
image_path = 'me.JPG'  # Replace with your image path
image = cv2.imread(image_path)

# Function to rotate an image
def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Get the rotation matrix
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    
    return rotated

# Perform rotations
rotation_90 = rotate_image(image, 90)
rotation_180 = rotate_image(image, 180)
rotation_270 = rotate_image(image, 270)
rotation_360 = rotate_image(image, 360)  # This will give the original image

# Plot the images using Matplotlib
fig, axs = plt.subplots(2, 2, figsize=(10, 10))

# Original image
axs[0, 0].imshow(cv2.cvtColor(rotation_90, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('90° Rotated Image')
axs[0, 0].axis('off')

# 180° rotated image
axs[0, 1].imshow(cv2.cvtColor(rotation_180, cv2.COLOR_BGR2RGB))
axs[0, 1].set_title('180° Rotated Image')
axs[0, 1].axis('off')

# 270° rotated image
axs[1, 0].imshow(cv2.cvtColor(rotation_270, cv2.COLOR_BGR2RGB))
axs[1, 0].set_title('270° Rotated Image')
axs[1, 0].axis('off')

# 360° rotated image (same as original)
axs[1, 1].imshow(cv2.cvtColor(rotation_360, cv2.COLOR_BGR2RGB))
axs[1, 1].set_title('360° (Original) Image')
axs[1, 1].axis('off')

# Show the plot
plt.show()