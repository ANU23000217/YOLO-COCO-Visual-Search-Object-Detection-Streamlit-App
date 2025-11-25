# YOLO-COCO-Visual-Search-Object-Detection-Streamlit-App

### Introduction:
This project implements a real-time visual search and object detection system using a YOLO model pretrained on the COCO dataset.
Users can upload an image through a simple Streamlit web UI, and the model detects objects, displays bounding boxes, class labels, and confidence scores.
The aim is to enable fast, accurate object recognition in an easy-to-use interface—achieving visual search functionality suitable for academic, commercial, and real-world applications.

## Dataset & YOLO Model Details (COCO)
### Dataset:

* COCO 2017 Dataset
* Contains n number of everyday object classes
* Examples: person, car, dog, bicycle, cup, laptop, bottle, chair, bus, etc.

### YOLO Model Used

* Model Variant: YOLOv8n

### Output:

* Bounding boxes
* Object class name
* Confidence score

 ## Environment Setup (Conda)
### Create Conda Environment
### CPU Users:
```
conda create -n yolo_image_search python=3.11 -y
conda activate yolo_image_search
```
### GPU Users (NVIDIA CUDA Supported System)
```
conda create -n yolo_image_search_gpu python=3.11 -y
conda activate yolo_image_search_gpu
```

## How to Run in VS Code using Conda
### Step 1: Open VS Code → Terminal
### Step 2: Activate Environment
conda activate yolo_image_search_gpu

### Step 3: Run Streamlit App
streamlit run app.py

### Step 4: Open the App

Click the terminal URL:

http://localhost:8501

## Output Screenshots:
<img width="1907" height="568" alt="Screenshot 2025-11-25 101839" src="https://github.com/user-attachments/assets/7cbc0c38-e312-4456-95df-702ae97ae0c4" />


<img width="1831" height="376" alt="Screenshot 2025-11-25 101927" src="https://github.com/user-attachments/assets/88ede127-f48e-4682-95e3-8fccd7057fa7" />


<img width="1920" height="908" alt="Screenshot 2025-11-25 102036" src="https://github.com/user-attachments/assets/3b28f6e7-6e81-4cd9-8739-21ff0a5fc79d" />


### Result: 

The YOLO COCO Streamlit application successfully performs object detection with high accuracy and speed on a user-friendly interface.
The system provides intuitive visual search, clear labeling, and smooth interaction.
This project demonstrates how COCO-trained YOLO models can be integrated with Streamlit for practical and real-world computer vision applications.
