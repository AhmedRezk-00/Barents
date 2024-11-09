import tkinter as tk
import src.rdf_manager as rdf_manager
import src.shared_resources

# function to create left sidebar
def create_left_sidebar(root):
    # divide left sidebar into grids to grid components
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1,2), weight=1)

    # split left sidebar into 3 panels for each level resource 
    data_source_panel = tk.Frame(root)
    data_sink_panel = tk.Frame(root)
    transformation_panel = tk.Frame(root)

    data_source_panel.grid(row=0, column=0, sticky='nesw')
    data_sink_panel.grid(row=1, column=0, sticky='nesw')
    transformation_panel.grid(row=2, column=0, sticky='nesw')

    # added button to add generic data level resource
    data_source_button = tk.Button(data_source_panel, text = 'add data source', command=(lambda: add_data_source()))
    data_source_button.grid(column=0, row=0, sticky = 'nesw')

# function to create rectangle to represent data source on canvas and add data source to rdf graph
def add_data_source():
    square = src.shared_resources.canvas.create_rectangle(50, 50, 100, 100, fill='gray30')
    rdf_manager.add_data_source(0)