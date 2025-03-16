from ultralytics import YOLO
import cv2

# Load the trained YOLO model
model = YOLO("dataset_aug/runs/detect/train2/weights/best.pt")

# Load an image
image_path = "./brownspot_orig_040.jpg"
image = cv2.imread(image_path)

# Perform inference
results = model(image)

# Show results
for r in results:
    r.show()  # Display the image with detections
