import tkinter as tk

from src.graphManager import *
from src.topbar import create_topbar
from src.leftSidebar.leftSidebar import create_leftSidebar
from src.canvas import create_canvas
from src.rightSidebar import create_rightSidebar

def create_editor(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight = 1)
    root.rowconfigure(1, weight=30)

    topbar = tk.Frame(root, bd=1, relief="solid")
    topbar.grid(row=0, column=0, sticky='nesw')
    create_topbar(topbar)

    mainframe = tk.Frame(root)
    mainframe.grid(row = 1, column=0, sticky='nesw')
    mainframe.columnconfigure((0,2), weight=1)
    mainframe.columnconfigure(1, weight=4)
    mainframe.rowconfigure(0, weight=1)

    canvas = tk.Frame(mainframe, bd=1, relief="solid")
    canvas.grid(row=0, column=1, sticky='nesw')
    create_canvas(canvas)

    left_sidebar = tk.Frame(mainframe, bd=1, relief="solid")
    left_sidebar.grid(row=0, column=0, sticky='nesw')
    create_leftSidebar(left_sidebar)

    right_sidebar = tk.Frame(mainframe, bd=1, relief="solid")
    right_sidebar.grid(row=0, column=2, sticky='nesw')
    create_rightSidebar(right_sidebar)

    
