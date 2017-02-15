import cv2
import copy

cap = cv2.VideoCapture(0)

winName1 = "Live feed"
winName2 = "Grayscale"

cv2.startWindowThread()
cv2.namedWindow(winName1)
cv2.namedWindow(winName2)

ctr = 0
while True:
    ret, f1 = cap.read()
    
    f2
    res = f2 - f1
    
    cv2.imshow(winName1, frame)
    cv2.imshow(winName2, gray)
    ctr = ctr + 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow(winName1)
