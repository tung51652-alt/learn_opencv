import cv2 as cv

img = cv.imread('photos/ca.jpg')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('fish', gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)

c1 = cv.Canny(img, 125, 175)
c2 = cv.Canny(blur, 125, 175)
# cv.imshow('1', c1)
# cv.imshow('2', c2)

# dilated = cv.dilate(c2, (7,7), iterations=3)
# cv.imshow('Dilated', dilated)

eroding = cv.erode(c2, (7,7), iterations= 3)
cv.imshow('erode', eroding)

cv.waitKey(0)
