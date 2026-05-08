import numpy as np


# ==========================================
# 1. Horizontal Flip (Mirror)
# ==========================================

def flip_horizontal(img):
    """
    Flip image horizontally (left ↔ right)
    """

    h, w = img.shape[:2]
    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):
            result[i, j] = img[i, w - j - 1]

    return result


# ==========================================
# 2. Vertical Flip
# ==========================================

def flip_vertical(img):
    """
    Flip image vertically (top ↔ bottom)
    """

    h, w = img.shape[:2]
    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):
            result[i, j] = img[h - i - 1, j]

    return result


# ==========================================
# 3. Rotate 90 degrees clockwise
# ==========================================

def rotate_90(img):
    """
    Rotate image 90 degrees clockwise
    """

    h, w = img.shape[:2]

    result = np.zeros((w, h), dtype=img.dtype)

    for i in range(h):
        for j in range(w):
            result[j, h - i - 1] = img[i, j]

    return result


# ==========================================
# 4. Rotate 180 degrees
# ==========================================

def rotate_180(img):
    """
    Rotate image 180 degrees
    """

    h, w = img.shape[:2]
    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):
            result[i, j] = img[h - i - 1, w - j - 1]

    return result


# ==========================================
# 5. Resize (Nearest Neighbor)
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
# 6. Translate (Shift Image)
# ==========================================

def translate(img, shift_x=0, shift_y=0):
    """
    Move image in x/y direction
    """

    h, w = img.shape[:2]

    result = np.zeros_like(img)

    for i in range(h):
        for j in range(w):

            new_i = i + shift_y
            new_j = j + shift_x

            if 0 <= new_i < h and 0 <= new_j < w:
                result[new_i, new_j] = img[i, j]

    return result


# ==========================================
# 7. Crop Image
# ==========================================

def crop(img, x1, y1, x2, y2):
    """
    Crop region from image
    """

    return img[y1:y2, x1:x2]


# ==========================================
# 8. Scale Image
# ==========================================

def scale(img, scale_factor):
    """
    Resize using scale factor
    """

    h, w = img.shape[:2]

    new_h = int(h * scale_factor)
    new_w = int(w * scale_factor)

    return resize(img, new_h, new_w)