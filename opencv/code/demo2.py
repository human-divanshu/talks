# read / write an image

import cv2

# see flags for your version of opencv in documenation
img = cv2.imread("cutecat.jpeg", cv2.CV_LOAD_IMAGE_GRAYSCALE)

# we even changed the format
cv2.imwrite("graycat.png", img)
