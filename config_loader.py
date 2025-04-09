# config_loader.py
import cv2

def load_yolo(config_path="yolov3.cfg", weights_path="yolov3.weights", classes_path="coco.names"):
    net = cv2.dnn.readNet(weights_path, config_path)
    with open(classes_path, "r") as f:
        classes = [line.strip() for line in f.readlines()]
    return net, classes
