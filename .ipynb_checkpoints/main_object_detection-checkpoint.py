# main_object_detection.py

import matplotlib.pyplot as plt
import cv2

from config_loader import load_yolo
from image_preprocessor import preprocess_image
from output_parser import parse_output
from non_max_suppressor import apply_nms
from draw_boxes import draw_labels

# Load model and classes
net, classes = load_yolo()

# Prepare input
image, blob, height, width = preprocess_image("image01.jpg")
net.setInput(blob)

# Get YOLO output
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

outs = net.forward(output_layers)

# Parse outputs
boxes, confidences, class_ids = parse_output(outs, width, height)

# Apply NMS
indexes = apply_nms(boxes, confidences)

# Draw labels
image = draw_labels(image, boxes, confidences, class_ids, indexes, classes)

# Show output
plt.figure(figsize=(12, 8))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
