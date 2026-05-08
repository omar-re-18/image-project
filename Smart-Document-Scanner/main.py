# ==========================================
# Smart Document Scanner
# Main Entry Point
# ==========================================

import sys
from pathlib import Path

# Add parent directory to path so we can import gui
sys.path.insert(0, str(Path(__file__).parent.parent))

from gui.app import run_app


def main():
    """
    Entry point for the application
    Starts the GUI and connects all modules
    """
    run_app()


if __name__ == "__main__":
    main()