import numpy as np

# Import our manual modules
from .preprocessing import to_grayscale, remove_noise, normalize
from .enhancement import contrast_stretch
from .morphology import erosion, dilation, closing


# ==========================================
# Smart Document Scanner Pipeline
# ==========================================

def auto_scan(image):
    """
    Full document scanning pipeline:
    Preprocessing → Enhancement → Threshold → Morphology
    """

    # ======================================
    # Step 1: Grayscale
    # ======================================
    gray = to_grayscale(image)

    # ======================================
    # Step 2: Noise Removal
    # ======================================
    denoised = remove_noise(gray, kernel_size=3)

    # ======================================
    # Step 3: Contrast Enhancement
    # ======================================
    enhanced = contrast_stretch(denoised)

    # Optional improvement (uncomment if needed)
    # enhanced = gamma_correction(enhanced, gamma=1.2)

    # ======================================
    # Step 4: Binarization (Threshold)
    # ======================================
    binary = simple_threshold(enhanced, threshold=127)

    # ======================================
    # Step 5: Morphology Cleaning
    # ======================================
    cleaned = closing(binary, kernel_size=3)

    # ======================================
    # Step 6: Final Normalization
    # ======================================
    result = normalize(cleaned)

    return result


# ==========================================
# Simple Threshold (Vectorized)
# ==========================================

def simple_threshold(img, threshold=127):
    """
    Binarize image using threshold (vectorized)
    """

    result = np.where(img > threshold, 255, 0).astype(np.uint8)

    return result


# ==========================================
# Step-by-step debug pipeline (for presentation)
# ==========================================

def debug_pipeline(image):
    """
    Returns all intermediate steps for visualization
    """

    steps = {}

    steps["original"] = image
    steps["gray"] = to_grayscale(image)
    steps["denoised"] = remove_noise(steps["gray"])
    steps["enhanced"] = contrast_stretch(steps["denoised"])
    steps["binary"] = simple_threshold(steps["enhanced"])
    steps["morphology"] = closing(steps["binary"])
    steps["final"] = normalize(steps["morphology"])

    return steps