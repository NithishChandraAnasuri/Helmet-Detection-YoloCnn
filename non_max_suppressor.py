# non_max_suppressor.py
import cv2

def apply_nms(boxes, confidences, iou_threshold=0.4):
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, iou_threshold)
    return indexes
