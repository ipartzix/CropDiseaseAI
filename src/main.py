# src/main.py


# ==============================================================================
# Local Application Imports
# ==============================================================================

from src.input.file_picker import select_image
from src.input.camera import capture_image

from src.model_loader import load_model
from src.preprocess import preprocess_image
from src.predictor import predict
from src.postprocess import process_predictions


# ==============================================================================
# Main Workflow
# ==============================================================================

def main():

    print("====================================")
    print(" Crop Disease Detection System")
    print("====================================")


    # --------------------------------------------------------------------------
    # Step 1: Select Image Source
    # --------------------------------------------------------------------------

    choice = input(
        "\n1. Upload Image from local machine"
        "\n2. Capture Image using Camera"
        "\nChoose option: "
    )


    if choice == "1":

        image_path = select_image()


    elif choice == "2":

        image_path = capture_image()


    else:

        print("Invalid option")
        return


    if image_path is None:

        print("No image selected.")
        return



    # --------------------------------------------------------------------------
    # Step 2: Load Model
    # --------------------------------------------------------------------------

    print("\nLoading model...")

    model, class_names = load_model()



    # --------------------------------------------------------------------------
    # Step 3: Preprocess Image
    # --------------------------------------------------------------------------

    print("Preprocessing image...")

    image_tensor = preprocess_image(
        image_path
    )



    # --------------------------------------------------------------------------
    # Step 4: Prediction
    # --------------------------------------------------------------------------

    print("Running prediction...")

    outputs = predict(
        model,
        image_tensor
    )



    # --------------------------------------------------------------------------
    # Step 5: Postprocess Result
    # --------------------------------------------------------------------------

    result = process_predictions(
        outputs,
        class_names
    )


    print("\nPrediction Result")
    print("----------------")

    print(
        f"Disease : {result['prediction']}"
    )

    print(
        f"Confidence : {result['confidence']:.2f}%"
    )


    print("\nTop Predictions:")

    for item in result["top_predictions"]:

        print(
            f"{item['class']} : {item['confidence']:.2f}%"
        )



# ==============================================================================
# Entry Point
# ==============================================================================

if __name__ == "__main__":

    main()