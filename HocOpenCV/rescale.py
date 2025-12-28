import cv2 as cv

def rescaleFrame(frame, scale = 0.75):
    # phải ép kiểu vì máy tính nó không hiện đc nửa điểm ảnh
    width = int(frame.shape[1] * scale) # trả về cột nên đưa ra chiều dài
    height = int(frame.shape[0] * scale) # trả về hàng nên đưa ra chiều rộng
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation= cv.INTER_AREA)
    # sử dụng thuật toán nội suy để thu nhỏ lại (INTER_AREA), phóng to ta dùng (INTER_LINEAR)

vd = cv.VideoCapture('video/song.mp4')

while True:
    isTrue, frame = vd.read()

    frame_rescale = rescaleFrame(frame, 0.2)

    cv.imshow('video1', frame_rescale)

    if cv.waitKey(20) & 0xFF == ord('d'): # bấm 'd' để tắt video
        break

vd.release()
cv.destroyAllWindows()

# img = cv.imread('photos/son.jpg')
# img1 = rescaleFrame(img, 0.1 )
# cv.imshow('goku', img1)
# cv.waitKey(0)