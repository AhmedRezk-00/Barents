import tkinter as tk

def create_left_sidebar(root):
    # divide left sidebar into grids to grid components
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1,2), weight=1)

    data_source_panel = tk.Frame(root)
    data_sink_panel = tk.Frame(root)
    transformation_panel = tk.Frame(root)

    data_source_panel.grid(row=0, column=0, sticky='nesw')
    data_sink_panel.grid(row=1, column=0, sticky='nesw')
    transformation_panel.grid(row=2, column=0, sticky='nesw')