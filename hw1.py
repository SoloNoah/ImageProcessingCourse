import cv2
import matplotlib.pyplot as plt
import numpy as np

''' Noah Solomon 320440621'''

# variables
green = np.uint8([[[0, 255, 0]]])
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])


# reading images from path
input_img = cv2.imread("input.jpg")
background_img = cv2.imread("background.jpg")

# converting to rgb and getting input image's size for resize
input_img = cv2.cvtColor(input_img, cv2.COLOR_BGR2RGB)
width = input_img.shape[1]
height = input_img.shape[0]
dim = (width, height)
background_img = cv2.resize(background_img, dim, interpolation=cv2.INTER_AREA)

# converting to hsv format
studios_hsv = cv2.cvtColor(input_img, cv2.COLOR_BGR2HSV)

# creating mask to detect green within the defined borders and apply bitwise operator on the image
mask = cv2.inRange(studios_hsv, lower_green, upper_green)
res = cv2.bitwise_or(input_img, input_img, mask)

# laying mask over background image
background_masked = cv2.bitwise_and(background_img, background_img, mask=mask)

# inverting mask to get the opposite
mask = np.invert(mask)

# removing green from input
green_removed = cv2.bitwise_or(input_img, input_img, mask=mask)
green_removed = cv2.cvtColor(green_removed, cv2.COLOR_BGR2RGB)

# merging, saving and showing the image
merged = cv2.bitwise_or(background_masked, green_removed)
cv2.imwrite("output.jpg", merged)
plt.imshow(cv2.cvtColor(merged, cv2.COLOR_BGR2RGB))
plt.show()


