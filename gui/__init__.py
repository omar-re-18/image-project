# ==========================================
# GUI Package Initialization
# Smart Document Scanner Project
# ==========================================

# Import main application runner
from .app import run_app

# Optional: expose main UI components if needed
from .layout import build_layout
from .widgets import create_button, create_panel


# ==========================================
# Package Metadata
# ==========================================

__version__ = "1.0.0"
__author__ = "Smart Document Scanner Team"
__description__ = "GUI module for Smart Document Scanner"