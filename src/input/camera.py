# src/input/camera.py


# ==============================================================================
# Standard Library Imports
# ==============================================================================

from pathlib import Path

# ==============================================================================
# Third-Party Library Imports
# ==============================================================================

import cv2

# ==============================================================================
# Local Application Imports
# ==============================================================================

from src.config import IMAGE_DIR

# ==============================================================================
# Capture Image from Camera
# ==============================================================================

def capture_image() -> Path | None:
    """
    Capture an image using the default webcam.

    Controls
    --------
    C : Capture image
    S : Save image
    R : Retake image
    Q : Quit without saving

    Returns
    -------
    Path | None
        Path to the saved image, otherwise None.
    """

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    image_path = IMAGE_DIR / "captured_image.jpg"

    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        raise RuntimeError("Unable to access the camera.")

    print("\nCamera Started")
    print("Press 'C' to capture.")
    print("Press 'Q' to quit.\n")

    try:

        while True:

            success, frame = camera.read()

            if not success:
                raise RuntimeError("Failed to read frame from the camera.")

            cv2.imshow("Camera", frame)

            key = cv2.waitKey(1) & 0xFF

            # ---------------- Capture ----------------

            if key == ord("c"):

                captured_frame = frame.copy()

                while True:

                    cv2.imshow("Captured Image", captured_frame)

                    print("Press 'S' to save | 'R' to retake | 'Q' to cancel")

                    preview_key = cv2.waitKey(0) & 0xFF

                    # Save
                    if preview_key == ord("s"):

                        cv2.imwrite(str(image_path), captured_frame)

                        print(f"\nImage saved successfully:")
                        print(image_path)

                        cv2.destroyWindow("Captured Image")

                        return image_path

                    # Retake
                    elif preview_key == ord("r"):

                        cv2.destroyWindow("Captured Image")

                        print("\nRetake the image...")

                        break

                    # Cancel
                    elif preview_key == ord("q"):

                        cv2.destroyWindow("Captured Image")

                        return None

            # ---------------- Quit ----------------

            elif key == ord("q"):

                return None

    finally:

        camera.release()
        cv2.destroyAllWindows()


# ==============================================================================
# Test Run
# ==============================================================================

if __name__ == "__main__":

    image = capture_image()

    if image is not None:
        print(f"\nCaptured Image : {image}")
    else:
        print("\nNo image captured.")