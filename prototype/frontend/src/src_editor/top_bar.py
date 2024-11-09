import tkinter as tk
from src.rdf_manager import export_graph, reset_graph

def create_top_bar(root):
    # create grid layout of top_bar
    root.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
    root.rowconfigure(0, weight=1)

    # define an export button that exports the rdf graph as an xml file
    export_button = tk.Button(command=(lambda: export_graph('unnamedRDF')), text='export graph')
    export_button.grid(row=0, column=0, sticky='nesw')

    reset_button = tk.Button(command=(lambda: reset_graph()), text='reset graph')
    reset_button.grid(row=0, column=1, sticky='nesw')