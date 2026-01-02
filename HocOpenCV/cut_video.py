import cv2 as cv


capture = cv.VideoCapture('video/song.mp4')

current_frame = 0

while True:
    
    isTrue, frame = capture.read()
    
    if not isTrue:
        break
    
    path = f'frames_folder/frame_{current_frame}.jpg'
    if(current_frame % 30 == 0):
        cv.imwrite(path, frame)
        print(f'Da luu: {path}')

    current_frame += 1 

# Giải phóng bộ nhớ
capture.release()
print("Hoan thanh viec cat video!")