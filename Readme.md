# 🌱 IoT Based Crop Disease Detection System for Smart Agriculture

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask">
  <img src="https://img.shields.io/badge/TensorFlow-Deep%20Learning-orange?logo=tensorflow">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn">
  <img src="https://img.shields.io/badge/Arduino-IoT-00979D?logo=arduino">
  <img src="https://img.shields.io/badge/OpenCV-Image%20Processing-green?logo=opencv">
</p>

---

#  Project Overview

The **IoT Based Crop Disease Detection System for Smart Agriculture** is an AI-powered smart farming solution that integrates **Internet of Things (IoT), Machine Learning, and Deep Learning** to monitor crop health and detect plant diseases at an early stage.

The system continuously collects real-time environmental data using IoT sensors connected to an **Arduino Uno**, including:

- 🌡 Temperature
- 💧 Humidity
- 🌱 Soil Moisture

This sensor data is analyzed using **Machine Learning models** such as:

- Random Forest
- XGBoost
- LightGBM

to evaluate crop health and predict disease risk based on environmental conditions.

At the same time, a **USB Camera/Webcam** captures images of crop leaves. These images are processed using a **Convolutional Neural Network (CNN)** trained on the **PlantVillage Dataset** to identify crop diseases and classify plants as **Healthy** or **Diseased** along with a prediction confidence score.

By combining **environmental sensor analysis** with **image-based disease detection**, the system provides farmers with accurate crop monitoring, early disease diagnosis, and intelligent recommendations for precision agriculture.

---

#  Objectives

- Detect crop diseases at an early stage
- Monitor environmental conditions in real time
- Improve farming decisions using Artificial Intelligence
- Reduce crop losses
- Increase agricultural productivity
- Promote precision farming

---

#  Key Features

 Real-time Sensor Monitoring

- Temperature Monitoring
- Humidity Monitoring
- Soil Moisture Monitoring

 AI-Based Disease Detection

- CNN-based leaf image classification
- Disease identification
- Confidence score prediction

 Machine Learning Prediction

- Environmental stress analysis
- Disease risk prediction
- Crop health assessment

 Smart Dashboard

- Live sensor values
- Uploaded leaf image
- Disease prediction
- Risk probability
- Health status
- Farming recommendation

---

# 🛠 Tech Stack

## Programming Languages

- Python
- C/C++ (Arduino)

## Machine Learning

- Scikit-Learn
- Random Forest
- XGBoost
- LightGBM

## Deep Learning

- TensorFlow
- Keras
- CNN (Convolutional Neural Network)

## IoT

- Arduino Uno
- Soil Moisture Sensor
- DHT11 / DHT22 Sensor
- USB Webcam

## Backend

- Flask / FastAPI

## Frontend

- HTML
- CSS
- JavaScript
- Bootstrap

## Libraries

- OpenCV
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-Learn
- TensorFlow
- Joblib

---

#  AI Models Used

## Machine Learning Model

Used for analyzing environmental sensor data.

Algorithms:

- Random Forest
- XGBoost
- LightGBM

### Input

- Temperature
- Humidity
- Soil Moisture

### Output

- Crop Health
- Disease Risk
- Risk Probability

---

## Deep Learning Model

CNN-based model trained on crop leaf images.

### Input

Leaf Image

### Output

- Disease Name
- Healthy/Diseased
- Confidence Score
---
# Dataset Information

This project utilizes two publicly available datasets to train the Machine Learning and Deep Learning models.

---

## 1. Crop Health & Environmental Stress Dataset

This dataset is used to train the **Machine Learning** model for crop health prediction based on environmental conditions.

### Features

- Temperature
- Humidity
- Soil Moisture
- Crop Health Label (Healthy / Unhealthy)

### Dataset Statistics

- **Total Records:** 212,019
- **Task:** Binary Classification (Healthy / Unhealthy)

### Source

**Dataset Name:** Crop Health & Environmental Stress Dataset

https://www.kaggle.com/datasets/datasetengineer/crop-health-and-environmental-stress-dataset

---

## 2. Custom Crop Disease Image Dataset

This dataset is used to train the **Deep Learning (CNN)** model for crop disease classification.

The final dataset was created by combining and cleaning images collected from multiple publicly available datasets.

### Original Data Sources

#### • PlantVillage Dataset

Dataset Link:

https://github.com/spMohanty/PlantVillage-Dataset

#### • 15 Crop and 45 Disease and Healthy Dataset (Mendeley Data)

Dataset Link:

https://data.mendeley.com/datasets/8fr7grr73p/1

---

### Final Dataset Statistics

| Crop | Classes | Images |
|------|---------:|-------:|
| Corn (Maize) | 6 | 6,617 |
| Potato | 3 | 2,988 |
| Rice | 3 | 3,637 |
| Tomato | 4 | 6,627 |
| Wheat | 3 | 2,820 |

### Overall Summary

- **Total Crops:** 5
- **Total Classes:** 19
- **Total Images:** 22,689
- **Image Format:** JPG / JPEG
- **Dataset Size:** ~1.36 GB

