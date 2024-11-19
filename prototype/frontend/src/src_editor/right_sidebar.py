import customtkinter as ctk
from src.rdf_manager import rename_triples, resource_dictionary, get_level, set_transformation_type, get_transformation_type, set_transformation_function, get_transformation_function, set_source, set_zone, get_source, get_zone

# id of resource currently being edited in right sidebar
current_resource_id = None
# transformation type of the currently selected information level resource
selected_type = None
# function (that is its expression) of currently selected information level resource
function_entry_text = None
# data soruce literal of currently selected data level resourse
source_entry_text = None
# data zone literal of currently selected knowledge level resource
zone_entry_text = None
FONT = ("Helvetica", 16, "bold")



# TODO: add comments for this file
def create_right_sidebar(root):
    root.rowconfigure((0,1), weight=1)
    root.columnconfigure(0, weight=1)

    generic_panel = ctk.CTkFrame(root)
    generic_panel.grid(row=0, column=0, sticky='nesw')
    generic_panel.columnconfigure(0, weight=1)
    generic_panel.rowconfigure((0,1,2), weight=1)

    generic_panel_label = ctk.CTkLabel(generic_panel, text='Customize Resource:',font=FONT)
    generic_panel_label.grid(row=0, column=0, sticky='nesw')
    
    global name_entry_text
    name_entry_text = ctk.StringVar(value='')
    resource_name_entry = ctk.CTkEntry(generic_panel, textvariable=name_entry_text,font=FONT)
    resource_name_entry.grid(row=1, column=0, sticky='ew')

    resource_name_button = ctk.CTkButton(generic_panel, fg_color="dark blue", text='Update Name',font=FONT, command=(lambda: submit_resource_name()),corner_radius=30)
    resource_name_button.grid(row=2, column=0, sticky='nesw',pady=10,padx=10)
    layer_specific_panel = ctk.CTkFrame(root)
    layer_specific_panel.grid(row=1, column=0, sticky='nesw')
    layer_specific_panel.columnconfigure(0, weight=1)
    layer_specific_panel.rowconfigure(0, weight=1)

    global knowledge_layer_panel, information_layer_panel, data_layer_panel
    knowledge_layer_panel = ctk.CTkFrame(layer_specific_panel)
    create_knowledge_layer_panel(knowledge_layer_panel)
    information_layer_panel = ctk.CTkFrame(layer_specific_panel)
    create_information_layer_panel(information_layer_panel)
    data_layer_panel = ctk.CTkFrame(layer_specific_panel)
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

            zone_entry_text.set(get_zone(resource_dictionary[current_resource_id]))
        case "Information Layer":
            knowledge_layer_panel.grid_forget()
            information_layer_panel.grid(row=0, column=0, sticky='nesw')
            data_layer_panel.grid_forget()

            transformation_type = get_transformation_type(resource_dictionary[current_resource_id])
            selected_type.set(transformation_type)

            function_entry = get_transformation_function(resource_dictionary[current_resource_id])
            function_entry_text.set(function_entry)
        case "Data Layer":
            knowledge_layer_panel.grid_forget()
            information_layer_panel.grid_forget()
            data_layer_panel.grid(row=0, column=0, sticky='nesw')
            source_entry_text.set(get_source(resource_dictionary[current_resource_id]))
    
def submit_resource_name():
    if current_resource_id:
        # TODO: ensure name_entry_text doesn't contain any spaces. if it does spaces should be turned into a special character like a dash
        rename_triples(resource_dictionary[current_resource_id], str(name_entry_text.get()))
        resource_dictionary[current_resource_id] = str(name_entry_text.get())

def create_knowledge_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1), weight=1)

    global zone_entry_text
    zone_entry_text = ctk.StringVar(value='')
    zone_entry = ctk.CTkEntry(root, textvariable=zone_entry_text,font=FONT)
    zone_entry.grid(row=0, column=0, sticky='ew')

    zone_button = ctk.CTkButton(root ,fg_color="dark blue",text='Update Zone',font=FONT, command=(lambda: set_zone(resource_dictionary[current_resource_id], zone_entry_text.get())), corner_radius=30)
    zone_button.grid(row=1, column=0, sticky='nesw',pady=10,padx=10)

def create_data_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1), weight=1)

    global source_entry_text
    source_entry_text = ctk.StringVar(value='')
    source_entry = ctk.CTkEntry(root, textvariable=source_entry_text,font=FONT)
    source_entry.grid(row=0, column=0, sticky='ew')

    source_button = ctk.CTkButton( root ,fg_color="dark blue", text='Update Source',font=FONT, command=(lambda: set_source(resource_dictionary[current_resource_id], source_entry_text.get())),corner_radius=30)
    source_button.grid(row=1, column=0, sticky='nesw',pady=10,padx=10)

def create_information_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1), weight=1)

    type_panel = ctk.CTkFrame(root)
    type_panel.grid(row=0, column=0, sticky='nesw')

    type_panel.rowconfigure(0, weight=1)
    type_panel.columnconfigure((0,1,2), weight=1)

    global selected_type
    selected_type = ctk.StringVar()
    def select_checkbox(transformation_type):
        selected_type.set(transformation_type)
        set_transformation_type(resource_dictionary[current_resource_id], transformation_type)

    filter_checkbox = ctk.CTkCheckBox(type_panel, text="filter",variable=selected_type, onvalue='filter', offvalue='', command=(lambda: select_checkbox('filter')))
    filter_checkbox.grid(column=0, row=0, sticky='nesw')
    map_checkbox = ctk.CTkCheckBox(type_panel, text="map",variable=selected_type, onvalue='map', offvalue='', command=(lambda: select_checkbox('map')))
    map_checkbox.grid(column=1, row=0, sticky='nesw')
    reduce_checkbox = ctk.CTkCheckBox(type_panel, text="reduce",variable=selected_type, onvalue='reduce', offvalue='', command=(lambda: select_checkbox('reduce')))
    reduce_checkbox.grid(column=2, row=0, sticky='nesw')

    function_panel = ctk.CTkFrame(root)
    function_panel.grid(row=1, column=0, sticky='nesw')

    function_panel.columnconfigure(0,weight=1)
    function_panel.rowconfigure((0,1),weight=1)

    global function_entry_text
    function_entry_text = ctk.StringVar(value='')
    function_entry = ctk.CTkEntry(function_panel, textvariable=function_entry_text,font=FONT)
    function_entry.grid(row=0, column=0, sticky='ew')

    function_button = ctk.CTkButton(function_panel,fg_color="dark blue", text='Update Function',font=FONT, command=(lambda: set_transformation_function(resource_dictionary[current_resource_id], function_entry_text.get())))
    function_button.grid(row=1, column=0, sticky='nesw',pady=10,padx=10)
