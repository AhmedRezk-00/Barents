import tkinter as tk 
import src.shared_resources

# function to create canvas of editor. rdf graph resources should be displayed here 
def create_canvas(root):
    # create canvas widget
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight=1)
    canvas = tk.Canvas(root, relief='solid', highlightbackground='black')
    canvas.grid(row=0, column=0, sticky='nesw')

    # define shared_resources.canvas to be this canvas
    src.shared_resources.canvas = canvas