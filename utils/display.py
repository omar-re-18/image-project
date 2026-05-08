import cv2
import numpy as np


# ==========================================
# 1. Resize for Display
# ==========================================

def resize_for_display(img, size=(400, 400)):
    """
    Resize image for GUI display only
    (does NOT affect processing pipeline)
    """

    return cv2.resize(img, size)


# ==========================================
# 2. Convert to Displayable Format
# ==========================================

def to_display_format(img):
    """
    Ensures image is in RGB format for GUI
    """

    if img is None:
        return None

    if len(img.shape) == 2:
        return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

    # OpenCV uses BGR → convert to RGB
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# ==========================================
# 3. Normalize for Safe Display
# ==========================================

def safe_normalize(img):
    """
    Prevent overflow/invalid pixel ranges
    """

    img = img.astype(np.float32)

    min_val = np.min(img)
    max_val = np.max(img)

    if max_val == min_val:
        return np.zeros_like(img, dtype=np.uint8)

    result = (img - min_val) * 255 / (max_val - min_val)

    return result.astype(np.uint8)


# ==========================================
# 4. Prepare Image for GUI
# ==========================================

def prepare_image(img, size=(400, 400)):
    """
    Full pipeline for GUI display:
    resize → normalize → format
    """

    img = safe_normalize(img)
    img = resize_for_display(img, size)
    img = to_display_format(img)

    return img


# ==========================================
# 5. Compare Two Images Side-by-Side
# ==========================================

def side_by_side(img1, img2):
    """
    Combine two images for comparison view
    """

    img1 = resize_for_display(img1)
    img2 = resize_for_display(img2)

    if len(img1.shape) == 2:
        img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

    if len(img2.shape) == 2:
        img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)

    return np.hstack((img1, img2))


# ==========================================
# 6. Grid View (for RGB or multiple outputs)
# ==========================================

def grid_view(images):
    """
    Arrange multiple images in a grid
    """

    processed = []

    for img in images:
        img = resize_for_display(img)
        if len(img.shape) == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        processed.append(img)

    row1 = np.hstack(processed[:2])
    row2 = np.hstack(processed[2:4])

    return np.vstack((row1, row2))