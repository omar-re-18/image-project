import numpy as np

# ==========================================
# 1. Brightness Adjustment (Manual)
# ==========================================

def adjust_brightness(img, value):
    """
    Increase or decrease image brightness
    value: positive → brighter
           negative → darker
    """
    result = img.astype(np.int16)

    h, w = result.shape[:2]

    for i in range(h):
        for j in range(w):
            result[i, j] += value

    return np.clip(result, 0, 255).astype(np.uint8)


# ==========================================
# 2. Contrast Stretching
# ==========================================

def contrast_stretch(img):
    """
    Expands intensity range from min-max → 0-255
    """

    min_val = np.min(img)
    max_val = np.max(img)

    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = ((img[i, j] - min_val) * 255) // (max_val - min_val + 1)

    return result


# ==========================================
# 3. Gamma Correction (Manual)
# ==========================================

def gamma_correction(img, gamma=1.0):
    """
    Non-linear brightness adjustment
    """

    img = img / 255.0

    h, w = img.shape
    result = np.zeros((h, w), dtype=np.float32)

    for i in range(h):
        for j in range(w):

            result[i, j] = img[i, j] ** gamma

    result = (result * 255)

    return np.clip(result, 0, 255).astype(np.uint8)


# ==========================================
# 4. Histogram Equalization (Manual simplified)
# ==========================================

def histogram_equalization(img):
    """
    Improves contrast using histogram distribution
    """

    hist = np.zeros(256)

    h, w = img.shape

    # Step 1: Histogram
    for i in range(h):
        for j in range(w):
            hist[img[i, j]] += 1

    # Step 2: Normalize histogram
    hist = hist / (h * w)

    # Step 3: CDF (Cumulative Distribution Function)
    cdf = np.zeros(256)
    cdf[0] = hist[0]

    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + hist[i]

    # Step 4: Mapping
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = int(cdf[img[i, j]] * 255)

    return result


# ==========================================
# 5. Sharpening Filter (Manual Kernel)
# ==========================================

def sharpen(img):
    """
    Edge enhancement using convolution kernel
    """

    kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    pad = 1
    padded = np.pad(img, pad, mode='edge')

    h, w = img.shape
    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):

            region = padded[i:i+3, j:j+3]

            value = np.sum(region * kernel)

            result[i, j] = np.clip(value, 0, 255)

    return result.astype(np.uint8)


# ==========================================
# 6. Edge Enhancement (Sobel-like Manual)
# ==========================================

def edge_enhancement(img):
    """
    Simple edge detection using difference
    """

    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h - 1):
        for j in range(w - 1):

            gx = int(img[i, j + 1]) - int(img[i, j])
            gy = int(img[i + 1, j]) - int(img[i, j])

            val = abs(gx) + abs(gy)

            result[i, j] = min(255, val)

    return result


# ==========================================
# 7. Normalize Image
# ==========================================

def normalize(img):
    """
    Scale image values to 0–255 range
    """

    min_val = np.min(img)
    max_val = np.max(img)

    result = (img - min_val) * 255 / (max_val - min_val + 1)

    return result.astype(np.uint8)