Object Detection using YOLO (You Only Look Once)

This project implements real-time object detection using the **YOLOv3 algorithm**, leveraging deep learning and convolutional neural networks (CNNs). It demonstrates how to detect multiple objects (like people, vehicles, helmets, etc.) in images and video streams using a single-pass CNN model.

---

## 📌 Project Overview

Object detection plays a critical role in many real-world applications such as:

- 🚗 Autonomous driving
- 🛡️ Workplace safety monitoring
- 🧍 Human detection in surveillance
- 🎯 Smart traffic control systems

In this project, we use the YOLOv3 model, a fast and accurate object detection algorithm that frames detection as a single regression problem, straight from image pixels to bounding box coordinates and class probabilities.

---

## 🚀 Key Features

- 🔍 Real-time object detection with YOLOv3
- ⚡ High frame rate (~45 FPS)
- 📦 Uses OpenCV for image and video processing
- 🎯 Non-Maximum Suppression (NMS) for eliminating redundant bounding boxes
- 🧠 Anchor box and confidence threshold support

---

## 📂 Project Structure

```
📁 Helmet-Detection-YoloCnn/
│
├── yolov3.cfg                 # YOLOv3 architecture config file
├── yolov3.weights             # Pretrained weights (Git LFS tracked)
├── coco.names                 # List of 80 object classes
├── main_object_detection.py   # Main script for detection
├── utils/
│   ├── config_loader.py
│   ├── draw_boxes.py
│   ├── image_preprocessor.py
│   └── other utilities...
├── test_images/
│   └── your_test_images.jpg
├── README.md
├── LICENSE
└── requirements.txt
```

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/NithishChandraAnasuri/Helmet-Detection-YoloCnn.git
cd Helmet-Detection-YoloCnn
```

### 2. Install Dependencies

Make sure Python and pip are installed, then:

```bash
pip install -r requirements.txt
```

> ⚠️ Note: `yolov3.weights` is over 200MB and managed using Git LFS. Make sure [Git LFS](https://git-lfs.github.com/) is installed before cloning.

### 3. Run Object Detection

```bash
python main_object_detection.py
```

---

## 📊 How It Works

- The image is divided into a grid (e.g. 19x19)
- Each grid cell predicts:
  - 5 anchor boxes
  - Confidence scores
  - Bounding box coordinates
  - Class probabilities
- Non-Max Suppression filters overlapping predictions
- The final bounding boxes and labels are drawn on the image

---


## 📈 Performance

- YOLO processes images in a single pass → very fast
- More efficient than CNN-based region proposals (like R-CNN, Fast-RCNN)
- Ideal for real-time detection applications

---

## 📌 Conclusion

This project showcases the power of YOLOv3 and CNNs in object detection. Compared to traditional methods, YOLO offers:

- ⚡ Speed (real-time performance)
- 🎯 Accuracy (low false positives)
- 🔁 Simplicity (single neural network)

It serves as a strong foundation for future work in safety enforcement, surveillance, or automation.

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more info.

---

## 🙌 Contributors

- 👨‍💻 A. Nithish Chandra — [LinkedIn](https://www.linkedin.com/in/nithish-chandra-anasuri-411017290/) | [GitHub](https://github.com/NithishChandraAnasuri)

---

## 📚 References

- [YOLOv3 Paper](https://pjreddie.com/media/files/papers/YOLOv3.pdf)
- [OpenCV Documentation](https://docs.opencv.org/)
- [Joseph Redmon’s YOLO GitHub](https://github.com/pjreddie/darknet)

```

