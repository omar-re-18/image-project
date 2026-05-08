import os
import numpy as np
import cv2


# ==========================================
# 1. Check if file is a valid image
# ==========================================

def is_image_file(path):
    """
    Validate image file extension
    """

    valid_ext = (".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff")

    return path.lower().endswith(valid_ext)


# ==========================================
# 2. Load Image Safely
# ==========================================

def load_image(path):
    """
    Safe image loading using OpenCV
    """

    if not os.path.exists(path):
        raise FileNotFoundError("Image path does not exist")

    img = cv2.imread(path)

    if img is None:
        raise ValueError("Failed to load image")

    return img


# ==========================================
# 3. Save Image
# ==========================================

def save_image(path, img):
    """
    Save image to disk safely
    """

    directory = os.path.dirname(path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    cv2.imwrite(path, img)


# ==========================================
# 4. Convert to Grayscale (Fallback)
# ==========================================

def to_grayscale(img):
    """
    Convert RGB/BGR to grayscale manually
    """

    if len(img.shape) == 2:
        return img

    h, w, _ = img.shape
    gray = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            b, g, r = img[i, j]

            gray[i, j] = int(0.114 * b + 0.587 * g + 0.299 * r)

    return gray


# ==========================================
# 5. Clip Image Values
# ==========================================

def clip(img):
    """
    Ensure pixel values are in valid range [0, 255]
    """

    return np.clip(img, 0, 255).astype(np.uint8)


# ==========================================
# 6. Image Info (for debugging)
# ==========================================

def image_info(img):
    """
    Return basic image metadata
    """

    return {
        "shape": img.shape,
        "dtype": str(img.dtype),
        "min": int(np.min(img)),
        "max": int(np.max(img))
    }