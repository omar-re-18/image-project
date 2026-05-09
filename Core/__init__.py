# ==========================================
# Core Package Initialization
# Smart Document Scanner Project
# ==========================================

# Import optimized processing functions
from .preprocessing import to_grayscale, remove_noise
from .enhancement import contrast_stretch
from .morphology import opening, closing
from .scanner_pipeline import auto_scan


# ==========================================
# Package Metadata (optional but professional)
# ==========================================

__version__ = "1.0.0"
__author__ = "Smart Document Scanner Team"
__description__ = "Core image processing module built from scratch using NumPy"