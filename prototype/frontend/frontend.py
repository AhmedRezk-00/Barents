import customtkinter as ctk
from src.editor import create_editor

# define root window size, color and title
root = ctk.CTk()
root.geometry('1200x675')
root.minsize(900,500)
root.state('zoomed')
root.configure(bg='gray10')
root.title("BFP-Barents frontend")

# function to create gui to edit rdf
create_editor(root)

root.mainloop()
