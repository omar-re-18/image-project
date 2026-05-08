import numpy as np


# ==========================================
# Floyd–Steinberg Dithering (Manual)
# ==========================================

def floyd_steinberg_dithering(img):
    """
    Converts grayscale image to black & white
    while preserving visual details using error diffusion
    """

    # Ensure grayscale
    if len(img.shape) == 3:
        raise ValueError("Input must be grayscale image")

    img = img.astype(np.float32)

    h, w = img.shape

    for i in range(h - 1):
        for j in range(1, w - 1):

            old_pixel = img[i, j]

            # threshold
            new_pixel = 255 if old_pixel > 127 else 0

            img[i, j] = new_pixel

            error = old_pixel - new_pixel

            # distribute error to neighbors
            img[i, j + 1] += error * 7 / 16
            img[i + 1, j - 1] += error * 3 / 16
            img[i + 1, j] += error * 5 / 16
            img[i + 1, j + 1] += error * 1 / 16

    return np.clip(img, 0, 255).astype(np.uint8)


# ==========================================
# Simple Threshold Dithering (Optional)
# ==========================================

def simple_dither(img, threshold=127):
    """
    Basic black & white conversion
    (less advanced than Floyd–Steinberg)
    """

    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = 255 if img[i, j] > threshold else 0

    return result