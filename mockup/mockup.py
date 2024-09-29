import tkinter as tk
from src.gui import create_gui

def main():
    root = tk.Tk()
    root.title("BARENTS Mockup")

    root.geometry("800x600")
    root.minsize(600, 300)  
    # root.maxsize(1200, 800)

    # Call function from src/gui.py
    create_gui(root)

    root.mainloop()

if __name__ == "__main__":
    main()