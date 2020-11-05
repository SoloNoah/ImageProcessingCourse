import cv2
import matplotlib.pyplot as plt
import numpy as np

green = np.uint8([[[0, 255, 0]]])

hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)


studio_imgs = cv2.imread("studio4.jpg")
background_imgs = cv2.imread("background3.JPG")

studio_imgs=cv2.GaussianBlur(studio_imgs, (5,5), 0)

studio_imgs = cv2.cvtColor(studio_imgs, cv2.COLOR_BGR2RGB)
background_imgs = cv2.cvtColor(background_imgs, cv2.COLOR_BGR2RGB)

studios_hsv = cv2.cvtColor(studio_imgs, cv2.COLOR_BGR2HSV)

lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])

mask = cv2.inRange(studios_hsv, lower_green, upper_green)

res = cv2.bitwise_or(studios_hsv, studios_hsv, mask=mask)

plt.imshow(mask, cmap="gray")
plt.show()


cv2.imwrite("mask.png", mask)

