import tkinter as tk

def create_rightSidebar(right_Sidebar):
    placeholder = tk.Label(right_Sidebar, text="Resources can be renamed here. \n partOf triples will be created by dragging lines between resources. \n Data sinks can also be renamed here. It might be useful for the user to manage data zones as well, in this mockup however they'd be handled like data sources. \n Functions and Procedures will be further defined & customized here.", wraplength=200)
    placeholder.pack()