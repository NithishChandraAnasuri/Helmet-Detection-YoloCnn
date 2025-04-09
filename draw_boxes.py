# draw_boxes.py
import cv2

# Set the Y-coordinate for the virtual stop line (adjust as per your image)
STOP_LINE_Y = 300

def draw_labels(image, boxes, confidences, class_ids, indexes, classes):
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]

            # Default color is green
            color = (0, 255, 0)

            # If the object is a car and its bottom crosses the stop line, change color to red
            if label == "car" and (y + h) > STOP_LINE_Y:
                color = (0, 0, 255)

            # Draw bounding box and label
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
            cv2.putText(image, f"{label} {round(confidence, 2)}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Draw the stop line (optional: for visualization)
    cv2.line(image, (0, STOP_LINE_Y), (image.shape[1], STOP_LINE_Y), (255, 255, 0), 2)

    return image
