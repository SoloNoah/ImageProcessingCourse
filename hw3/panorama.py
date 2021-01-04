import cv2
import os.path
from datetime import datetime
import numpy as np
import argparse
import matplotlib.pyplot as plt

start = datetime.now()
axes = []
image_left_path = "1/left.jpg"
image_right_path = "1   /right.jpg"

print(f"[Reading images and converting] start time: {datetime.now()}")
img_left = cv2.imread(image_left_path)
img_right = cv2.imread(image_right_path)

'''change height only later on in a more efficient way'''
height_panorama, w_left = img_left.shape[:2]
h_right, w_right = img_right.shape[:2]
dim = (w_left, height_panorama)


width_panorama = w_left + w_right
img_right = cv2.resize(img_right, dim, interpolation=cv2.INTER_AREA)

left_gray = cv2.cvtColor(img_left, cv2.COLOR_BGR2GRAY)
right_gray = cv2.cvtColor(img_right, cv2.COLOR_BGR2GRAY)

print(f"[Reading images and converting] end time: {datetime.now()}")


print(f"[Calculating sift] start time: {datetime.now()}")

sift = cv2.xfeatures2d.SIFT_create()
print(f"[Calculating sift for left image] start time: {datetime.now()}")
(kps_left, descs_left) = sift.detectAndCompute(left_gray, None)
print(f"[Calculating sift for left image] end time: {datetime.now()}")
print(f"[Calculating sift for right image] start time: {datetime.now()}")
(kps_right, descs_right) = sift.detectAndCompute(right_gray, None)
print(f"[Calculating sift for right image] end time: {datetime.now()}")

print(f"[Brute force matching] start time: {datetime.now()}")

bf = cv2.BFMatcher()
raw_matches = bf.knnMatch(descs_left, descs_right, k=2)
matches = []
ratio = 0.85
for m1, m2 in raw_matches:
    if m1.distance < ratio * m2.distance:
        matches.append(m1)

print(f"[Brute force matching] end time: {datetime.now()}")

print(f"[Matching lines] start time: {datetime.now()}")

img_matches = cv2.drawMatches(img_left, kps_left, img_right, kps_right, matches, None)
plt.imshow(img_matches), plt.show()
print(f"[Matching lines] end time: {datetime.now()}")


src_pts = np.float32([kps_left[m.queryIdx].pt for m in matches]).reshape(-1,1,2)
dst_pts = np.float32([kps_right[m.trainIdx].pt for m in matches]).reshape(-1,1,2)

H, status = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
res = cv2.warpPerspective(img_right, H, (width_panorama, height_panorama))

cv2.imwrite("result.jpg", res)
print(f"[Total time] end time: {start - datetime.now()}")




'''def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("path_left", metavar='path left', type=str,
                       help="Choose path of left image.")
    parse.add_argument("path_right", metavar='path left', type=str,
                       help="Choose path of right image.")
    parse.add_argument("output", metavar='path left', type=str,
                       help="Choose output path.")
    args = parse.parse_args()'''
