import tkinter as tk

def create_left_sidebar(root):
    # divide left sidebar into grids to grid components
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1,2), weight=1)