import cv2

# Load the image
image = cv2.imread('IMD2020/1a9tss/c8vklwm_0.png')

# Define the new resolution
new_width = 1800
new_height = 200

# Resize the image
resized_image = cv2.resize(image, (new_width, new_height))

# Save the resized image
cv2.imwrite('examples_input/resized_image22.jpg', resized_image)
