import tkinter as tk


# ==========================================
# 1. Button Factory
# ==========================================

def create_button(parent, text, command, bg="#444", fg="white", width=12):
    """
    Creates a styled button
    """

    btn = tk.Button(
        parent,
        text=text,
        command=command,
        bg=bg,
        fg=fg,
        width=width,
        relief=tk.RAISED,
        bd=2,
        activebackground="#666",
        activeforeground="white"
    )

    btn.pack(side=tk.LEFT, padx=5, pady=5)

    return btn


# ==========================================
# 2. Panel Creator
# ==========================================

def create_panel(parent, bg="black"):
    """
    Creates a simple container panel
    """

    frame = tk.Frame(parent, bg=bg)
    frame.pack(fill=tk.BOTH, expand=True)

    return frame


# ==========================================
# 3. Image Label Creator
# ==========================================

def create_image_label(parent, text="Image"):
    """
    Label for displaying images
    """

    label = tk.Label(
        parent,
        text=text,
        bg="black",
        fg="white"
    )

    label.pack(padx=10, pady=10)

    return label


# ==========================================
# 4. Status Label
# ==========================================

def create_status_bar(parent):
    """
    Bottom status bar
    """

    status = tk.Label(
        parent,
        text="Ready",
        bg="#1e1e1e",
        fg="white",
        anchor="w"
    )

    status.pack(side=tk.BOTTOM, fill=tk.X)

    return status


# ==========================================
# 5. Toolbar Builder
# ==========================================

def create_toolbar(parent):
    """
    Top toolbar container
    """

    toolbar = tk.Frame(parent, bg="#2b2b2b", height=50)
    toolbar.pack(side=tk.TOP, fill=tk.X)

    return toolbar