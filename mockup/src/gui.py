import tkinter as tk

def create_gui(root):
    # Create the left sidebar
    left_sidebar = tk.Frame(root, width=200, bg='lightgray')
    left_sidebar.pack(side="left", fill="y")

    # Create the right sidebar
    right_sidebar = tk.Frame(root, width=200, bg='lightgray')
    right_sidebar.pack(side="right", fill="y")

    # Create a main content area 
    main_content = tk.Frame(root, bg='white')
    main_content.pack(side="left", fill="both", expand=True)  