# image_preprocessor.py
import cv2

def preprocess_image(image_path):
    image = cv2.imread(image_path)
    height, width = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, 1/255, (416,416), swapRB=True, crop=False)
    return image, blob, height, width
