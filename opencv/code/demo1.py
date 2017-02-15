# read / write an image

import cv2

img = cv2.imread("cutecat.jpeg")

# we even changed the format
cv2.imwrite("cutecat.png", img)
