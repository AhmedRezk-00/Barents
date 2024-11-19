import tkinter as tk
from src.editor import create_editor

# define root window size, color and title
root = tk.Tk()
root.geometry('1200x675')
root.minsize(800,450)
root.state('zoomed')
root.configure(bg='gray10')
root.title("BFP-Barents frontend")

# function to create gui to edit rdf
create_editor(root)

# function to run gui from root window
root.mainloop()