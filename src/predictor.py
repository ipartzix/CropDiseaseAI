# src/predictor.py

# ==============================================================================
# Third-Party Library Imports
# ==============================================================================

import torch


# ==============================================================================
# Local Application Imports
# ==============================================================================

from src.config import DEVICE


# ==============================================================================
# Model Prediction
# ==============================================================================

def predict(model, image_tensor):
    """
    Run model inference.

    Parameters
    ----------
    model : torch.nn.Module
        Loaded EfficientNet model.

    image_tensor : torch.Tensor
        Preprocessed image tensor.

    Returns
    -------
    torch.Tensor
        Raw model outputs (logits).
    """

    # Move image to CPU/GPU
    image_tensor = image_tensor.to(DEVICE)

    # Disable gradient calculation
    with torch.no_grad():

        outputs = model(
            image_tensor
        )

    return outputs