import tkinter as tk
from src.gui import create_gui

def main():
    root = tk.Tk()
    root.title("BARENTS Mockup")

    root.geometry("1600x900")
    root.resizable(False, False)

    # Call function from src/gui.py
    create_gui(root)

    root.mainloop()

if __name__ == "__main__":
    main()