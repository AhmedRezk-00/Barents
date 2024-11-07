import tkinter as tk
from src.rdfManager import exportGraph, resetGraph
import src.sharedResources

def create_topbar(topbar):
    topbar.rowconfigure(0, weight=1)
    topbar.columnconfigure((0,1), weight=1)
    
    export_button = tk.Button(topbar, text='export as rdf', command=(lambda: exportGraph()), bg='gray20')
    export_button.grid(row=0, column=0, sticky='nesw', pady=5, padx=5)

    reset_button = tk.Button(topbar, text='reset rdf', command=(lambda: reset_function()), bg='gray20')
    reset_button.grid(row=0, column=1, sticky='nesw', pady=5, padx=5)

def reset_function():
    resetGraph()
    if src.sharedResources.canvas:
        src.sharedResources.canvas.delete('all')