import tkinter as tk
from src.graphManager import *
from src.canvas import create_square

def create_dataSource_panel(dataSource_panel):
    dataSource_panel.columnconfigure(0, weight=1)
    dataSource_panel.rowconfigure(0, weight=1)
    dataSource_panel.rowconfigure(1, weight=10)

    dataSource_label = tk.Label(dataSource_panel, text="Data Sources")
    dataSource_label.grid(row=0, column=0, sticky='n', pady=10, padx=10)

    button_frame = tk.Frame(dataSource_panel)
    button_frame.grid(row=1, column=0, sticky='nesw', pady=5, padx=5)

    dataSource_button = tk.Button(button_frame, text="add test data Source", command=(lambda: add_dataSourceNode("test")), bd=1, relief="raised", bg='grey')
    chocolate_button = tk.Button(button_frame, text="add Chocolate", command=(lambda: add_dataSource("chocolate")), bd=1, relief="raised", bg='grey')

    chocolate_button.pack(fill=tk.X, padx=5, pady=5)
    dataSource_button.pack(fill=tk.X, padx=5, pady=5)

def add_dataSourceNode(source):
    add_dataSource(source)
    create_square()