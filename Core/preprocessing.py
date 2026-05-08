import numpy as np

# ==========================================
# 1. Convert to Grayscale (Vectorized)
# ==========================================

def to_grayscale(img):
    """
    Convert RGB image to grayscale using luminance formula (vectorized)
    """

    if len(img.shape) == 2:
        return img  # already grayscale

    # Vectorized: much faster than nested loops
    gray = (0.299 * img[:,:,2] + 0.587 * img[:,:,1] + 0.114 * img[:,:,0]).astype(np.uint8)
    
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
# 4. Noise Reduction (Vectorized)
# ==========================================

def remove_noise(img, kernel_size=3):
    """
    Simple averaging filter to reduce noise (vectorized with scipy)
    """
    from scipy.ndimage import uniform_filter

    # Use scipy's optimized uniform filter instead of nested loops
    result = uniform_filter(img.astype(np.float32), size=kernel_size)
    
    return np.clip(result, 0, 255).astype(np.uint8)


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