### Train / Validation / Test Split

A **stratified split** is used to maintain the class distribution across all categories.

- **Training Set:** 70%
- **Validation Set:** 15%
- **Testing Set:** 15%

### Image Preprocessing

During model training, images are processed dynamically using **PyTorch Torchvision** transforms.

- Automatic image resizing
- Image normalization
- Data augmentation (training set only)
- Original images remain unchanged
#  System Architecture

```
                     User (Farmer)
                           │
                           ▼
                    Web Application
                           │
        ┌──────────────────┴──────────────────┐
        │                                     │
        ▼                                     ▼
 USB Camera/Webcam                      Arduino Uno
 (Leaf Image)                           │
                                        │
                 ┌──────────────────────┴────────────────────┐
                 │                                            │
          DHT11/DHT22 Sensor                      Soil Moisture Sensor
       (Temperature & Humidity)
                 │
                 ▼
          Flask / FastAPI Backend
                 │
      ┌──────────┴──────────┐
      │                     │
      ▼                     ▼
Image Preprocessing   Sensor Preprocessing
      │                     │
      ▼                     ▼
 CNN Model          Random Forest/XGBoost
      │                     │
      └──────────┬──────────┘
                 ▼
        Disease Prediction 
                 &
        Smart Recommendation
                 │
                 ▼
         Results Dashboard
```

---

#  Project Workflow

```text
Start
   │
   ▼
Collect Sensor Data
   │
   ▼
Capture Leaf Image
   │
   ▼
Data Preprocessing
   │
   ├──────────────┐
   │              │
   ▼              ▼
Machine       CNN Model
Learning
   │              │
   └──────┬───────┘
          ▼
Combine Predictions
          │
          ▼
Disease Detection
          │
          ▼
Generate Recommendation
          │
          ▼
Display Results
```

---

#  Project Structure

```
IoT_Based_Crop_Disease_Detection_System/
│
├── datasets/
│   ├── image_dataset/
│   │   └── README.md    # Hugging Face dataset link
│   │
│   └── sensor_dataset/
│       ├── sensor_data.csv
│       └── README.md
│
├── notebooks/
│   ├── 01_sensor_data_EDA.ipynb
│   ├── 02_sensor_data_preprocessing.ipynb
│   ├── 03_sensor_model_training.ipynb
│   ├── 04_image_data_EDA.ipynb
│   └── 05_image_model_training.ipynb
│
├── src/
│   ├── image_classification/
│   │   ├── model.py
│   │   ├── evaluate.py
│   │   └── predict.py
│   │
│   ├── sensor_prediction/
│   │   ├── preprocess.py
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── predict.py
│   │
│   └── docs/
│       ├── screenshots/
│       │   ├── image_data_screenshots
│       │   └── sensor_data_screenshots
|       |
│       ├──classification_report.txt
│       ├── confusion_matrix.png
│       ├── draw.tldr # use tldr extension to see the diagram in vscode 
│       └── architecture_diagram.png  # under process of being created
|
├── models/
│   ├── cnn/
│   │   ├── mobilenetv3_best.pth
│   │   └── class_names.json
│   │
│   └── ml/
│       ├── random_forest.pkl
│       ├── xgboost.pkl
│       ├── lightgbm.pkl
│       └── best_model.pkl
│
├── web_app/
│   ├── app.py
│   ├── routes.py
│   ├── templates/
│   │   ├── index.html
│   │   └── result.html
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   ├── images/
│   │   └── uploads/
│   │
│   └── requirements.txt
│
├── arduino/
│   ├── crop_disease_detection.ino
│   └── sensors.md
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   ├── dataset_description.md
│   └── screenshots/
│
├── tests/
│   ├── test_cnn.py
│   ├── test_ml.py
│   └── test_api.py
│
├── requirements.txt
├── README.md
├── LICENSE
├── .gitignore
└── .env.example
```

---

#  Future Improvements

- Mobile Application
- Cloud Deployment
- SMS Alert System
- Fertilizer Recommendation
- Pest Detection
- Weather Forecast Integration
- Multi-language Support
- GPS-based Farm Monitoring

---

#  Expected Outcomes

- Early Disease Detection
- Improved Crop Yield
- Reduced Farming Costs
- Smart Decision Support
- Sustainable Agriculture
- Precision Farming

---

#  Sample Output

- Sensor Readings
- Leaf Image
- Disease Name
- Confidence Score
- Disease Risk
- Health Status
- Recommendation

---

#  References

### Sensor Dataset

https://www.kaggle.com/datasets/datasetengineer/crop-health-and-environmental-stress-dataset

### PlantVillage Dataset

https://github.com/spMohanty/PlantVillage-Dataset

---

 

#  Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

It motivates us to continue developing AI-powered solutions for smart agriculture.

---

##  License

This project is developed for **academic and research purposes**.

The datasets used in this project belong to their respective owners and are used only for educational and research purposes.