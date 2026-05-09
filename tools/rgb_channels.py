import numpy as np


# ==========================================
# Channel Visualization Grid
# ==========================================

def channel_grid(img):
    """
    Returns combined visualization:
    Top row: R | G
    Bottom row: B | Gray
    """

    if len(img.shape) != 3:
        raise ValueError("Input must be RGB image")

    r = img[:, :, 2]
    g = img[:, :, 1]
    b = img[:, :, 0]

    # Simple grayscale using average
    gray = np.mean(img, axis=2).astype(np.uint8)

    top = np.hstack((r, g))
    bottom = np.hstack((b, gray))

    return np.vstack((top, bottom))