import os

labels_path = "D:/Projects/P2PClouds/Dataset/rice_dataset/dataset_aug/labels/val"

for file in os.listdir(labels_path):
    if file.endswith(".txt"):
        with open(os.path.join(labels_path, file), "r") as f:
            lines = f.readlines()
            for line in lines:
                class_id = line.split()[0]
                if class_id != "0":
                    print(f"❌ Incorrect class ID in {file}: {class_id}")
                else:
                    print(f"✅ Correct class ID in {file}")