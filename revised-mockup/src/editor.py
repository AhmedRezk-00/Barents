import tkinter as tk

from src.graphManager import testRun

def create_editor(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    test_button = tk.Button(root, text='run test graph', command=(lambda: testRun()), bg='grey')
    test_button.grid(row=0, column=0, sticky='nesw', pady=5, padx=5)