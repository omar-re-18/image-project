import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
import numpy as np

# Core modules
from core.scanner_pipeline import auto_scan, debug_pipeline
from core.preprocessing import to_grayscale
from core.enhancement import contrast_stretch, adjust_brightness
from core.morphology import opening, closing

# Tools
from tools.negative import negative
from tools.solarization import solarize
from tools.dithering import floyd_steinberg_dithering
from tools.rgb_channels import channel_grid


# ==========================================
# Global State
# ==========================================

original_image = None
current_image = None


# ==========================================
# Load Image
# ==========================================

def upload_image():
    global original_image, current_image

    path = filedialog.askopenfilename()

    if not path:
        return

    img = cv2.imread(path)

    if img is None:
        messagebox.showerror("Error", "Invalid image file")
        return

    original_image = img
    current_image = img

    show_image(current_image, original_label)


# ==========================================
# Display Image Helper
# ==========================================

def show_image(img, label):
    img = cv2.resize(img, (400, 400))

    if len(img.shape) == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img = tk.PhotoImage(master=root, data=cv2.imencode('.png', img)[1].tobytes())

    label.configure(image=img)
    label.image = img


# ==========================================
# Auto Scan
# ==========================================

def run_auto_scan():
    global current_image

    if original_image is None:
        return

    current_image = auto_scan(original_image)
    show_image(current_image, processed_label)


# ==========================================
# Manual Tools
# ==========================================

def apply_negative():
    global current_image
    current_image = negative(to_grayscale(original_image))
    show_image(current_image, processed_label)


def apply_solarization():
    global current_image
    current_image = solarize(to_grayscale(original_image))
    show_image(current_image, processed_label)


def apply_dithering():
    global current_image
    gray = to_grayscale(original_image)
    current_image = floyd_steinberg_dithering(gray)
    show_image(current_image, processed_label)


def apply_contrast():
    global current_image
    gray = to_grayscale(original_image)
    current_image = contrast_stretch(gray)
    show_image(current_image, processed_label)


def apply_opening():
    global current_image
    gray = to_grayscale(original_image)
    current_image = opening(gray)
    show_image(current_image, processed_label)


def apply_closing():
    global current_image
    gray = to_grayscale(original_image)
    current_image = closing(gray)
    show_image(current_image, processed_label)


def show_rgb():
    global current_image
    current_image = channel_grid(original_image)
    show_image(current_image, processed_label)


# ==========================================
# GUI Setup
# ==========================================

def run_app():
    global root, original_label, processed_label

    root = tk.Tk()
    root.title("Smart Document Scanner")
    root.geometry("1000x600")
    root.configure(bg="black")

    # Buttons Frame
    frame = tk.Frame(root, bg="gray")
    frame.pack(side=tk.TOP, fill=tk.X)

    tk.Button(frame, text="Upload", command=upload_image).pack(side=tk.LEFT)
    tk.Button(frame, text="Auto Scan", command=run_auto_scan).pack(side=tk.LEFT)
    tk.Button(frame, text="Negative", command=apply_negative).pack(side=tk.LEFT)
    tk.Button(frame, text="Solarization", command=apply_solarization).pack(side=tk.LEFT)
    tk.Button(frame, text="Dithering", command=apply_dithering).pack(side=tk.LEFT)
    tk.Button(frame, text="Contrast", command=apply_contrast).pack(side=tk.LEFT)
    tk.Button(frame, text="Opening", command=apply_opening).pack(side=tk.LEFT)
    tk.Button(frame, text="Closing", command=apply_closing).pack(side=tk.LEFT)
    tk.Button(frame, text="RGB View", command=show_rgb).pack(side=tk.LEFT)

    # Image Display Area
    display_frame = tk.Frame(root, bg="black")
    display_frame.pack()

    original_label = tk.Label(display_frame, text="Original Image", bg="black")
    original_label.pack(side=tk.LEFT, padx=20)

    processed_label = tk.Label(display_frame, text="Processed Image", bg="black")
    processed_label.pack(side=tk.RIGHT, padx=20)

    root.mainloop()