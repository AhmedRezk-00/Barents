import tkinter as tk
from turtle import window_width
from src.src_editor.canvas import create_canvas
from src.src_editor.top_bar import create_top_bar
from src.src_editor.right_sidebar import create_right_sidebar
from src.src_editor.left_sidebar import create_left_sidebar


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

    # function to create all the defined editor components
    create_canvas(canvas)
    create_top_bar(top_bar)
    create_left_sidebar(left_sidebar)
    create_canvas(canvas)
    create_right_sidebar(right_sidebar)