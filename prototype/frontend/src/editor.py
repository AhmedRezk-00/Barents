import tkinter as tk

def create_editor(root):
    # divide entry window into rows and columns
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=10)
    root.columnconfigure((0,2), weight=1)
    root.columnconfigure(1, weight=5)

    # define bar at the top of editor, a left and right sidebar, and the main canvas
    top_bar = tk.Frame(root)
    left_sidebar = tk.Frame(root)
    canvas = tk.Frame(root)
    right_sidebar = tk.Frame(root)

    # grid top bar, left- and right sidebar, canvas
    top_bar.grid(column=0, row=0, columnspan=3, sticky='nesw')
    left_sidebar.grid(column=0, row=1, sticky='nesw')
    canvas.grid(column=1, row=1, sticky='nesw')
    right_sidebar.grid(column=2, row=1, sticky='nesw')