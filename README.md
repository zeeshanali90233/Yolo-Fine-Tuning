# YOLO Fine-Tuning 🚀

## Overview
This repository contains scripts and datasets used for fine-tuning YOLO on a **Leaf Dataset** annotated using **CVAT**. The fine-tuning process has demonstrated superior performance compared to traditional XML-to-YOLO annotation conversion scripts.

## Features
✅ **Fine-tuning YOLO on Leaf Dataset** 🍃  
✅ **CVAT Annotations** (outperforms XML-to-YOLO conversion) 🏆  
✅ **Prediction Script** for testing trained models 🎯  
✅ **Dataset Split Script** to organize training, validation, and test sets 📂  
✅ **Pre-trained YOLO Model Utilization** for better accuracy 🤖  

## Repository Structure
```
Yolo-Fine-Tuning/
│-- dataset/               # Contains leaf dataset
│-- annotations/           # CVAT annotations
│-- scripts/
│   ├── xml_to_yolo.py     # Convert XML annotations to YOLO format
│   ├── split_dataset.py   # Script to split dataset into train, val, and test
│   ├── predict.py         # YOLO model inference script
│-- models/                # Pre-trained and fine-tuned YOLO models
│-- README.md              # This documentation
```

## Installation
Ensure you have the required dependencies installed before running the scripts.

```sh
pip install ultralytics opencv-python numpy torch torchvision
```

## Training YOLO Model 🏋️‍♂️
To fine-tune YOLO on the Leaf dataset:

```sh
yolo train model=yolov8n.pt data=dataset.yaml epochs=50 imgsz=640
```

## Converting XML Annotations to YOLO 📌
Use the script below to convert CVAT XML annotations to YOLO format.

```sh
python scripts/xml_to_yolo.py --input annotations/ --output dataset/
```

## Splitting the Dataset 📂
Run the dataset split script to create training, validation, and test sets.

```sh
python scripts/split_dataset.py --input dataset/ --train 0.7 --val 0.2 --test 0.1
```

## Running Inference 🧐
To make predictions using the fine-tuned YOLO model:

```sh
python scripts/predict.py --weights models/yolo_finetuned.pt --source test_images/
```

## Results 📈
The fine-tuned YOLO model consistently **outperforms** standard XML-to-YOLO conversion pipelines when trained on the Leaf Dataset annotated with CVAT. The model achieves **higher accuracy and recall**, making it a superior choice for leaf disease detection.

## Sample Prediction 🖼️
![YOLO Prediction](images/sample_prediction.png)

## Contributing 🤝
Feel free to contribute by submitting **issues** or **pull requests**!

## License 📜
This project is open-source and available under the **MIT License**.

---
🚀 **Fine-tune YOLO like a pro and achieve state-of-the-art results!**
