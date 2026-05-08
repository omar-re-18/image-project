import tkinter as tk


# ==========================================
# Main Layout Builder
# ==========================================

def build_layout(root):
    """
    Builds UI layout structure (frames + labels)
    without binding logic/events
    """

    # ======================================
    # Top Control Frame (Buttons area)
    # ======================================
    top_frame = tk.Frame(root, bg="#2b2b2b", height=80)
    top_frame.pack(side=tk.TOP, fill=tk.X)

    # ======================================
    # Main Display Frame
    # ======================================
    main_frame = tk.Frame(root, bg="black")
    main_frame.pack(fill=tk.BOTH, expand=True)

    # ======================================
    # Left Panel (Original Image)
    # ======================================
    left_frame = tk.Frame(main_frame, bg="black")
    left_frame.pack(side=tk.LEFT, expand=True, padx=10, pady=10)

    original_label = tk.Label(
        left_frame,
        text="Original Image",
        bg="black",
        fg="white"
    )
    original_label.pack()

    # ======================================
    # Right Panel (Processed Image)
    # ======================================
    right_frame = tk.Frame(main_frame, bg="black")
    right_frame.pack(side=tk.RIGHT, expand=True, padx=10, pady=10)

    processed_label = tk.Label(
        right_frame,
        text="Processed Image",
        bg="black",
        fg="white"
    )
    processed_label.pack()

    # ======================================
    # Status Bar
    # ======================================
    status_bar = tk.Label(
        root,
        text="Ready",
        bg="#1e1e1e",
        fg="white",
        anchor="w"
    )
    status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    # Return all UI components
    return {
        "top_frame": top_frame,
        "main_frame": main_frame,
        "original_label": original_label,
        "processed_label": processed_label,
        "status_bar": status_bar
    }