import numpy as np

from core.scanner_pipeline import auto_scan, debug_pipeline
from core.preprocessing import to_grayscale
from core.enhancement import contrast_stretch
from core.morphology import opening, closing

from tools.negative import negative
from tools.solarization import solarize
from tools.dithering import floyd_steinberg_dithering
from tools.rgb_channels import channel_grid


# ==========================================
# Event Handlers Class
# ==========================================

class EventHandler:

    def __init__(self, ui):
        """
        ui → reference to GUI elements (labels, state, etc.)
        """
        self.ui = ui
        self.original_image = None
        self.current_image = None


    # ======================================
    # Set Image
    # ======================================

    def set_image(self, img):
        self.original_image = img
        self.current_image = img


    # ======================================
    # Auto Scan Event
    # ======================================

    def auto_scan(self):
        if self.original_image is None:
            return

        self.current_image = auto_scan(self.original_image)
        self.ui.update_processed(self.current_image)


    # ======================================
    # Negative Event
    # ======================================

    def negative(self):
        if self.original_image is None:
            return

        gray = to_grayscale(self.original_image)
        self.current_image = negative(gray)
        self.ui.update_processed(self.current_image)


    # ======================================
    # Solarization Event
    # ======================================

    def solarization(self):
        if self.original_image is None:
            return

        gray = to_grayscale(self.original_image)
        self.current_image = solarize(gray)
        self.ui.update_processed(self.current_image)


    # ======================================
    # Dithering Event
    # ======================================

    def dithering(self):
        if self.original_image is None:
            return

        gray = to_grayscale(self.original_image)
        self.current_image = floyd_steinberg_dithering(gray)
        self.ui.update_processed(self.current_image)


    # ======================================
    # Contrast Event
    # ======================================

    def contrast(self):
        if self.original_image is None:
            return

        gray = to_grayscale(self.original_image)
        self.current_image = contrast_stretch(gray)
        self.ui.update_processed(self.current_image)


    # ======================================
    # Morphology Events
    # ======================================

    def opening(self):
        if self.original_image is None:
            return

        gray = to_grayscale(self.original_image)
        self.current_image = opening(gray)
        self.ui.update_processed(self.current_image)


    def closing(self):
        if self.original_image is None:
            return

        gray = to_grayscale(self.original_image)
        self.current_image = closing(gray)
        self.ui.update_processed(self.current_image)


    # ======================================
    # RGB Event
    # ======================================

    def rgb_view(self):
        if self.original_image is None:
            return

        self.current_image = channel_grid(self.original_image)
        self.ui.update_processed(self.current_image)


    # ======================================
    # Debug Pipeline Event
    # ======================================

    def show_pipeline_steps(self):
        """
        Returns all steps for visualization mode
        """
        if self.original_image is None:
            return None

        return debug_pipeline(self.original_image)