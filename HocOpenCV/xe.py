import cv2 as cv

img = cv.imread('photos/ban.jpg')
img = cv.resize(img, None, fx = 0.5, fy = 0.5)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY )
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
c = cv.Canny(blur, 5, 25)
dilated = cv.dilate(c, (7,7), iterations=3)
cv.imshow('Dilated', dilated)
cv.waitKey(0)