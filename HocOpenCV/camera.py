import cv2 as cv

# 1. Khởi động Webcam (Số 0 thường là camera mặc định của laptop)
cap = cv.VideoCapture(0)

# Kiểm tra xem có mở được camera không
if not cap.isOpened():
    print("Không thể mở Camera")
    exit()

print("Nhấn phím 'q' để thoát chương trình.")

while True:
    # 2. Đọc từng khung hình (frame) từ camera
    # ret: Trạng thái đọc (True/False), frame: Hình ảnh nhận được
    ret, frame_goc = cap.read()

    if not ret:
        print("Không nhận được tín hiệu từ Camera (Exiting...).")
        break

    # Chuyển sang ảnh xám
    frame_xam = cv.cvtColor(frame_goc, cv.COLOR_BGR2GRAY)

    # Làm mờ
    frame_mo = cv.GaussianBlur(frame_xam, (7, 7), 0)

    #Tìm biên cạnh (Canny Edge Detection)
    frame_bien = cv.Canny(frame_mo, 50, 150)

    # 1.Hiển thị ảnh gốc (Màu)
    cv.imshow('1. Original (Goc)', frame_goc)

    # 2.Hiển thị ảnh xám
    cv.imshow('2. Grayscale (Xam)', frame_xam)

    # 3.Hiển thị ảnh mờ
    cv.imshow('3. Blurred (Mo)', frame_mo)

    # 4.Hiển thị kết quả ảnh cuối
    cv.imshow('4. Canny Edges (Bien)', frame_bien)

   
    if cv.waitKey(1) == ord('q'):
        break


cap.release()
cv.destroyAllWindows()