import cv2
from ultralytics import YOLO

def main():
    # 1. Tải mô hình đã được fine-tune của bạn
    # Đảm bảo file 'best.pt' nằm cùng thư mục với file 'detect.py' này
    try:
        model = YOLO('best.pt')
        print("Đã tải mô hình best.pt thành công!")
    except Exception as e:
        print(f"Lỗi tải mô hình: {e}")
        return

    # 2. Mở luồng video từ webcam (ID = 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Lỗi: Không thể kết nối với Webcam.")
        return
    else:
        print("Đã kết nối Webcam. Nhấn phím 'q' để thoát.")

    # 3. Vòng lặp xử lý hình ảnh trực tiếp
    while True:
        success, frame = cap.read()
        if not success:
            print("Mất tín hiệu camera.")
            break

        # Đưa frame vào mô hình để dự đoán
        results = model.predict(source=frame, conf=0.5, verbose=False) # conf=0.5: Chỉ lấy các dự đoán có độ tin cậy > 50%

        # Vẽ kết quả (bounding box) lên khung hình
        annotated_frame = results[0].plot()

        # Hiển thị lên màn hình
        cv2.imshow("Nhan Dien Trang Thai Ghe Ngoi", annotated_frame)

        # 4. Lắng nghe phím bấm, nhấn 'q' để thoát
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # 5. Dọn dẹp tài nguyên
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()