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


# ==========================================
# Channel-wise Negative (Optional Advanced)
# ==========================================

def negative_rgb(img):
    """
    Apply negative separately on RGB channels
    """

    if len(img.shape) != 3:
        raise ValueError("Input must be RGB image")

    result = np.zeros_like(img)

    h, w, c = img.shape

    for i in range(h):
        for j in range(w):
            for k in range(c):
                result[i, j, k] = 255 - img[i, j, k]

    return result