import os
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
import cv2

# ==========================================
# Core Modules
# ==========================================

from core.scanner_pipeline import auto_scan
from core.preprocessing import to_grayscale
from core.enhancement import contrast_stretch
from core.morphology import opening, closing

# ==========================================
# Tools
# ==========================================

from tools.negative import negative
from tools.solarization import solarize
from tools.dithering import dither_image
from tools.rgb_channels import channel_grid

# ==========================================
# Utils
# ==========================================

from utils.image_io import load_image
from utils.display import prepare_image


# ==========================================
# Theme Configuration
# ==========================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# ==========================================
# Main Application
# ==========================================

class SmartScannerApp(ctk.CTk):

    def __init__(self):

        super().__init__()

        # ==================================
        # Window Setup
        # ==================================

        self.title("Smart Document Scanner")

        self.geometry("1450x850")

        self.minsize(1300, 750)

        self.configure(fg_color="#1a1a1a")

        # ==================================
        # Image State
        # ==================================

        self.original_image = None
        self.current_image = None

        # ==================================
        # Icons Cache
        # ==================================

        self.icons = {}

        # ==================================
        # Build UI
        # ==================================

        self.build_ui()

    # ======================================
    # Load Icon
    # ======================================

    def load_icon(self, filename, size=(24, 24)):

        # Get the project root by going up from gui directory
        gui_dir = Path(__file__).parent
        project_root = gui_dir.parent
        icon_path = project_root / "assets" / "icons" / filename

        # Handle missing icon file
        if not icon_path.exists():
            # Create a placeholder image if icon doesn't exist
            placeholder = Image.new("RGB", size, color=(100, 100, 100))
            return ctk.CTkImage(
                light_image=placeholder,
                dark_image=placeholder,
                size=size
            )

        image = Image.open(icon_path)

        return ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=size
        )

    # ======================================
    # Build UI
    # ======================================

    def build_ui(self):

        # ==================================
        # Sidebar
        # ==================================

        self.sidebar = ctk.CTkFrame(
            self,
            width=260,
            corner_radius=0,
            fg_color="#202020"
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # ==================================
        # Logo / Title
        # ==================================

        self.logo = ctk.CTkLabel(
            self.sidebar,
            text="SMART\nSCANNER",
            font=("Arial", 30, "bold"),
            text_color="#00d9ff"
        )

        self.logo.pack(
            pady=(35, 25)
        )

        # ==================================
        # Buttons
        # ==================================

        self.create_sidebar_button(
            "Upload Image",
            "upload.png",
            self.upload_image
        )

        self.create_sidebar_button(
            "Auto Scan",
            "scan.png",
            self.run_auto_scan
        )

        self.create_sidebar_button(
            "Negative",
            "negative.png",
            self.apply_negative
        )

        self.create_sidebar_button(
            "Solarization",
            "solarize.png",
            self.apply_solarization
        )

        self.create_sidebar_button(
            "Dithering",
            "dithering.png",
            self.apply_dithering
        )

        self.create_sidebar_button(
            "Contrast",
            "contrast.png",
            self.apply_contrast
        )

        self.create_sidebar_button(
            "Opening",
            "opening.png",
            self.apply_opening
        )

        self.create_sidebar_button(
            "Closing",
            "closing.png",
            self.apply_closing
        )

        self.create_sidebar_button(
            "RGB Channels",
            "rgb.png",
            self.show_rgb
        )

        self.create_sidebar_button(
            "Reset",
            "reset.png",
            self.reset_image
        )

        # ==================================
        # Main Area
        # ==================================

        self.main_area = ctk.CTkFrame(
            self,
            fg_color="#1a1a1a"
        )

        self.main_area.pack(
            side="right",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # ==================================
        # Status Bar
        # ==================================

        self.status = ctk.CTkLabel(
            self.main_area,
            text="Ready",
            height=40,
            anchor="w",
            corner_radius=10,
            fg_color="#2a2a2a",
            font=("Arial", 14)
        )

        self.status.pack(
            fill="x",
            pady=(0, 15)
        )

        # ==================================
        # Images Area
        # ==================================

        self.images_frame = ctk.CTkFrame(
            self.main_area,
            fg_color="transparent"
        )

        self.images_frame.pack(
            fill="both",
            expand=True
        )

        # ==================================
        # Original Image Panel
        # ==================================

        self.original_panel = self.create_image_panel(
            self.images_frame,
            "Original Image"
        )

        self.original_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        self.original_label = ctk.CTkLabel(
            self.original_panel,
            text=""
        )

        self.original_label.pack(
            expand=True,
            padx=10,
            pady=10
        )

        # ==================================
        # Processed Image Panel
        # ==================================

        self.processed_panel = self.create_image_panel(
            self.images_frame,
            "Processed Image"
        )

        self.processed_panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10
        )

        self.processed_label = ctk.CTkLabel(
            self.processed_panel,
            text=""
        )

        self.processed_label.pack(
            expand=True,
            padx=10,
            pady=10
        )

    # ======================================
    # Sidebar Button
    # ======================================

    def create_sidebar_button(
        self,
        text,
        icon_name,
        command
    ):

        icon = self.load_icon(icon_name)

        button = ctk.CTkButton(
            self.sidebar,
            text=text,
            image=icon,
            command=command,
            height=48,
            corner_radius=12,
            anchor="w",
            font=("Arial", 14, "bold"),
            fg_color="#2d2d2d",
            hover_color="#3b3b3b"
        )

        button.pack(
            fill="x",
            padx=18,
            pady=6
        )

    # ======================================
    # Image Panel
    # ======================================

    def create_image_panel(self, parent, title):

        panel = ctk.CTkFrame(
            parent,
            corner_radius=18,
            fg_color="#232323"
        )

        label = ctk.CTkLabel(
            panel,
            text=title,
            font=("Arial", 20, "bold"),
            text_color="white"
        )

        label.pack(
            pady=(15, 5)
        )

        return panel

    # ======================================
    # Upload Image
    # ======================================

    def upload_image(self):

        path = filedialog.askopenfilename(
            filetypes=[
                (
                    "Images",
                    "*.png *.jpg *.jpeg *.bmp"
                )
            ]
        )

        if not path:
            return

        try:

            self.original_image = load_image(path)

            self.current_image = self.original_image.copy()

            self.display_image(
                self.original_image,
                self.original_label
            )

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Image uploaded successfully"
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    # ======================================
    # Display Image
    # ======================================

    def display_image(self, img, label):

        img = prepare_image(
            img,
            size=(520, 520)
        )

        image = Image.fromarray(img)

        ctk_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,
            size=(520, 520)
        )

        label.configure(
            image=ctk_image,
            text=""
        )

        label.image = ctk_image

    # ======================================
    # Update Status
    # ======================================

    def update_status(self, text):

        self.status.configure(
            text=f"  {text}"
        )

    # ======================================
    # Processing Operations
    # ======================================

    def run_auto_scan(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            self.current_image = auto_scan(
                self.original_image
            )

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Auto scan completed"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_negative(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            gray = to_grayscale(
                self.original_image
            )

            self.current_image = negative(gray)

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Negative effect applied"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_solarization(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            gray = to_grayscale(
                self.original_image
            )

            self.current_image = solarize(gray)

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Solarization applied"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_dithering(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        # Ask user to choose dithering method
        choice = messagebox.askquestion(
            "Dithering Method",
            "Choose dithering method:\n\n" +
            "Yes = Floyd-Steinberg (High Quality, Slower)\n" +
            "No = Ordered Dithering (Fast, Good Quality)\n\n" +
            "Floyd-Steinberg: 252x slower but better quality\n" +
            "Ordered: Much faster with good visual results"
        )

        method = 'floyd_steinberg' if choice == 'yes' else 'ordered'

        try:
            gray = to_grayscale(self.original_image)

            self.current_image = dither_image(gray, method=method)

            self.display_image(
                self.current_image,
                self.processed_label
            )

            method_name = "Floyd-Steinberg" if method == 'floyd_steinberg' else "Ordered"
            self.update_status(
                f"{method_name} dithering completed"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_contrast(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            gray = to_grayscale(
                self.original_image
            )

            self.current_image = contrast_stretch(gray)

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Contrast enhanced"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_opening(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            gray = to_grayscale(
                self.original_image
            )

            self.current_image = opening(gray)

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Opening applied"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_closing(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            gray = to_grayscale(
                self.original_image
            )

            self.current_image = closing(gray)

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Closing applied"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_rgb(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            self.current_image = channel_grid(
                self.original_image
            )

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "RGB channels visualized"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # ======================================
    # Reset
    # ======================================

    def reset_image(self):

        if self.original_image is None:
            messagebox.showwarning("Warning", "Please upload an image first")
            return

        try:
            self.current_image = self.original_image.copy()

            self.display_image(
                self.current_image,
                self.processed_label
            )

            self.update_status(
                "Image reset"
            )
        except Exception as e:
            messagebox.showerror("Error", str(e))


# ==========================================
# Run Application
# ==========================================

def run_app():

    app = SmartScannerApp()

    app.mainloop()


# ==========================================
# Main
# ==========================================

if __name__ == "__main__":

    run_app()