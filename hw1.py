import cv2
import matplotlib.pyplot as plt
import numpy as np

green = np.uint8([[[0, 255, 0]]])

hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)

#reading images from path
studio_imgs = cv2.imread("studio4.jpg")
background_imgs = cv2.imread("background3.JPG")

#converting to rgb
studio_imgs = cv2.cvtColor(studio_imgs, cv2.COLOR_BGR2RGB)
background_imgs = cv2.cvtColor(background_imgs, cv2.COLOR_BGR2RGB)

#converting to hsv format
studios_hsv = cv2.cvtColor(studio_imgs, cv2.COLOR_BGR2HSV)

#setting lower and upper green boundries
lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])

#creating mask to detect green within the defined borders and apply bitwise operator on the image
mask = cv2.inRange(studios_hsv, lower_green, upper_green)
res = cv2.bitwise_or(studio_imgs, studio_imgs, mask)

plt.imshow(mask, cmap="gray")
plt.show()

'''
TODO:   1) figure out how to blend background in var res after the mask has been applied
        2) remove green from original pic
        3) the last step is probably applying bitwise_or on images from (1) and (2)
        4) add argsparse to make it possible for the script to run on images from directory given as input

'''

#cv2.imwrite("mask.png", mask)

