import tkinter as tk

from src.skeleton import create_gui

root = tk.Tk()
root.geometry('1600x900')
root.configure(bg='gray30')

create_gui(root)

root.mainloop()