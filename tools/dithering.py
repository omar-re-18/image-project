import numpy as np


# ==========================================
# Unified Dithering Interface
# ==========================================

def dither_image(img, method='floyd_steinberg'):
    """
    Apply dithering to grayscale image

    Parameters:
    - img: grayscale image (2D array)
    - method: 'floyd_steinberg' (quality) or 'ordered' (speed)

    Returns:
    - dithered binary image
    """

    if len(img.shape) == 3:
        raise ValueError("Input must be grayscale image")

    if method == 'floyd_steinberg':
        return floyd_steinberg_dithering(img)
    elif method == 'ordered':
        return ordered_dithering(img)
    else:
        raise ValueError(f"Unknown dithering method: {method}")


# ==========================================
# Floyd–Steinberg Dithering (High Quality)
# ==========================================

def floyd_steinberg_dithering(img):
    """
    Converts grayscale image to black & white
    while preserving visual details using error diffusion

    Optimized version with:
    - Fixed loop bounds (starts from j=0)
    - Pre-computed error weights
    - Efficient boundary checks
    - NumPy optimizations
    """

    # Ensure grayscale
    if len(img.shape) == 3:
        raise ValueError("Input must be grayscale image")

    # Work on float32 copy for precision
    img = img.astype(np.float32).copy()
    h, w = img.shape

    # Pre-compute error diffusion weights
    weights = np.array([
        [0, 0, 7/16],      # current row: right neighbor
        [3/16, 5/16, 1/16] # next row: left, center, right
    ], dtype=np.float32)

    # Process pixels (skip last row and column for boundary safety)
    for i in range(h - 1):
        for j in range(w - 1):
            old_pixel = img[i, j]
            new_pixel = 255.0 if old_pixel > 127.5 else 0.0
            img[i, j] = new_pixel

            error = old_pixel - new_pixel

            # Apply error diffusion to neighbors using pre-computed weights
            # Current row: right pixel
            if j + 1 < w:
                img[i, j + 1] += error * weights[0, 2]

            # Next row: left, center, right pixels
            if i + 1 < h:
                if j - 1 >= 0:
                    img[i + 1, j - 1] += error * weights[1, 0]
                img[i + 1, j] += error * weights[1, 1]
                if j + 1 < w:
                    img[i + 1, j + 1] += error * weights[1, 2]

    # Handle last column separately (no right neighbors)
    for i in range(h - 1):
        j = w - 1
        old_pixel = img[i, j]
        new_pixel = 255.0 if old_pixel > 127.5 else 0.0
        img[i, j] = new_pixel

        error = old_pixel - new_pixel

        # Only diffuse to next row (no right neighbor)
        if i + 1 < h:
            if j - 1 >= 0:
                img[i + 1, j - 1] += error * weights[1, 0]
            img[i + 1, j] += error * weights[1, 1]

    # Handle last row separately (no bottom neighbors)
    for j in range(w):
        i = h - 1
        old_pixel = img[i, j]
        new_pixel = 255.0 if old_pixel > 127.5 else 0.0
        img[i, j] = new_pixel

        # No error diffusion for last row

    return np.clip(img, 0, 255).astype(np.uint8)


# ==========================================
# Ordered Dithering (Fast Alternative)
# ==========================================

def ordered_dithering(img, matrix_size=4):
    """
    Fast ordered dithering using Bayer matrix
    Much faster than Floyd-Steinberg but different visual quality
    """

    if len(img.shape) == 3:
        raise ValueError("Input must be grayscale image")

    h, w = img.shape

    # Bayer matrix for 4x4 ordered dithering
    if matrix_size == 4:
        bayer = np.array([
            [0, 8, 2, 10],
            [12, 4, 14, 6],
            [3, 11, 1, 9],
            [15, 7, 13, 5]
        ], dtype=np.float32) / 16.0
    else:
        # Simple 2x2 for smaller matrices
        bayer = np.array([
            [0, 2],
            [3, 1]
        ], dtype=np.float32) / 4.0

    # Tile the Bayer matrix to cover the image
    tiled_h = (h + matrix_size - 1) // matrix_size
    tiled_w = (w + matrix_size - 1) // matrix_size

    bayer_tiled = np.tile(bayer, (tiled_h, tiled_w))[:h, :w]

    # Apply dithering
    threshold = (bayer_tiled * 255).astype(np.uint8)
    result = np.where(img > threshold, 255, 0).astype(np.uint8)

    return result


# ==========================================
# Simple Threshold Dithering (Vectorized)
# ==========================================

def simple_dither(img, threshold=127):
    """
    Basic black & white conversion (vectorized)
    """

    result = np.where(img > threshold, 255, 0).astype(np.uint8)

    return result