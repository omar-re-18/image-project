import numpy as np


# ==========================================
# Negative Image Transformation
# ==========================================

def negative(img):
    """
    Inverts image colors:
    white ↔ black, light ↔ dark
    """

    # Ensure valid input
    if img is None:
        raise ValueError("Image input is None")

    result = 255 - img

    return result.astype(np.uint8)