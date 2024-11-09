import tkinter as tk
from src.rdf_manager import export_graph, reset_graph
import src.shared_resources

# function to create top bar widget 
def create_top_bar(root):
    # create grid layout of top_bar
    root.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
    root.rowconfigure(0, weight=1)

    # define an export button that exports the rdf graph as an xml file
    export_button = tk.Button(root, command=(lambda: export_graph('unnamedRDF')), text='export graph')
    export_button.grid(row=0, column=0, sticky='nesw')

    # reset button that resets rdf graph and canvas on click
    reset_button = tk.Button(root, command=(lambda: reset_canvas()), text='reset graph')
    reset_button.grid(row=0, column=1, sticky='nesw')

# function that resets the rdf graph as well as the canvas 
def reset_canvas():
    reset_graph()
    src.shared_resources.canvas.delete('all')