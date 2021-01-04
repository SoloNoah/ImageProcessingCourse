import cv2
import os.path
from datetime import datetime
import argparse
import matplotlib.pyplot as plt

axes = []
image_left_path = "1/left.jpg"
image_right_path = "1/right.jpg"
img_left = cv2.imread(image_left_path)
img_right = cv2.imread(image_right_path)
left_gray = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
right_gray = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
(kps_left, descs_left) = sift.detectAndCompute(left_gray, None)
(kps_right, descs_right) = sift.detectAndCompute(right_gray, None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)
matches = bf.match(descs_left, descs_right)
matches = sorted(matches, key=lambda x: x.distance)
img3 = cv2.drawMatches(img_left, kps_left, img_right, kps_right,matches[:50], img_right, flags=2)
plt.imshow(img3),plt.show()
''' add_subplot gets rows, columns and index indicating where the image will be shown
can be refactored into a function reading both images from folder in a loop or in a better way
will work for now'''
'''fig = plt.figure()
axes.append(fig.add_subplot(1, 2, 1))
plt.imshow(left_gray)
axes.append(fig.add_subplot(1, 2, 2))
plt.imshow(right_gray)
plt.show()'''



'''def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("path_left", metavar='path left', type=str,
                       help="Choose path of left image.")
    parse.add_argument("path_right", metavar='path left', type=str,
                       help="Choose path of right image.")
    parse.add_argument("output", metavar='path left', type=str,
                       help="Choose output path.")
    args = parse.parse_args()'''