import tkinter as tk

def create_right_sidebar(root):
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)

    global testText
    testText = tk.StringVar()
    testLabel = tk.Label(root, textvariable=testText)
    testLabel.grid(row=0, column=0, sticky='nesw')

def update_right_sidebar(resource):
    testText.set(resource)