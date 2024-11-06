import tkinter as tk
from src.editor import create_editor
from src.topbar import create_topbar

def create_gui(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0,weight=1)
    root.rowconfigure(1, weight=10)

    editor = tk.Frame(root, bg='gray20')
    editor.grid(column=0, row=1, sticky='nesw')
    create_editor(editor)

    topbar = tk.Frame(root, bg='gray30')
    topbar.grid(column=0, row=0, sticky='nesw')
    create_topbar(topbar)