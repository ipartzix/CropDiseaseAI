# CropDiseaseAI

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-ee4c2c?logo=pytorch">
  <img src="https://img.shields.io/badge/TorchVision-Computer%20Vision-orange?logo=pytorch">
  <img src="https://img.shields.io/badge/OpenCV-Image%20Processing-green?logo=opencv">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-F7931E?logo=scikitlearn">
</p>

---

# Project Overview

**CropDiseaseAI** is a deep-learning-based crop disease detection system designed to identify diseases from crop leaf images.

The system accepts a leaf image either from an existing image file or through a webcam. The image is then passed through an image preprocessing pipeline before being analyzed by a trained **EfficientNet-B0** image classification model.

The model classifies the image into one of the supported crop disease categories and returns the predicted class along with a confidence score.

The project focuses specifically on **computer vision and deep learning for crop disease classification**. The previous IoT hardware and environmental sensor components have been removed from the current version of the project.

### Current Pipeline

```text
Leaf Image
    │
    ▼
Image Input
    │
    ├── Existing Image
    │
    └── Webcam Capture
    │
    ▼
Image Preprocessing
    │
    ▼
EfficientNet-B0
    │
    ▼
Disease Classification
    │
    ▼
Prediction + Confidence
    │
    ▼
Result Display
```

---

# Objectives

* Detect crop diseases from leaf images
* Classify crop diseases using deep learning
* Provide prediction confidence
* Build a modular image-classification pipeline
* Support both existing image files and webcam input
* Develop a practical AI-based crop health analysis system
* Apply computer vision and deep learning techniques to agricultural problems

---

# Key Features

## AI-Based Disease Detection

* Deep-learning-based image classification
* EfficientNet-B0 architecture
* Multiple crop and disease classes
* Healthy and diseased crop classification
* Prediction confidence score

## Image Input

The system supports two image-input methods:

### Existing Image

Users can select an image already stored on their computer.

```text
File Explorer
      │
      ▼
Select Leaf Image
      │
      ▼
Image Path
```

### Webcam

Users can capture a new crop-leaf image using a webcam.

```text
Webcam
   │
   ▼
Live Preview
   │
   ▼
Capture Image
   │
   ▼
Save Image
   │
   ▼
Prediction
```

## Image Processing

* Image loading
* Resizing
* Tensor conversion
* Normalization
* Training-time data augmentation
* Model-ready preprocessing

## Prediction

The system provides:

* Predicted crop/disease class
* Confidence score
* Classification result

---

# Tech Stack

## Programming Language

* Python 3.11

## Deep Learning

* PyTorch
* TorchVision
* EfficientNet-B0
* Convolutional Neural Networks

## Computer Vision

* OpenCV
* Pillow

## Machine Learning Utilities

* NumPy
* Pandas
* Scikit-Learn
* Matplotlib
* Seaborn

## Application

* Python-based local application
* Modular inference pipeline

---

# AI Model

## EfficientNet-B0

The project uses **EfficientNet-B0** as the primary image classification model.

EfficientNet-B0 provides a good balance between:

* Model size
* Computational cost
* Classification performance
* Inference efficiency

The model is trained to classify crop leaf images into the supported disease categories.

### Input

```text
RGB Leaf Image
```

The image is transformed into a normalized PyTorch tensor suitable for the model.

### Model Input Shape

```text
(3, 224, 224)
```

### Output

```text
Predicted Class
+
Confidence Score
```

---

# Dataset Information

The deep-learning model is trained using a custom crop disease image dataset created by combining and cleaning images from publicly available datasets.

## Original Data Sources

### PlantVillage Dataset

Dataset repository:

https://github.com/spMohanty/PlantVillage-Dataset

### 15 Crop and 45 Disease and Healthy Dataset

Mendeley Data:

https://data.mendeley.com/datasets/8fr7grr73p/1

---

# Final Dataset

The final dataset contains five crop categories.

| Crop         | Classes |     Images |
| ------------ | ------: | ---------: |
| Corn (Maize) |       6 |      6,617 |
| Potato       |       3 |      2,988 |
| Rice         |       3 |      3,637 |
| Tomato       |       4 |      6,627 |
| Wheat        |       3 |      2,820 |
| **Total**    |  **19** | **22,689** |

### Dataset Summary

* **Total Crops:** 5
* **Total Classes:** 19
* **Total Images:** 22,689
* **Image Format:** JPG / JPEG
* **Dataset Size:** ~1.36 GB

---

# Dataset Split

A stratified dataset split is used to preserve class distribution across the different subsets.

| Dataset    | Percentage |
| ---------- | ---------: |
| Training   |        70% |
| Validation |        15% |
| Testing    |        15% |

