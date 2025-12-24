import cv2 as cv

# vd = cv.VideoCapture('video/song.mp4')

# while True:
#     isTrue, frame = vd.read()

#     cv.imshow('video', frame)

#     if cv.waitKey(20) & 0xFF == ord('d'): # bấm 'd' để tắt video
#         break

# vd.release()
# cv.destroyAllWindows()

img = cv.imread('photos/son.jpg')
cv.imshow('goku', img)
cv.waitKey(0)