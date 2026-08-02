# src/postprocess.py


# ==============================================================================
# Third-Party Library Imports
# ==============================================================================

import torch


# ==============================================================================
# Process Prediction Results
# ==============================================================================

def process_predictions(outputs, class_names, top_k=5):
    """
    Convert model logits into prediction results.

    Parameters
    ----------
    outputs : torch.Tensor
        Raw model output logits.

    class_names : list
        Disease class labels.

    top_k : int
        Number of highest probability predictions.

    Returns
    -------
    dict
        Prediction result with confidence and top-k predictions.
    """

    # Convert logits to probabilities
    probabilities = torch.softmax(
        outputs,
        dim=1
    )[0]


    # Avoid requesting more classes than available
    top_k = min(
        top_k,
        len(class_names)
    )


    # Get top predictions
    top_probabilities, top_indices = torch.topk(
        probabilities,
        top_k
    )


    predictions = []


    for probability, index in zip(
        top_probabilities,
        top_indices
    ):

        predictions.append(
            {
                "class": class_names[index.item()],
                "confidence": round(
                    probability.item() * 100,
                    2
                )
            }
        )


    return {
        "prediction": predictions[0]["class"],
        "confidence": predictions[0]["confidence"],
        "top_predictions": predictions
    }