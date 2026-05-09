# ==========================================
# Tools Package Initialization
# Smart Document Scanner Project
# ==========================================

# Image effects
from .negative import negative
from .solarization import solarize

# Advanced processing
from .dithering import dither_image
from .rgb_channels import channel_grid


# ==========================================
# Package Metadata
# ==========================================

__version__ = "1.0.0"
__author__ = "Smart Document Scanner Team"
__description__ = "Extra image processing tools module"