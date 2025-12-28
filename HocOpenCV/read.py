import cv2 as cv

# img = cv.imread('photos/son.jpg')
# cv.imshow('goku', img)
# print("hiện ảnh thành công")
# print(img)
# print(img.shape)
# #unit8 = unsigned int 2^8

# cv.waitKey(0)

path  = 'video/song.mp4'
vd = cv.VideoCapture(path)
# cv.VideoCapture(0)
while True:
    isTrue, frame = vd.read()

    if(not isTrue):
        break

    cv.imshow('video', frame)

    if cv.waitKey(20) == ord('d'): # bấm 'd' để tắt video
        break

vd.release()
cv.destroyAllWindows()

