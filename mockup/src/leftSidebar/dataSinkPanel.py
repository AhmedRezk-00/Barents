import tkinter as tk
from src.graphManager import add_dataSink

def create_dataSink_panel(dataSink_panel):
    dataSink_panel.columnconfigure(0, weight=1)
    dataSink_panel.rowconfigure(0, weight=1)
    dataSink_panel.rowconfigure(1, weight=10)

    dataSink_label = tk.Label(dataSink_panel, text="Data Sinks")
    dataSink_label.grid(row=0, column=0, sticky='n', pady=10, padx=10)
    dataSink_button = tk.Button(dataSink_panel, text="add Data Sink", command=(lambda: add_dataSink("unnamedDataZone")), bg='grey')
    dataSink_button.grid(row=1, column=0, sticky='new', pady=5, padx=5)