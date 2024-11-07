import tkinter as tk
from src.graphManager import *

def create_topbar(topbar):
    topbar.rowconfigure(0, weight = 1)
    topbar.columnconfigure((0,1,2,3,4,5,6,7,8,9,10), weight=1)

    importButton = tk.Button(topbar, text="import existing RDF", bd=1, relief="raised", bg='grey')
    importButton.grid(row=0, column=0, sticky='nesw', pady=5, padx=5)

    startButton = tk.Button(topbar, text="Process and Deliver", bd=1, relief="raised", bg='grey')
    startButton.grid(row=0, column=1, sticky='nesw', pady=5)
    
    exportButton = tk.Button(topbar, text="export RDF", command=exportGraph, bd=1, relief="raised", bg='grey')
    exportButton.grid(row=0, column=2, sticky='nesw', pady=5, padx=5)

    delete_all_button = tk.Button(topbar, text="delete all RDF", command=deleteGraph, bd=1, relief="raised", bg='grey')
    delete_all_button.grid(row=0, column=3, sticky='nesw', pady=5, padx=5)