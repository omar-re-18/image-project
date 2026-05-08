import numpy as np


# ==========================================
# 1. Split RGB Channels
# ==========================================

def split_rgb_channels(img):
    """
    Splits image into Red, Green, Blue channels
    """

    if len(img.shape) != 3:
        raise ValueError("Input must be RGB image")

    r = img[:, :, 2]
    g = img[:, :, 1]
    b = img[:, :, 0]

    return r, g, b


# ==========================================
# 2. Merge RGB Channels
# ==========================================

def merge_rgb_channels(r, g, b):
    """
    Combine separate channels into one RGB image
    """

    h, w = r.shape

    result = np.zeros((h, w, 3), dtype=np.uint8)

    result[:, :, 2] = r
    result[:, :, 1] = g
    result[:, :, 0] = b

    return result


# ==========================================
# 3. Isolate Red Channel
# ==========================================

def red_channel(img):
    """
    Keep only Red channel
    """

    r, g, b = split_rgb_channels(img)

    return merge_rgb_channels(r, np.zeros_like(g), np.zeros_like(b))


# ==========================================
# 4. Isolate Green Channel
# ==========================================

def green_channel(img):
    """
    Keep only Green channel
    """

    r, g, b = split_rgb_channels(img)

    return merge_rgb_channels(np.zeros_like(r), g, np.zeros_like(b))


# ==========================================
# 5. Isolate Blue Channel
# ==========================================

def blue_channel(img):
    """
    Keep only Blue channel
    """

    r, g, b = split_rgb_channels(img)

    return merge_rgb_channels(np.zeros_like(r), np.zeros_like(g), b)


# ==========================================
# 6. Grayscale via Channel Averaging
# ==========================================

def rgb_to_gray_average(img):
    """
    Simple grayscale using average of RGB channels
    """

    h, w, _ = img.shape

    gray = np.zeros((h, w), dtype=np.uint8)

    for i in range(h):
        for j in range(w):

            r, g, b = img[i, j]

            gray[i, j] = int((r + g + b) / 3)

    return gray


# ==========================================
# 7. Channel Visualization Grid
# ==========================================

def channel_grid(img):
    """
    Returns combined visualization:
    Top row: R | G
    Bottom row: B | Gray
    """

    r, g, b = split_rgb_channels(img)
    gray = rgb_to_gray_average(img)

    top = np.hstack((r, g))
    bottom = np.hstack((b, gray))

    return np.vstack((top, bottom))