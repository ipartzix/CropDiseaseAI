# src/model_loader.py

# ==============================================================================
# Standard Library Imports
# ==============================================================================

import json


# ==============================================================================
# Third-Party Library Imports
# ==============================================================================

import torch
import torch.nn as nn
from torchvision import models


# ==============================================================================
# Local Application Imports
# ==============================================================================

from src.config import (
    MODEL_PATH,
    CLASS_NAMES_PATH,
    DEVICE,
)


# ==============================================================================
# Load Class Names
# ==============================================================================

def load_class_names():
    """
    Load class names from JSON file.

    Returns
    -------
    list
        List of disease class names.
    """

    with open(CLASS_NAMES_PATH, "r") as file:
        class_names = json.load(file)

    return class_names


# ==============================================================================
# Build EfficientNet-B0 Model
# ==============================================================================

def build_model(num_classes):
    """
    Create EfficientNet-B0 architecture.

    Parameters
    ----------
    num_classes : int
        Number of output classes.

    Returns
    -------
    torch.nn.Module
        EfficientNet-B0 model.
    """

    model = models.efficientnet_b0(
        weights=None
    )

    # Replace classifier layer
    model.classifier = nn.Sequential(
        nn.Dropout(p=0.2),
        nn.Linear(
            model.classifier[1].in_features,
            num_classes
        )
    )

    return model


# ==============================================================================
# Load Trained Model
# ==============================================================================

def load_model():

    if not MODEL_PATH.exists():
        raise FileNotFoundError(
            "Model file not found"
        )

    if not CLASS_NAMES_PATH.exists():
        raise FileNotFoundError(
            "Class names file not found"
        )

    class_names = load_class_names()

    model = build_model(
        len(class_names)
    )

    checkpoint = torch.load(
        MODEL_PATH,
        map_location=DEVICE
    )

    model.load_state_dict(
        checkpoint
    )

    model.to(DEVICE)
    model.eval()

    return model, class_names