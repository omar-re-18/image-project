import os


# ==========================================
# Image file validation
# ==========================================

def is_valid_image(path):
    """
    Check if file has valid image extension
    """

    valid_ext = (".png", ".jpg", ".jpeg", ".bmp", ".tiff")

    return os.path.isfile(path) and path.lower().endswith(valid_ext)