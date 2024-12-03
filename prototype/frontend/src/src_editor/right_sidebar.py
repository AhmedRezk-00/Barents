import customtkinter as ctk
from src.rdf_manager import rename_triples, resource_dictionary, get_level, set_transformation_type, get_transformation_type, set_transformation_function, get_transformation_function, set_source, set_zone, get_source, get_zone, delete_resource, does_resource_exist
import src.shared_resources

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
FONT = ("Helvetica", 16)
SMALLFONT = ("Helvetica", 12)
BIGFONT = ("Helvetica", 16, "bold")

# function to create right sidebar 
def create_right_sidebar(root):
    # grid right sidebar 
    root.rowconfigure(0, weight=0)
    root.rowconfigure(1, weight=1)
    root.columnconfigure(0, weight=1)

    # header for right sidebar
    header_label = ctk.CTkLabel(root, text='Customize Resource:',font=BIGFONT, fg_color='dark blue')
    header_label.grid(row=0, column=0, sticky='nesw')

    main_frame = ctk.CTkFrame(root, fg_color='dark blue')
    main_frame.grid(column=0, row=1, sticky='nesw')
    main_frame.columnconfigure(0, weight=1)
    main_frame.rowconfigure(0, weight=1)
    main_frame.rowconfigure(1, weight=1)

    # panel present for all resources
    generic_panel = ctk.CTkFrame(main_frame)
    generic_panel.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)
    generic_panel.columnconfigure(0, weight=1)
    generic_panel.rowconfigure((0,1,2,3,4), weight=1)

    # header to group name entry widgets
    name_header = ctk.CTkLabel(generic_panel, text='Customize Resource Name:', font=SMALLFONT, fg_color='blue')
    name_header.grid(row=0, column=0, sticky= 'ew')

    # entry field for changing resource names
    global name_entry_text
    name_entry_text = ctk.StringVar(value='')
    resource_name_entry = ctk.CTkEntry(generic_panel, textvariable=name_entry_text,font=FONT)
    resource_name_entry.grid(row=1, column=0, sticky='ew')

    # button for changing resource names
    resource_name_button = ctk.CTkButton(generic_panel, fg_color="blue", text='Update Name',font=FONT, command=(lambda: submit_resource_name()),corner_radius=30)
    resource_name_button.grid(row=2, column=0, sticky='nesw',pady=10,padx=10)

    # header to group delete resource widgets
    delete_header = ctk.CTkLabel(generic_panel, text='Delete Resource:', font=SMALLFONT, fg_color='blue')
    delete_header.grid(row=3, column=0, sticky= 'ew')

    # button for deleting resource
    delete_button = ctk.CTkButton(generic_panel, fg_color="blue", text='Delete resource',font=FONT, command=(lambda: delete_function()),corner_radius=30)
    delete_button.grid(row=4, column=0, sticky='nesw',pady=10,padx=10)

    # panel that changes based on what layer a selected resource belongs to
    layer_specific_panel = ctk.CTkFrame(main_frame)
    layer_specific_panel.grid(row=1, column=0, sticky='nesw',padx=5, pady=5)
    layer_specific_panel.columnconfigure(0, weight=1)
    layer_specific_panel.rowconfigure(0, weight=1)

    # panels that will be loaded dynamically based on what layer selected resource belongs to 
    global knowledge_layer_panel, information_layer_panel, data_layer_panel
    knowledge_layer_panel = ctk.CTkFrame(layer_specific_panel)
    create_knowledge_layer_panel(knowledge_layer_panel)
    information_layer_panel = ctk.CTkFrame(layer_specific_panel)
    create_information_layer_panel(information_layer_panel)
    data_layer_panel = ctk.CTkFrame(layer_specific_panel)
    create_data_layer_panel(data_layer_panel)

# function to update right sidebar (the layer_specific_panel) based on selected resource
def update_right_sidebar(resource_id):
    global current_resource_id
    current_resource_id = resource_id
    # update name entry field 
    name_entry_text.set(resource_dictionary[current_resource_id])

    #dynamically load layer_specific_panel depending on what layer resource belongs to 
    match get_level(resource_dictionary[resource_id]):
        case "Knowledge Layer":
            knowledge_layer_panel.grid(row=0, column=0, sticky='nesw')
            information_layer_panel.grid_forget()
            data_layer_panel.grid_forget()
            # update zone entry text
            zone_entry_text.set(get_zone(resource_dictionary[current_resource_id]))
        case "Information Layer":
            knowledge_layer_panel.grid_forget()
            information_layer_panel.grid(row=0, column=0, sticky='nesw')
            data_layer_panel.grid_forget()
            #update transformation type 
            transformation_type = get_transformation_type(resource_dictionary[current_resource_id])
            selected_type.set(transformation_type)
            # update function entry text
            function_entry = get_transformation_function(resource_dictionary[current_resource_id])
            function_entry_text.set(function_entry)
        case "Data Layer":
            knowledge_layer_panel.grid_forget()
            information_layer_panel.grid_forget()
            data_layer_panel.grid(row=0, column=0, sticky='nesw')
            # update source entry text
            source_entry_text.set(get_source(resource_dictionary[current_resource_id]))
    
