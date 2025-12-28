import cv2 as cv

img = cv.imread('photos/xe1.jpg')
img = cv.resize(img, None, fx = 0.5, fy = 0.5)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
c2 = cv.Canny(blur, 125, 175)
d = cv.dilate(c2, (7,7), iterations=3)
cv.imshow('Dilated', c2)
cv.waitKey(0)