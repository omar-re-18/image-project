import numpy as np

# ==========================================
# 1. RGB → Grayscale (Manual)
# ==========================================

def to_grayscale(img):
    h, w, c = img.shape
    gray = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):
            r, g, b = img[i, j]

            # luminance formula
            gray[i, j] = int(0.299 * r + 0.587 * g + 0.114 * b)

    return gray


# ==========================================
# 2. Brightness Adjustment
# ==========================================

def adjust_brightness(img, value):
    result = img.astype(np.int16)

    h, w = result.shape[:2]

    for i in range(h):
        for j in range(w):
            result[i, j] += value

    return np.clip(result, 0, 255).astype(np.uint8)


# ==========================================
# 3. Contrast Stretching
# ==========================================

def contrast_stretch(img):
    min_val = np.min(img)
    max_val = np.max(img)

    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = ((img[i, j] - min_val) * 255) // (max_val - min_val + 1)

    return result


# ==========================================
# 4. Box Blur (from scratch)
# ==========================================

def box_blur(img, kernel_size=3):
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
# 5. Thresholding (Manual)
# ==========================================

def threshold(img, t=127):
    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            if img[i, j] > t:
                result[i, j] = 255
            else:
                result[i, j] = 0

    return result


# ==========================================
# 6. Negative Image
# ==========================================

def negative(img):
    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = 255 - img[i, j]

    return result


# ==========================================
# 7. Solarization
# ==========================================

def solarize(img, t=128):
    result = img.copy()

    h, w = img.shape

    for i in range(h):
        for j in range(w):

            if result[i, j] > t:
                result[i, j] = 255 - result[i, j]

    return result


# ==========================================
# 8. Addition
# ==========================================

def add(img, value):
    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = min(255, img[i, j] + value)

    return result


# ==========================================
# 9. Subtraction
# ==========================================

def subtract(img, value):
    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = max(0, img[i, j] - value)

    return result


# ==========================================
# 10. Multiplication
# ==========================================

def multiply(img, alpha):
    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = min(255, int(img[i, j] * alpha))

    return result


# ==========================================
# 11. Division
# ==========================================

def divide(img, alpha):
    h, w = img.shape
    result = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            result[i, j] = min(255, int(img[i, j] / alpha))

    return result


# ==========================================
# 12. Erosion (Manual Morphology)
# ==========================================

def erosion(img, kernel=3):
    pad = kernel // 2

    padded = np.pad(img, pad, mode='constant', constant_values=255)

    h, w = img.shape
    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):

            region = padded[i:i+kernel, j:j+kernel]
            result[i, j] = np.min(region)

    return result


# ==========================================
# 13. Dilation
# ==========================================

def dilation(img, kernel=3):
    pad = kernel // 2

    padded = np.pad(img, pad, mode='constant', constant_values=0)

    h, w = img.shape
    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):

            region = padded[i:i+kernel, j:j+kernel]
            result[i, j] = np.max(region)

    return result


# ==========================================
# 14. Opening / Closing
# ==========================================

def opening(img):
    return dilation(erosion(img))


def closing(img):
    return erosion(dilation(img))