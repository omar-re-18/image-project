# ==========================================
# Utils Package Initialization
# Smart Document Scanner Project
# ==========================================

# Import common helper functions (if you have them split)
from .image_io import load_image, save_image
from .validators import is_valid_image
from .logger import get_logger


# ==========================================
# Package Metadata
# ==========================================

__version__ = "1.0.0"
__author__ = "Smart Document Scanner Team"
__description__ = "Utility functions for image processing project"