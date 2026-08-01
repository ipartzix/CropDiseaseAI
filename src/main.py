# ==============================================================================
# IoT Based Crop Disease Detection System
# EfficientNet-B0 Crop Disease Prediction
# src/main.py
# ==============================================================================


# ==============================================================================
# Imports
# ==============================================================================


# ==============================================================================
# Standard Library Imports
# ==============================================================================

import json
from pathlib import Path


# ==============================================================================
# Third-Party Library Imports
# ==============================================================================

import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image


# ==============================================================================
# Project Paths
# ==============================================================================

MODEL_PATH = Path(r"C:\IOT_Based_Crop_Disease_Detection_System_For_Smart_Agriculture\models\cnn\efficientnet_b0_best.pth")
CLASS_JSON = Path(r"C:\IOT_Based_Crop_Disease_Detection_System_For_Smart_Agriculture\models\cnn\class_names.json")
IMAGE_PATH = Path(r"C:\IOT_Based_Crop_Disease_Detection_System_For_Smart_Agriculture\images")


# ==============================================================================
# Model Configuration
# ==============================================================================

MODEL_NAME = "EfficientNet-B0"
IMAGE_SIZE = (224, 224)


# ==============================================================================
# Device Configuration
# ==============================================================================

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


# ==============================================================================
# Load Class Names
# ==============================================================================

with open(CLASS_JSON, "r") as f:
    class_names = json.load(f)

NUM_CLASSES = len(class_names)


# ==============================================================================
# Load Model
# ==============================================================================

model = models.efficientnet_b0(weights=None)

model.classifier = nn.Sequential(
    nn.Dropout(0.2),
    nn.Linear(model.classifier[1].in_features, NUM_CLASSES)
)

model.load_state_dict(torch.load(MODEL_PATH, map_location=DEVICE))
model.to(DEVICE)
model.eval()


# ==============================================================================
# Image Preprocessing
# ==============================================================================

transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=[0.485, 0.456, 0.406],
        std=[0.229, 0.224, 0.225]
    ),
])


# ==============================================================================
# Load Image
# ==============================================================================

image = Image.open(IMAGE_PATH).convert("RGB")
input_tensor = transform(image).unsqueeze(0).to(DEVICE)


# ==============================================================================
# Model Prediction
# ==============================================================================

with torch.no_grad():
    outputs = model(input_tensor)
    probabilities = torch.softmax(outputs, dim=1)[0]

top5_prob, top5_idx = torch.topk(probabilities, 5)


# ==============================================================================
# Display Top-5 Predictions
# ==============================================================================

print("\nTop 5 Predictions:\n")

for prob, idx in zip(top5_prob, top5_idx):
    print(f"{class_names[idx.item()]:40} {prob.item()*100:.2f}%")


# ==============================================================================
# Best Prediction
# ==============================================================================

predicted_class = class_names[top5_idx[0].item()]
confidence = top5_prob[0].item() * 100


# ==============================================================================
# Display Result
# ==============================================================================

print("=" * 45)
print(f"Image      : {IMAGE_PATH.name}")
print(f"Prediction : {predicted_class}")
print(f"Confidence : {confidence:.2f}%")
print("=" * 45)