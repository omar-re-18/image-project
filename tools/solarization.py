import numpy as np


# ==========================================
# Solarization Effect
# ==========================================

def solarize(img, threshold=128):
    """
    Inverts pixel values above a certain threshold
    """

    if img is None:
        raise ValueError("Image input is None")

    result = img.copy()

    h, w = result.shape[:2]

    for i in range(h):
        for j in range(w):

            # grayscale or RGB handling
            if len(result.shape) == 2:
                if result[i, j] > threshold:
                    result[i, j] = 255 - result[i, j]

            else:
                for c in range(3):
                    if result[i, j, c] > threshold:
                        result[i, j, c] = 255 - result[i, j, c]

    return result.astype(np.uint8)


# ==========================================
# Adaptive Solarization (Advanced version)
# ==========================================

def adaptive_solarize(img):
    """
    Automatically chooses threshold based on mean intensity
    """

    if len(img.shape) == 2:
        threshold = np.mean(img)
    else:
        gray = np.mean(img, axis=2)
        threshold = np.mean(gray)

    return solarize(img, threshold=int(threshold))


# ==========================================
# Partial Solarization (Creative Effect)
# ==========================================

def partial_solarize(img, low=100, high=200):
    """
    Only invert pixels in a specific intensity range
    """

    result = img.copy()

    h, w = result.shape[:2]

    for i in range(h):
        for j in range(w):

            if len(result.shape) == 2:

                if low < result[i, j] < high:
                    result[i, j] = 255 - result[i, j]

            else:

                for c in range(3):

                    if low < result[i, j, c] < high:
                        result[i, j, c] = 255 - result[i, j, c]

    return result.astype(np.uint8)