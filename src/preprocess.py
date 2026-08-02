# ==============================================================================
# Third-Party Imports
# ==============================================================================

from PIL import Image
from torchvision import transforms


# ==============================================================================
# Local Imports
# ==============================================================================

from src.config import (
    IMAGE_SIZE,
    MEAN,
    STD,
    DEVICE
)


# ==============================================================================
# Image Transform
# ==============================================================================

transform = transforms.Compose([
    transforms.Resize(IMAGE_SIZE),
    transforms.ToTensor(),
    transforms.Normalize(
        mean=MEAN,
        std=STD
    )
])


# ==============================================================================
# Preprocess Image
# ==============================================================================

def preprocess_image(image_path):
    """
    Prepare image for EfficientNet inference.

    Parameters
    ----------
    image_path : Path
        Input image path

    Returns
    -------
    torch.Tensor
        Tensor shape:
        (1, 3, IMAGE_SIZE, IMAGE_SIZE)
    """

    try:
        image = Image.open(image_path).convert("RGB")

    except Exception as e:
        raise RuntimeError(
            f"Failed to load image {image_path}: {e}"
        )

    image_tensor = transform(image)

    # Add batch dimension
    image_tensor = image_tensor.unsqueeze(0)

    # Move tensor to CPU/GPU
    image_tensor = image_tensor.to(DEVICE)

    return image_tensor