# function of button when renaming triples
def submit_resource_name():
    if current_resource_id:
        if not does_resource_exist(str(name_entry_text.get())):
            rename_triples(resource_dictionary[current_resource_id], str(name_entry_text.get()))
            resource_dictionary[current_resource_id] = str(name_entry_text.get())
            text = src.shared_resources.canvas.find_withtag(f"tag:{current_resource_id}")
            if text:
                src.shared_resources.canvas.itemconfig(text[0], text=str(name_entry_text.get()))
        else:
            print('right_sidebar: submit_resource_name: new name already in graph')

# function to create panel specific to knowledge level resource
def create_knowledge_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1,2), weight=1)

    # header to group zone entry widgets
    name_header = ctk.CTkLabel(root, text='Customize data zone:', font=SMALLFONT, fg_color='blue')
    name_header.grid(row=0, column=0, sticky= 'ew')

    # zone entry field to change zone literal of selected resource
    global zone_entry_text
    zone_entry_text = ctk.StringVar(value='')
    zone_entry = ctk.CTkEntry(root, textvariable=zone_entry_text,font=FONT)
    zone_entry.grid(row=1, column=0, sticky='ew')
    # button to update zone based on entered zone of currently selected resource
    zone_button = ctk.CTkButton(root ,fg_color="blue",text='Update Zone',font=FONT, command=(lambda: set_zone(resource_dictionary[current_resource_id], zone_entry_text.get())), corner_radius=30)
    zone_button.grid(row=2, column=0, sticky='nesw',pady=10,padx=10)

# functioon to create panel specific to data level resource
def create_data_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1,2), weight=1)

    # header to group zone entry widgets
    name_header = ctk.CTkLabel(root, text='Customize data source:', font=SMALLFONT, fg_color='blue')
    name_header.grid(row=0, column=0, sticky= 'ew')
    # source entry field to change source literal of selected resource
    global source_entry_text
    source_entry_text = ctk.StringVar(value='')
    source_entry = ctk.CTkEntry(root, textvariable=source_entry_text,font=FONT)
    source_entry.grid(row=1, column=0, sticky='ew')
    # button to update selected resources source literal based on entered text
    source_button = ctk.CTkButton( root ,fg_color="blue", text='Update Source',font=FONT, command=(lambda: set_source(resource_dictionary[current_resource_id], source_entry_text.get())),corner_radius=30)
    source_button.grid(row=2, column=0, sticky='nesw',pady=10,padx=10)

# function to create panel specific to information layer resource
def create_information_layer_panel(root):
    root.columnconfigure(0, weight=1)
    root.rowconfigure((0,1,2,3), weight=1)


    # header to group type entry widgets
    type_header = ctk.CTkLabel(root, text='Customize Transformation Type:', font=SMALLFONT, fg_color='blue')
    type_header.grid(row=0, column=0, sticky= 'ew')

    # panel to change transformation type of selected resource 
    type_panel = ctk.CTkFrame(root)
    type_panel.grid(row=1, column=0, sticky='nesw')

    type_panel.rowconfigure(0, weight=1)
    type_panel.columnconfigure((0,1,2), weight=1)

    global selected_type
    selected_type = ctk.StringVar()
    # function to manage checkboxes to select transfomation type 
    def select_checkbox(transformation_type):
        selected_type.set(transformation_type)
        set_transformation_type(resource_dictionary[current_resource_id], transformation_type)

    # checkboxes to select transformation type of selected resource
    filter_checkbox = ctk.CTkCheckBox(type_panel, text="filter",variable=selected_type, onvalue='filter', offvalue='', command=(lambda: select_checkbox('filter')))
    filter_checkbox.grid(column=0, row=0, sticky='nesw')
    map_checkbox = ctk.CTkCheckBox(type_panel, text="map",variable=selected_type, onvalue='map', offvalue='', command=(lambda: select_checkbox('map')))
    map_checkbox.grid(column=1, row=0, sticky='nesw')
    reduce_checkbox = ctk.CTkCheckBox(type_panel, text="reduce",variable=selected_type, onvalue='reduce', offvalue='', command=(lambda: select_checkbox('reduce')))
    reduce_checkbox.grid(column=2, row=0, sticky='nesw')


    # header to group function entry widgets
    function_header = ctk.CTkLabel(root, text='Enter Function Expression:', font=SMALLFONT, fg_color='blue')
    function_header.grid(row=2, column=0, sticky= 'ew')

    # panel to change function text of selected resource
    function_panel = ctk.CTkFrame(root)
    function_panel.grid(row=3, column=0, sticky='nesw')

    function_panel.columnconfigure(0,weight=1)
    function_panel.rowconfigure((0,1),weight=1)

    # entry field to change function text of selected resource 
    global function_entry_text
    function_entry_text = ctk.StringVar(value='')
    function_entry = ctk.CTkEntry(function_panel, textvariable=function_entry_text,font=FONT)
    function_entry.grid(row=0, column=0, sticky='ew')
    # button to change function text of selected resource
    function_button = ctk.CTkButton(function_panel,fg_color="blue", text='Update Function',font=FONT, command=(lambda: set_transformation_function(resource_dictionary[current_resource_id], function_entry_text.get())))
    function_button.grid(row=1, column=0, sticky='nesw',pady=10,padx=10)

def delete_function():
    src.shared_resources.canvas.delete(current_resource_id)
    delete_resource(current_resource_id)
    for id in src.shared_resources.canvas.find_withtag(f"tag:{current_resource_id}"):
        src.shared_resources.canvas.delete(id)