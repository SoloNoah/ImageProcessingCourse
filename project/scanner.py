import argparse
import cv2
from imutils.perspective import four_point_transform
import imutils
import sys

'''
For a given image in bgr format this function finds its edges and does blurring to clean salt and pepper.
'''
def cannyGaussFilter(img):
    image = cv2.GaussianBlur(img, (5, 5), 0)
    canny = cv2.Canny(image, 0, 100)
    return canny

'''
Reading image and converting to grayscale.
'''
def readImage(path):
    image = cv2.imread(path)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

'''
    Finding 4 contour points in the image.
    
'''
def contours(img):
    cnts = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for c in cnts:
        epsilon = 0.1 * cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, epsilon, True)
        if len(approx) == 4:
            return approx
    raise Exception()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-input', type=str, help='type input image name with format')
    parser.add_argument('-output', type=str, help='location to save image')

    args = parser.parse_args()

    '''
    reading image and saving the ratio of the original picture.
    later we will use this ratio to convert the contours found to the scale of the original image.
    changing the size of the picture to speed up the program with respect to the original ratio.
    
    '''
    image = readImage(args.input)
    ratio = image.shape[0] / 1000.0
    orig = image.copy()
    image = imutils.resize(image, height=1000)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    canny_image = cannyGaussFilter(image)

    '''
        Checks if the function contours has found enough contours (atleast 4).
        if not - stops the program.
    '''
    try:
        aprx = contours(canny_image)
    except:
        sys.exit("Error message: Not enough contour points")

    '''
        Changes the perspective of the picture.
    '''
    warped = four_point_transform(orig, aprx.reshape(4, 2) * ratio)
    cv2.imwrite(args.output, warped)

main()