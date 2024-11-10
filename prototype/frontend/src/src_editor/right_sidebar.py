import tkinter as tk
from src.rdf_manager import rename_triples, resource_dictionary, get_level, set_transformation_type, get_transformation_type

current_resource_id = None
selected_type = None

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

    global knowledge_layer_panel, information_layer_panel, data_layer_panel
    knowledge_layer_panel = tk.Frame(layer_specific_panel)
    create_knowledge_layer_panel(knowledge_layer_panel)
    information_layer_panel = tk.Frame(layer_specific_panel)
    create_information_layer_panel(information_layer_panel)
    data_layer_panel = tk.Frame(layer_specific_panel)
    create_data_layer_panel(data_layer_panel)

def update_right_sidebar(resource_id):
    global current_resource_id
    current_resource_id = resource_id
    name_entry_text.set(resource_dictionary[current_resource_id])

    match get_level(resource_dictionary[resource_id]):
        case "Knowledge Layer":
            knowledge_layer_panel.grid(row=0, column=0, sticky='nesw')
            information_layer_panel.grid_forget()
            data_layer_panel.grid_forget()
        case "Information Layer":
            knowledge_layer_panel.grid_forget()
            information_layer_panel.grid(row=0, column=0, sticky='nesw')
            data_layer_panel.grid_forget()

            transformation_type = get_transformation_type(resource_dictionary[current_resource_id])
            selected_type.set(transformation_type)
        case "Data Layer":
            knowledge_layer_panel.grid_forget()
            information_layer_panel.grid_forget()
            data_layer_panel.grid(row=0, column=0, sticky='nesw')
    
def submit_resource_name():
    if current_resource_id:
        # TODO: ensure name_entry_text doesn't contain any spaces. if it does spaces should be turned into a special character like a dash
        rename_triples(resource_dictionary[current_resource_id], str(name_entry_text.get()))
        resource_dictionary[current_resource_id] = str(name_entry_text.get())

def create_knowledge_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

def create_data_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

def create_information_layer_panel(root):
    root.columnconfigure((0,1,2), weight=1)
    root.rowconfigure(0, weight=1)

    global selected_type
    selected_type = tk.StringVar()
    def select_checkbox(transformation_type):
        selected_type.set(transformation_type)
        set_transformation_type(resource_dictionary[current_resource_id], transformation_type)

    filter_checkbox = tk.Checkbutton(root, text="filter",variable=selected_type, onvalue='filter', offvalue='', command=(lambda: select_checkbox('filter')))
    filter_checkbox.grid(column=0, row=0, sticky='nesw')
    map_checkbox = tk.Checkbutton(root, text="map",variable=selected_type, onvalue='map', offvalue='', command=(lambda: select_checkbox('map')))
    map_checkbox.grid(column=1, row=0, sticky='nesw')
    reduce_checkbox = tk.Checkbutton(root, text="reduce",variable=selected_type, onvalue='reduce', offvalue='', command=(lambda: select_checkbox('reduce')))
    reduce_checkbox.grid(column=2, row=0, sticky='nesw')

