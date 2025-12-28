import cv2 as cv


img = cv.imread('photos/son.jpg')

img1 = cv.resize(img, (400,200))


img2 = cv.resize(img, None, fx = 0.1, fy = 0.1)


cv.imshow('goku1', img1)
cv.imshow('goku2', img2)
cv.waitKey(0)