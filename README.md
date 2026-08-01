# Real-time Chair Occupancy Detection (Nhận Diện Trạng Thái Ghế Ngồi) 🪑

---

## 📝 Tổng quan dự án
Xây dựng hệ thống nhận diện trạng thái ghế ngồi theo thời gian thực từ luồng video camera nhằm hỗ trợ giám sát và tối ưu hóa việc quản lý không gian tại thư viện, phòng học và các khu vực công cộng.

## 🛠️ Trách nhiệm chính & Cấu trúc thực hiện
* **Xây dựng dữ liệu:** Thu thập, tiền xử lý và xây dựng tập dữ liệu gồm hai lớp đối tượng (*person* và *chair*) phục vụ huấn luyện mô hình.
* **Huấn luyện AI:** Fine-tune mô hình **YOLOv8** trên tập dữ liệu tùy chỉnh nhằm nâng cao khả năng phát hiện đối tượng trong môi trường thực tế.
* **Phát triển thuật toán logic:** Xây dựng thuật toán xác định trạng thái **Occupied/Vacant** (Đang sử dụng/Trống) dựa trên mối quan hệ không gian giữa người và ghế thông qua chỉ số **Intersection over Union (IoU)** và khoảng cách tâm đối tượng.
* **Xây dựng Pipeline:** Phát triển luồng xử lý video thời gian thực bằng **OpenCV**, thực hiện nhận diện, theo dõi đối tượng và cập nhật trạng thái ghế theo từng khung hình.
* **Tối ưu hóa hệ thống:** Tối ưu tốc độ suy luận và hiển thị kết quả trực quan với bounding box, nhãn đối tượng và thống kê số lượng ghế trống/đang sử dụng theo thời gian thực.

## 📈 Kết quả đạt được
* Hệ thống hoạt động ổn định trên luồng webcam/video thời gian thực.
* Đạt khoảng **70% độ chính xác** trong bài toán nhận diện trạng thái ghế ngồi trên tập dữ liệu thử nghiệm.
* Giảm đáng kể thời gian kiểm tra thủ công và tạo nền tảng cho các ứng dụng quản lý không gian thông minh.

## 💻 Công nghệ sử dụng
* **Ngôn ngữ lập trình:** Python
* **Machine Learning / Deep Learning:** YOLOv8, PyTorch
* **Xử lý ảnh & Tính toán:** OpenCV, NumPy
* **Lĩnh vực ứng dụng:** Computer Vision, Object Detection, Object Tracking
