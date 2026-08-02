#src/input/file_picker.py

# ==============================================================================
# Standard Library Imports
# ==============================================================================

from pathlib import Path
from tkinter import Tk, filedialog


# ==============================================================================
# File Picker Function
# ==============================================================================

def select_image():
    """
    Opens file explorer and allows user to select an image.

    Returns:
        Path: Selected image path
        None: If no file selected
    """

    # Hide tkinter main window
    root = Tk()
    root.withdraw()

    # Open file explorer
    file_path = filedialog.askopenfilename(
        title="Select Crop Image",
        filetypes=[
            ("Image Files", "*.jpg *.jpeg *.png"),
            ("All Files", "*.*")
        ]
    )

    # Close tkinter window
    root.destroy()

    if file_path:
        return Path(file_path)

    return None


# ==============================================================================
# Testing
# ==============================================================================

if __name__ == "__main__":

    image_path = select_image()

    if image_path:
        print(f"Selected Image: {image_path}")
    else:
        print("No image selected")