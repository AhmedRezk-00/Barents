import tkinter as tk
from src.graphManager import addTransformation

def create_transformation_panel(transformation_panel):
    transformation_panel.columnconfigure(0, weight=1)
    transformation_panel.rowconfigure(0, weight=1)
    transformation_panel.rowconfigure(1, weight=10)

    transformation_label = tk.Label(transformation_panel, text="Transformation")
    transformation_label.grid(row=0, column=0, sticky='n', pady=5, padx=5)

    button_frame = tk.Frame(transformation_panel, bd=1, relief="solid")
    button_frame.grid(column=0, row=1, sticky='nesw', padx=5, pady=5)

    button_frame.columnconfigure((0,1), weight=1)
    button_frame.rowconfigure((0,1), weight=1)

    filter_button = tk.Button(button_frame, text="filter", bd=1, relief="raised", bg='grey', command=(lambda:addTransformation("filter")))
    map_button = tk.Button(button_frame, text="map", bd=1, relief="raised", bg='grey', command=(lambda:addTransformation("map")))
    reduce_button = tk.Button(button_frame, text="reduce", bd=1, relief="raised", bg='grey', command=(lambda:addTransformation("reduce")))
    procedure_button = tk.Button(button_frame, text="procedure", bd=1, relief="raised", bg='grey', command=(lambda: addTransformation("procedure")))

    filter_button.grid(column=0, row=0, sticky="nesw", padx=5, pady=5)
    map_button.grid(column=1, row=0, sticky="nesw", padx=5, pady=5)
    reduce_button.grid(column=0, row=1, sticky="nesw", padx=5, pady=5)
    procedure_button.grid(column=1, row=1, sticky="nesw", padx=5, pady=5)