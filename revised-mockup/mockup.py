import tkinter as tk

from src.editor import create_editor

root = tk.Tk()
root.geometry('1600x900')

create_editor(root)

root.mainloop()