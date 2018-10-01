import cv2
from matplotlib import pyplot as plt
import glob

THRESHOLD = 80
BLURSIZE = (15, 15)
MIN_AREA = 800
DT = 0.1

folder = './input/test2/'
pics = sorted(glob.glob(folder+'*.png'))

# Find base image
image = cv2.imread(pics[0], 1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
base_gray = cv2.GaussianBlur(gray, BLURSIZE, 0)
base_image = base_gray.copy().astype("float")


for pic in pics:
    image = cv2.imread(pic, 1)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    new_gray = cv2.GaussianBlur(gray, BLURSIZE, 0)
    new_image = new_gray.copy().astype("float")


    frameDelta = cv2.absdiff(new_gray, cv2.convertScaleAbs(base_image))
    thresh = cv2.threshold(frameDelta, THRESHOLD, 255, cv2.THRESH_BINARY)[1]

    thresh = cv2.dilate(thresh, None, iterations=2)
    (_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    # look for motion
    motion_found = False
    biggest_area = 0
    # examine the contours, looking for the largest one
    x,y,h,w = 0,0,0,0
    for c in cnts:
        (x1, y1, w1, h1) = cv2.boundingRect(c)
        # get an approximate area of the contour
        found_area = w1 * h1
        # find the largest bounding rectangle
        if (found_area > MIN_AREA) and (found_area > biggest_area):
            biggest_area = found_area
            motion_found = True
            x = x1
            y = y1
            h = h1
            w = w1

    if motion_found:
        plt.subplot(221)
        plt.imshow(base_gray)

        plt.subplot(222)
        plt.imshow(new_gray)

        plt.subplot(223)
        plt.imshow(frameDelta)

        plt.subplot(224)
        plt.imshow(thresh)
        plt.plot([x, x+w, x+w, x, x], [y, y, y+h, y+h, y])

        plt.show()



