import cv2 as cv
import numpy as np

# tạo ra một ma trận kích cỡ 500 pixel x 500 pixel, và có 3 chiều màu sắc 
blank  = np.zeros((800,500,3), dtype = 'uint8')
# print(blank)
# cv.imshow('blank1', blank)

# khổng gian 3 chiều này là dài, rộng và màu sắc 
# kiểu dữ liệu ở đâu là unsign int (số nguyên ko âm) và biểu diễn ở dạng 8 bit 
# blank[:] = 0, 150, 100
# blank[100:200, 100 : 200] = 0, 100, 100
# blank[200:300] = 0, 100, 200
# img = cv.imread('photos/ca.jpg')
# img[0 : img.shape[0] // 2, 0 : img.shape[1] // 2], img[0 : img.shape[0] // 2, 0 : img.shape[1] // 2], img[0 : img.shape[0] // 2, 0 : img.shape[1] // 2] = 0, 100, 0
# cv.imshow('blank2', img)
#print(blank)
# vẽ hình chữ nhật
# Vẽ hình chữ nhật viền xanh lá

#cv.rectangle(img, pt1, pt2, color, thickness)

# cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=30)


# Vẽ hình chữ nhật đặc (tô kín màu)
#cv.rectangle(blank, (0,0), (250,500), (0,255,0), thickness=cv.FILLED)
#cv.imshow('blank', blank)
# #vẽ hình chữ nhật che 1/4 màn
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)

# #vẽ đường
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)


# cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
# cv.imshow('blank', blank)



cv.waitKey(0)