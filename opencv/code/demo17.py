import cv2

cap = cv2.VideoCapture("people-walking.mp4")

fgbg = cv2.BackgroundSubtractorMOG()

winName1 = "Live feed"
winName2 = "Motion detection"

cv2.startWindowThread()

cv2.namedWindow(winName1)
cv2.namedWindow(winName2)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    
    cv2.imshow(winName1, frame)
    cv2.imshow(winName2, fgmask)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindow(winName1)
cv2.destroyWindow(winName2)
