import albumentations as A
import cv2
import os
import numpy as np


# Define augmentation pipeline
transform = A.Compose([
    A.HorizontalFlip(p=0.5),  # Flip 50% of the images
    A.RandomBrightnessContrast(p=0.2),  # Adjust brightness/contrast
    A.Rotate(limit=20, p=0.5),  # Rotate within ±20 degrees
    A.GaussNoise(p=0.3),  # Add noise
    A.Blur(blur_limit=3, p=0.2)  # Apply blur
], bbox_params=A.BboxParams(format="yolo", label_fields=["category_ids"]))

# Paths
image_dir = "dataset/images"
label_dir = "dataset/labels"
augmented_image_dir = "dataset/images_aug"
augmented_label_dir = "dataset/labels_aug"

os.makedirs(augmented_image_dir, exist_ok=True)
os.makedirs(augmented_label_dir, exist_ok=True)

# List all images
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]

# Augment each image
for image_file in image_files:
    # Load image
    img_path = os.path.join(image_dir, image_file)
    img = cv2.imread(img_path)

    # Load corresponding label file
    label_path = os.path.join(label_dir, image_file.replace(".jpg", ".txt"))
    with open(label_path, "r") as f:
        lines = f.readlines()

    # Convert YOLO bbox format (class x_center y_center width height) to Albumentations format
    bboxes = []
    category_ids = []
    
    height, width, _ = img.shape
    for line in lines:
        cls, x, y, w, h = map(float, line.strip().split())
        bboxes.append([x, y, w, h])  # YOLO format
        category_ids.append(int(cls))  # Class ID

    # Apply augmentation
    augmented = transform(image=img, bboxes=bboxes, category_ids=category_ids)

    # Save augmented image
    aug_img_path = os.path.join(augmented_image_dir, f"aug_{image_file}")
    cv2.imwrite(aug_img_path, augmented["image"])

    # Save new annotation
    aug_label_path = os.path.join(augmented_label_dir, f"aug_{image_file.replace('.jpg', '.txt')}")
    with open(aug_label_path, "w") as f:
        for bbox, cls in zip(augmented["bboxes"], augmented["category_ids"]):
            x, y, w, h = bbox
            f.write(f"{cls} {x} {y} {w} {h}\n")

print("Augmentation completed successfully!")