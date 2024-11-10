import tkinter as tk
from src.rdf_manager import rename_triples, resource_dictionary

current_resource_id = None

# TODO: add comments for this file
def create_right_sidebar(root):
    root.rowconfigure((0,1), weight=1)
    root.columnconfigure(0, weight=1)

    generic_panel = tk.Frame(root)
    generic_panel.grid(row=0, column=0, sticky='nesw')
    generic_panel.columnconfigure(0, weight=1)
    generic_panel.rowconfigure((0,1,2), weight=1)

    generic_panel_label = tk.Label(generic_panel, text='Customize Resource:')
    generic_panel_label.grid(row=0, column=0, sticky='nesw')
    
    global name_entry_text
    name_entry_text = tk.StringVar(value='')
    resource_name_entry = tk.Entry(generic_panel, textvariable=name_entry_text)
    resource_name_entry.grid(row=1, column=0, sticky='ew')

    resource_name_button = tk.Button(generic_panel, text='update name', command=(lambda: submit_resource_name()))
    resource_name_button.grid(row=2, column=0, sticky='nesw')

    layer_specific_panel = tk.Frame(root)
    layer_specific_panel.grid(row=1, column=0, sticky='nesw')
    layer_specific_panel.columnconfigure(0, weight=1)
    layer_specific_panel.rowconfigure(0, weight=1)

def update_right_sidebar(resource_id):
    global current_resource_id
    current_resource_id = resource_id
    name_entry_text.set(resource_dictionary[current_resource_id])

def submit_resource_name():
    if current_resource_id:
        # TODO: ensure name_entry_text doesn't contain any spaces. if it does spaces should be turned into a special character like a dash
        rename_triples(resource_dictionary[current_resource_id], str(name_entry_text.get()))
        resource_dictionary[current_resource_id] = str(name_entry_text.get())