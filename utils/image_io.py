import os
import cv2


# ==========================================
# 1. Load Image
# ==========================================

def load_image(path):
    """
    Load image from disk safely using OpenCV
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    img = cv2.imread(path)

    if img is None:
        raise ValueError("Failed to load image (invalid format or corrupted file)")

    return img

