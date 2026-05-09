import numpy as np
from scipy import ndimage

# ==========================================
# Helper: Padding
# ==========================================

def pad_image(img, pad_size, pad_value):
    return np.pad(
        img,
        pad_size,
        mode='constant',
        constant_values=pad_value
    )


# ==========================================
# 1. Erosion (Optimized with scipy)
# ==========================================

def erosion(img, kernel_size=3):
    """
    Removes small white noise (optimized)
    """

    # Create binary structuring element
    struct = ndimage.generate_binary_structure(2, 1)
    struct = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    
    # Use scipy's optimized binary_erosion
    result = ndimage.binary_erosion(img > 127, structure=struct).astype(np.uint8) * 255

    return result


# ==========================================
# 2. Dilation (Optimized with scipy)
# ==========================================

def dilation(img, kernel_size=3):
    """
    Expands white regions (optimized)
    """

    # Create binary structuring element
    struct = np.ones((kernel_size, kernel_size), dtype=np.uint8)
    
    # Use scipy's optimized binary_dilation
    result = ndimage.binary_dilation(img > 127, structure=struct).astype(np.uint8) * 255

    return result


# ==========================================
# 3. Opening (Erosion → Dilation)
# ==========================================

def opening(img, kernel_size=3):
    """
    Removes noise (small objects)
    """

    eroded = erosion(img, kernel_size)
    opened = dilation(eroded, kernel_size)

    return opened


# ==========================================
# 4. Closing (Dilation → Erosion)
# ==========================================

def closing(img, kernel_size=3):
    """
    Fills small holes
    """

    dilated = dilation(img, kernel_size)
    closed = erosion(dilated, kernel_size)

    return closed


# ==========================================
# 5. Morphological Gradient
# ==========================================

def morphological_gradient(img, kernel_size=3):
    """
    Highlights edges (Dilation - Erosion)
    """

    dilated = dilation(img, kernel_size)
    eroded = erosion(img, kernel_size)

    result = dilated.astype(np.int16) - eroded.astype(np.int16)

    return np.clip(result, 0, 255).astype(np.uint8)
