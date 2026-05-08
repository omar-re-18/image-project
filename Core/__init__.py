# ==========================================
# Core Package Initialization
# Smart Document Scanner Project
# ==========================================

# Import main manual processing functions
from .manual_processing import (
    to_grayscale,
    adjust_brightness,
    contrast_stretch,
    box_blur,
    threshold,
    negative,
    solarize,
    add,
    subtract,
    multiply,
    divide,
    erosion,
    dilation,
    opening,
    closing
)

# Import scanner pipeline (if exists)
try:
    from .scanner_pipeline import auto_scan
except ImportError:
    auto_scan = None


# ==========================================
# Package Metadata (optional but professional)
# ==========================================

__version__ = "1.0.0"
__author__ = "Smart Document Scanner Team"
__description__ = "Core image processing module built from scratch using NumPy"