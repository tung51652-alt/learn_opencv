import cv2 as cv

# img = cv.imread('photos/ca.jpg', 0)
# cv.imshow('ca', img)
# print(img.shape)
# cv.waitKey(0)

#uint8 = unsigned int 2^8

path  = 'video/song.mp4'
vd = cv.VideoCapture(path)
# cv.VideoCapture(0)
while True:
    isTrue, frame = vd.read()

    if(not isTrue):
        break

    cv.imshow('video', frame)
    
    if cv.waitKey(1) == ord('d'): # bấm 'd' để tắt video
        break

vd.release()
cv.destroyAllWindows()

