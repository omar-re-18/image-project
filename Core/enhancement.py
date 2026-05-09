import numpy as np

# ==========================================
# Contrast Stretching (Vectorized)
# ==========================================

def contrast_stretch(img):
    """
    Expands intensity range from min-max → 0-255 (vectorized)
    """

    min_val = np.min(img)
    max_val = np.max(img)

    # Handle uniform image (all same values)
    if min_val == max_val:
        return np.full_like(img, 128, dtype=np.uint8)

    # Vectorized operation: much faster
    result = ((img.astype(np.float32) - min_val) * 255 / (max_val - min_val)).astype(np.uint8)

    return result