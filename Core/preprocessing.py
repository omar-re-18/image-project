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

    # Convert to float32 to avoid overflow during calculation
    img_float = img.astype(np.float32)
    result = (img_float - min_val) * 255 / (max_val - min_val)

    return np.clip(result, 0, 255).astype(np.uint8)


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


