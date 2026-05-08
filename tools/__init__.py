# ==========================================
# Tools Package Initialization
# Smart Document Scanner Project
# ==========================================

# Arithmetic operations
from .arithmetic import (
    add,
    subtract,
    multiply,
    divide
)

# Image effects
from .negative import negative
from .solarization import solarize

# Advanced processing
from .dithering import floyd_steinberg_dithering
from .rgb_channels import split_rgb_channels


# ==========================================
# Package Metadata
# ==========================================

__version__ = "1.0.0"
__author__ = "Smart Document Scanner Team"
__description__ = "Extra image processing tools module"