import os
import shutil
import random

# Paths
image_dir = "dataset aug/images"
label_dir = "dataset aug/labels"
train_img_dir = "dataset aug/images/train"
val_img_dir = "dataset aug/images/val"
train_label_dir = "dataset aug/labels/train"
val_label_dir = "dataset aug/labels/val"

# Create train/val directories
for d in [train_img_dir, val_img_dir, train_label_dir, val_label_dir]:
    os.makedirs(d, exist_ok=True)

# Get all images
image_files = [f for f in os.listdir(image_dir) if f.endswith(".jpg")]
random.shuffle(image_files)

# Split dataset
split_idx = int(0.8 * len(image_files))
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

# Move files to train/val folders
for file in train_files:
    shutil.move(os.path.join(image_dir, file), os.path.join(train_img_dir, file))
    shutil.move(os.path.join(label_dir, file.replace(".jpg", ".txt")), os.path.join(train_label_dir, file.replace(".jpg", ".txt")))

for file in val_files:
    shutil.move(os.path.join(image_dir, file), os.path.join(val_img_dir, file))
    shutil.move(os.path.join(label_dir, file.replace(".jpg", ".txt")), os.path.join(val_label_dir, file.replace(".jpg", ".txt")))

print("Dataset split into train & validation successfully!")