The split is performed while maintaining the distribution of the different classes.

---

# Image Preprocessing

The training pipeline applies image transformations dynamically using **PyTorch TorchVision**.

The training transformation pipeline includes:

* Image resizing/cropping
* Random horizontal flipping
* Random rotation
* Tensor conversion
* Image normalization

The resulting image is converted into a normalized `float32` PyTorch tensor with the required model input dimensions.

### Training Pipeline

```text
Raw JPG/JPEG RGB Image
          │
          ▼
Random Crop / Resize
          │
          ▼
Random Horizontal Flip
          │
          ▼
Random Rotation
          │
          ▼
To Tensor
          │
          ▼
Normalization
          │
          ▼
Tensor (3, 224, 224)
          │
          ▼
EfficientNet-B0
```

Validation and testing use deterministic preprocessing without training-time random augmentation.

---

# System Architecture

```text
                         User
                           │
                           ▼
                    Image Input Layer
                           │
              ┌────────────┴────────────┐
              │                         │
              ▼                         ▼
       Existing Image              Webcam
              │                         │
              └────────────┬────────────┘
                           │
                           ▼
                    Image Path
                           │
                           ▼
                  Image Preprocessing
                           │
                           ▼
                  PyTorch Tensor
                    (3, 224, 224)
                           │
                           ▼
                    EfficientNet-B0
                           │
                           ▼
                  Class Probabilities
                           │
                           ▼
                Post-processing
                           │
                           ▼
             Prediction + Confidence
                           │
                           ▼
                    Result Display
```

---

# Project Workflow

```text
Start
  │
  ▼
Choose Input Method
  │
  ├───────────────┐
  │               │
  ▼               ▼
Select Image    Open Webcam
  │               │
  │               ▼
  │          Capture Image
  │               │
  └───────┬───────┘
          │
          ▼
      Image Path
          │
          ▼
 Image Preprocessing
          │
          ▼
   EfficientNet-B0
          │
          ▼
  Disease Prediction
          │
          ▼
 Confidence Score
          │
          ▼
   Display Result
          │
          ▼
         End
```

---

# Project Structure

```text
CropDiseaseAI/
│
├── datasets/
│   └── image_dataset/
│       └── README.md
│
├── notebooks/
│   ├── 01_image_data_EDA.ipynb
│   └── 02_image_model_training.ipynb
│
├── src/
│   ├── main.py
│   ├── config.py
│   ├── file_picker.py
│   ├── camera.py
│   ├── preprocess.py
│   ├── predictor.py
│   └── postprocess.py
│
├── models/
│   └── cnn/
│       ├── efficientnet_b0_best.pth
│       └── class_names.json
│
├── docs/
│   ├── architecture.png
│   ├── workflow.png
│   ├── dataset_description.md
│   ├── classification_report.txt
│   ├── confusion_matrix.png
│   ├── draw.tldr
│   └── screenshots/
│
├── images/
│   └── captured_image.jpg
│
├── tests/
│   └── test_cnn.py
│
├── environment.yml
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

# Module Responsibilities

The application follows a modular pipeline where each component has a specific responsibility.

## `config.py`

Stores project configuration values such as:

* Model path
* Class names path
* Image size
* Device
* Normalization values
* Prediction settings

It does not perform the prediction itself.

---

## `file_picker.py`

Allows the user to select an existing image from the computer.

```text
File Explorer
      │
      ▼
Select Image
      │
      ▼
Return Image Path
```

The module only handles image selection.

---

## `camera.py`

Handles webcam-based image capture.

```text
Webcam
   │
   ▼
Live Preview
   │
   ▼
Capture
   │
   ├── Save
   ├── Retake
   └── Cancel
```

The module returns the path of the captured image.

---

## `preprocess.py`

Responsible for preparing the selected image for the model.

```text
Image
  │
  ▼
Resize
  │
  ▼
Tensor Conversion
  │
  ▼
Normalization
  │
  ▼
Model Input
```

---

## `predictor.py`

Responsible for:

* Loading the trained model
* Running inference
* Generating class probabilities
* Obtaining the predicted class

---

## `postprocess.py`

Responsible for converting the raw model output into a user-readable result.

```text
Model Output
     │
     ▼
Predicted Class
     │
     ▼
Confidence
     │
     ▼
Readable Result
```

---

## `main.py`

Acts as the main application pipeline.

```text
Input
  ↓
Image Selection / Camera
  ↓
Preprocessing
  ↓
Prediction
  ↓
Post-processing
  ↓
