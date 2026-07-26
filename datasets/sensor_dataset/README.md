# Environment Health Sensor Dataset

<p align="center">
  <img src="https://img.shields.io/badge/Dataset-212,019%2B%20Records-green">
  <img src="https://img.shields.io/badge/Task-Binary%20Classification-blue">
  <img src="https://img.shields.io/badge/Domain-Smart%20Agriculture-orange">
</p>

## Overview

The **Environment Health Sensor Dataset** is a processed agricultural sensor dataset created for the **IoT Based Crop Disease Detection System for Smart Agriculture** project.

This dataset is designed for machine learning models that analyze environmental conditions and predict crop health status. It contains approximately **212,019 sensor records** collected from crop environmental parameters.

The dataset includes three input features:

- Temperature
- Humidity
- Soil Moisture

and one target classification label:

- Environment_Health_Label

The objective of this dataset is to enable smart farming applications by using machine learning techniques for automatic crop health monitoring.

---

## Dataset Link

The processed dataset is publicly available on Hugging Face:

```
[ADD HUGGING FACE DATASET LINK HERE]
```

---

## Original Dataset Source

Original Dataset:
```
https://www.kaggle.com/datasets/datasetengineer/crop-health-and-environmental-stress-dataset
```

The original dataset was processed and prepared for integration into an IoT-based crop monitoring and prediction system.

---

## Dataset Details

| Feature | Description |
|---------|-------------|
| Temperature | Environmental temperature measurement |
| Humidity | Atmospheric humidity measurement |
| Soil_Moisture | Soil water content measurement |
| Environment_Health_Label | Environment health classification output |

Dataset Information:

- Total Samples: 212,019
- Data Format: CSV
- Input Features: 3
- Target Feature: 1
- Machine Learning Task: Binary Classification

---

## Target Label Information

Target Column:

```
Crop_Health_Label
```

Label Mapping:

```
0 → Unhealthy Environment

1 → Healthy Environment
```

---

## Machine Learning Usage

The dataset can be used for supervised machine learning classification tasks.

Input:

```text
Temperature
Humidity
Soil_Moisture
```

Output:

```text
Environment_Health_Label
```

The model learns the relationship between environmental conditions and crop health to predict whether a crop is healthy or under stress.

---

## Recommended Machine Learning Algorithms

This dataset can be used with:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost
- LightGBM
- Support Vector Machine
- Neural Networks

---

## Project Integration

This dataset is a part of the:

# IoT Based Crop Disease Detection System for Smart Agriculture

The complete system contains two AI modules:

### 1. Image-Based Crop Disease Detection

Input:
- Crop leaf images

Model:
- CNN / Deep Learning

Output:
- Disease classification

### 2. Sensor-Based Crop Health Prediction

Input:
- Temperature
- Humidity
- Soil Moisture

Model:
- Machine Learning Classification

Output:

```
Healthy Environment
or
Unhealthy Environment
```

---

## Data Processing Pipeline

```
Sensor Data
      |
      ↓
Data Cleaning
      |
      ↓
Feature Selection
      |
      ↓
Feature Scaling
      |
      ↓
Machine Learning Model
      |
      ↓
Environment Health Prediction
```

---

## Dataset Format Example

```csv
Temperature,Humidity,Soil_Moisture,Crop_Health_Label
28.5,65.2,42.1,1
34.1,40.5,20.3,0
```

---

## Future Improvements

Future versions may include:

- Real-time IoT sensor data collection
- ESP32/Raspberry Pi integration
- Time-series environmental monitoring
- Weather API integration
- Additional agricultural parameters
- Multi-class crop health prediction

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Machine Learning
- IoT Sensor Data Processing

---

## License

This dataset is intended for educational, research, and smart agriculture development purposes.

Original dataset credit belongs to the Kaggle dataset creator.

---

## Project

**IoT Based Crop Disease Detection System for Smart Agriculture**

AI Components:

- Computer Vision Model → Crop Disease Detection
- Machine Learning Model → Sensor-Based Crop Health Prediction