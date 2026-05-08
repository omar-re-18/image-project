import numpy as np


# ==========================================
# 1. Addition (Brightness Increase)
# ==========================================

def add(img, value):
    """
    Increase pixel intensity
    """

    result = img.astype(np.int16)

    h, w = img.shape[:2]

    for i in range(h):
        for j in range(w):
            result[i, j] += value

    return np.clip(result, 0, 255).astype(np.uint8)


# ==========================================
# 2. Subtraction (Brightness Decrease)
# ==========================================

def subtract(img, value):
    """
    Decrease pixel intensity
    """

    result = img.astype(np.int16)

    h, w = img.shape[:2]

    for i in range(h):
        for j in range(w):
            result[i, j] -= value

    return np.clip(result, 0, 255).astype(np.uint8)


# ==========================================
# 3. Multiplication (Contrast Boost)
# ==========================================

def multiply(img, alpha):
    """
    Scale intensity (contrast-like effect)
    """

    result = img.astype(np.float32)

    h, w = img.shape[:2]

    for i in range(h):
        for j in range(w):
            result[i, j] *= alpha

    return np.clip(result, 0, 255).astype(np.uint8)


# ==========================================
# 4. Division (Intensity Reduction)
# ==========================================

def divide(img, alpha):
    """
    Reduce intensity values
    """

    result = img.astype(np.float32)

    h, w = img.shape[:2]

    for i in range(h):
        for j in range(w):
            result[i, j] /= alpha

    return np.clip(result, 0, 255).astype(np.uint8)