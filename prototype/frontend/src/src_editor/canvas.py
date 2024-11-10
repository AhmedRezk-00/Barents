import tkinter as tk 
import src.shared_resources
from src.rdf_manager import resource_dictionary, get_level
from src.src_editor.right_sidebar import update_right_sidebar

# variables to store the last clicked resource
current_resource_id = None
# variables to handle drag and drop
offset_x = 0
offset_y = 0

# function to create canvas of editor. rdf graph resources should be displayed here 
def create_canvas(root):
    # create canvas widget
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight=1)
    canvas = tk.Canvas(root, relief='solid', highlightbackground='black')
    canvas.grid(row=0, column=0, sticky='nesw')

    # define shared_resources.canvas to be this canvas
    src.shared_resources.canvas = canvas

    # events for drag and drop & right sidebar customization 
    canvas.bind('<Button-1>', lambda event: on_click(event, canvas))
    canvas.bind("<B1-Motion>", lambda event: on_drag(event, canvas))
    canvas.bind("<ButtonRelease-1>", lambda event: on_drop(event))

# function to handle on_click event
def on_click(event, canvas):
    global current_resource_id
    # check if theres any items on canvas to drag and drop
    if canvas.find_all():
        current_resource_id = canvas.find_closest(event.x, event.y)[0]
        global offset_x, offset_y
        offset_x = event.x - canvas.coords(current_resource_id)[0]
        offset_y = event.y - canvas.coords(current_resource_id)[1]

        # update right sidebar 
        update_right_sidebar(get_level(resource_dictionary[current_resource_id]))

# function to handle drag event
def on_drag(event, canvas):
    global current_resource_id
    # check if there's any resource selected to drag
    if current_resource_id:
        new_x = event.x - offset_x
        new_y = event.y - offset_y
        canvas.coords(current_resource_id, new_x, new_y, new_x+50, new_y+50)

# function to handle  drop event
def on_drop(event): 
    # NOTE: resetting current_resource_id would also reset right_sidebar selection unless an extra variable is introduced
    pass

# function to return current_resource_id 
def get_current_resource_id():
    return current_resource_id