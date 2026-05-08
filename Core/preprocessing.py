import numpy as np

# ==========================================
# 1. Convert to Grayscale (Manual fallback)
# ==========================================

def to_grayscale(img):
    """
    Convert RGB image to grayscale using luminance formula
    """

    if len(img.shape) == 2:
        return img  # already grayscale

    h, w, _ = img.shape
    gray = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            r, g, b = img[i, j]

            gray[i, j] = int(0.299*r + 0.587*g + 0.114*b)

    return gray


# ==========================================
# 2. Resize Image (Manual nearest neighbor)
# ==========================================

def resize(img, new_h, new_w):
    """
    Resize image using nearest neighbor interpolation
    """

    h, w = img.shape[:2]

    result = np.zeros((new_h, new_w), dtype=img.dtype)

    for i in range(new_h):
        for j in range(new_w):

            src_i = int(i * h / new_h)
            src_j = int(j * w / new_w)

            result[i, j] = img[src_i, src_j]

    return result


# ==========================================
# 3. Normalize Image
# ==========================================

def normalize(img):
    """
    Scale pixel values to 0–255 range
    """

    min_val = np.min(img)
    max_val = np.max(img)

    if max_val == min_val:
        return img.copy()

    result = (img - min_val) * 255 / (max_val - min_val)

    return result.astype(np.uint8)


# ==========================================
# 4. Noise Reduction (Box Filter)
# ==========================================

def remove_noise(img, kernel_size=3):
    """
    Simple averaging filter to reduce noise
    """

    pad = kernel_size // 2

    padded = np.pad(img, pad, mode='edge')

    h, w = img.shape
    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):

            region = padded[i:i+kernel_size, j:j+kernel_size]

            result[i, j] = np.mean(region)

    return result.astype(np.uint8)


# ==========================================
# 5. Invert Intensity Range (Pre-step enhancement)
# ==========================================

def invert(img):
    """
    Invert image intensity
    """

    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = 255 - img[i, j]

    return result


# ==========================================
# 6. Crop Center (Useful for document detection)
# ==========================================

def center_crop(img, crop_ratio=0.8):
    """
    Crop center region of image
    """

    h, w = img.shape[:2]

    new_h = int(h * crop_ratio)
    new_w = int(w * crop_ratio)

    start_i = (h - new_h) // 2
    start_j = (w - new_w) // 2

    return img[start_i:start_i+new_h, start_j:start_j+new_w]