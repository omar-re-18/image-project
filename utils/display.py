import cv2
import numpy as np


# ==========================================
# Prepare Image for GUI
# ==========================================

def prepare_image(img, size=(400, 400)):
    """
    Full pipeline for GUI display:
    resize → normalize → format
    """

    # Prevent overflow/invalid pixel ranges
    img = img.astype(np.float32)
    min_val = np.min(img)
    max_val = np.max(img)

    if max_val == min_val:
        img = np.zeros_like(img, dtype=np.uint8)
    else:
        img = (img - min_val) * 255 / (max_val - min_val)
        img = img.astype(np.uint8)

    img = cv2.resize(img, size)

    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    return img