Result
```

The modular design allows both file-based and webcam-based inputs to use the same downstream prediction pipeline.

---

# Getting Started

## Prerequisites

Install one of the following:

* **Miniconda** — Recommended
* **Anaconda**

Miniconda is recommended because it provides a lightweight Conda installation without unnecessary packages.

---

# Clone the Repository

```bash
git clone https://github.com/ipartzix/CropDiseaseAI.git
cd CropDiseaseAI
```

---

# Create the Conda Environment

The project provides an `environment.yml` file containing the required dependencies.

```bash
conda env create -f environment.yml
```

The environment installs the required packages, including:

* Python
* PyTorch
* TorchVision
* NumPy
* Pillow
* OpenCV
* Other project dependencies

---

# Activate the Environment

```bash
conda activate CropDisease_AI
```

---

# Run the Application

From the project root directory:

```bash
python -m src.main
```

The application will start the image classification workflow.

You can then provide an image through the supported input method.

---

# Deactivate the Environment

After finishing:

```bash
conda deactivate
```

---

# Model Files

The trained model is stored under:

```text
models/
└── cnn/
    ├── efficientnet_b0_best.pth
    └── class_names.json
```

### `efficientnet_b0_best.pth`

Contains the trained EfficientNet-B0 model weights.

### `class_names.json`

Contains the class-name mapping required to convert model output indices into disease labels.

---

# Model Inference

The inference pipeline follows:

```text
Input Image
     │
     ▼
Load Image
     │
     ▼
Preprocess
     │
     ▼
Convert to Tensor
     │
     ▼
Load EfficientNet-B0
     │
     ▼
Run Inference
     │
     ▼
Softmax Probabilities
     │
     ▼
Select Predicted Class
     │
     ▼
Calculate Confidence
     │
     ▼
Display Result
```

---

The project is now focused on:

> **Deep-learning-based crop disease detection from leaf images.**

---

# Future Improvements

Potential future improvements include:

* Mobile application
* Cloud deployment
* REST API
* Real-time camera inference
* Model optimization
* ONNX deployment
* Edge-device deployment
* Additional crop classes
* Additional disease classes
* Explainable AI using Grad-CAM
* Multilingual prediction results
* Disease treatment recommendations
* Model performance monitoring

---

# Expected Outcomes

The system is designed to provide:

* Automated crop disease classification
* Fast image-based prediction
* Prediction confidence
* A modular deep-learning pipeline
* Practical computer-vision application for agriculture

---

# References

### PlantVillage Dataset

https://github.com/spMohanty/PlantVillage-Dataset

### 15 Crop and 45 Disease and Healthy Dataset

https://data.mendeley.com/datasets/8fr7grr73p/1

---

# Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

---

# License

This project is developed for **academic and research purposes**.

The datasets used in this project belong to their respective owners and are used according to their respective terms and licenses.

---

# Contributors

<div align="center">

<table>
<tr>
<td align="center" width="50%">

### Biswajit Sarkar

<a href="https://github.com/biswajit-sarkar-007">
<img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub">
</a>

<a href="https://www.linkedin.com/in/biswajit007">
<img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn">
</a>

<br><br>

Developed the **Web Application** and designed the responsive **User Interface (UI)**.

Implemented the frontend using modern web development practices.

Integrated the frontend with the backend and deep-learning prediction pipeline.

Ensured seamless interaction between the user interface and the image classification system.

</td>

<td align="center" width="50%">

### Partha Paul

<a href="https://github.com/ipartzix">
<img src="https://img.shields.io/badge/GitHub-Profile-black?style=for-the-badge&logo=github" alt="GitHub">
</a>

<a href="https://www.linkedin.com/in/ipartzix">
<img src="https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin" alt="LinkedIn">
</a>

<br><br>

Designed and developed the **Deep Learning** module.

Built and trained the **EfficientNet-B0** model for crop disease image classification.

Performed image preprocessing, data augmentation, model training, validation, and performance evaluation.

Integrated the trained model into the application for inference and prediction.

Designed and implemented the **main source pipeline**, connecting image input, preprocessing, model inference, and result generation.

</td>
</tr>
</table>

</div>


* Designed and developed the **Deep Learning** module.
* Built and trained an **EfficientNet-B0** model for crop disease image classification.
* Performed image preprocessing and data augmentation.
* Conducted model training, validation, and performance evaluation.
* Integrated the trained model into the application for inference and prediction.
* Designed and implemented the **main source pipeline**, connecting image input, preprocessing, model inference, and result generation.

   </td>
  </tr>

</table>

---

# Project Status

**Current Focus:** Deep Learning-based crop disease image classification

**Model:** EfficientNet-B0

**Framework:** PyTorch

**Input:** Crop leaf image

**Output:** Crop disease class + prediction confidence

**IoT Hardware:** Removed from the current project scope
