import os
import cv2
import numpy as np


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


# ==========================================
# 2. Save Image
# ==========================================

def save_image(path, img):
    """
    Save image to disk safely
    """

    directory = os.path.dirname(path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    success = cv2.imwrite(path, img)

    if not success:
        raise IOError("Failed to save image")


# ==========================================
# 3. Read as Grayscale
# ==========================================

def load_grayscale(path):
    """
    Load image directly as grayscale
    """

    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    if img is None:
        raise ValueError("Failed to load grayscale image")

    return img


# ==========================================
# 4. Convert and Save (Pipeline Utility)
# ==========================================

def process_and_save(input_path, output_path, process_fn):
    """
    Load image → apply function → save result
    """

    img = load_image(input_path)

    processed = process_fn(img)

    save_image(output_path, processed)

    return processed


# ==========================================
# 5. Validate Image Format
# ==========================================

def is_valid_image(path):
    """
    Check if file is a valid image type
    """

    valid_ext = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")

    return path.lower().endswith(valid_ext)


# ==========================================
# 6. Get Image Info
# ==========================================

def get_image_info(img):
    """
    Return basic metadata about image
    """

    return {
        "shape": img.shape,
        "dtype": str(img.dtype),
        "min_pixel": int(np.min(img)),
        "max_pixel": int(np.max(img))
    }