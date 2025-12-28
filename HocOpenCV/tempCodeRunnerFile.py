img = cv.imread('photos/son.jpg')
img1 = rescaleFrame(img, 0.1)
cv.imshow('goku', img1)
cv.waitKey(0)