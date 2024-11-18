import tkinter as tk 
import src.shared_resources
from src.src_editor.right_sidebar import update_right_sidebar
from screeninfo import get_monitors     #issue12: to get screen size


# variables to store the last clicked resource
current_resource_id = None
# variables to handle drag and drop
offset_x = 0
offset_y = 0

#issue12: get screen size
monitor_details = get_monitors();
canvas_width = monitor_details[0].width;
canvas_height = monitor_details[0].height;

# function to create canvas of editor. rdf graph resources should be displayed here 
def create_canvas(root):
    # create canvas widget
    root.columnconfigure(0, weight = 1)
    root.rowconfigure(0, weight=1)
    canvas = tk.Canvas(root,width=800, height=450, relief='solid', highlightbackground='black',
                       scrollregion=(0, 0, 800, 450)) #issue12
    canvas.grid(row=0, column=0)#, sticky='nesw')
    print("Canvas width: "+ str(canvas.winfo_reqwidth()));
    print("Canvas height: "+ str(canvas.winfo_reqheight()));

    #issue12: add scrollbar
    y_scroll = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
    y_scroll.grid(row=0, column=1, sticky='ns')
    x_scroll = tk.Scrollbar(root, orient='horizontal', command=canvas.xview)
    x_scroll.grid(row=1, column=0, sticky='ew')
    canvas.config(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

    # define shared_resources.canvas to be this canvas
    src.shared_resources.canvas = canvas

    # events for drag and drop & right sidebar customization 
    canvas.bind('<Button-1>', lambda event: on_click(event, canvas))
    canvas.bind("<B1-Motion>", lambda event: on_drag(event, canvas))
    canvas.bind("<ButtonRelease-1>", lambda event: on_drop(event))

    canvas.config(scrollregion=canvas.bbox('all'))#issue12

# function to handle on_click event
def on_click(event, canvas):
    global current_resource_id
    # check if theres any items on canvas to drag and drop
    canvas_x = canvas.canvasx(event.x)
    canvas_y = canvas.canvasy(event.y)
    if canvas.find_overlapping(canvas_x, canvas_y, canvas_x, canvas_y):
    #if canvas.find_overlapping(event.x, event.y, event.x, event.y):
        current_resource_id = canvas.find_overlapping(canvas_x, canvas_y, canvas_x, canvas_y)[0]
        global offset_x, offset_y
        offset_x = event.x - canvas.coords(current_resource_id)[0]
        offset_y = event.y - canvas.coords(current_resource_id)[1]

        # update right sidebar 
        update_right_sidebar(current_resource_id)
    else:
        current_resource_id = None

# function to handle drag event
def on_drag(event, canvas):
    global current_resource_id
    # check if there's any resource selected to drag
    if current_resource_id:
        new_x = event.x - offset_x;
        new_y = event.y - offset_y;

        #issue12: new_x and new_y have to be within canvas
        new_x = moveIntoCanvasX(new_x);
        new_y = moveIntoCanvasY(new_y);

        canvas.coords(current_resource_id, new_x, new_y, new_x+50, new_y+50)

#issue12: checks and potentially moves data_source-x-value within canvas-borders
def moveIntoCanvasX(new_x):
    #border-x-values 
    #800x450 canvas (frontend.py); radius=25 (left_sidebar.add_data_source)
    left_border = 0;
    right_border = 800;

    #checks (and updates) x
    if new_x < left_border: 
        print("outside left border"); 
        #print("coords x: " + str(new_x) + " , " + str(new_y)); 
        return left_border;
    elif new_x+50 > right_border:   
       print("outside right border"); 
       #print("coords x: " + str(new_x) + " , " + str(new_y)); 
       return right_border-50;
    else: return new_x;

# checks and potentially moves data_source-y-value within canvas-borders
def moveIntoCanvasY(new_y):
    #border-y-values
    #800x450 canvas (frontend.py); radius=25 (left_sidebar.add_data_source)
    upper_border = 0;
    lower_border = 450;

    #checks (and updates) y
    if new_y+50 > lower_border: 
        print("outside lower border"); 
        #print("coords: " + str(new_x) + " , " + str(new_y));
        return lower_border-50;
    elif new_y < upper_border: 
        print("outside upper border"); 
        #print("coords: " + str(new_x) + " , " + str(new_y)); 
        return upper_border;
    else: return new_y;

# function to handle  drop event
def on_drop(event): 
    # NOTE: resetting current_resource_id would also reset right_sidebar selection unless an extra variable is introduced
    pass

# function to return current_resource_id 
def get_current_resource_id():
    return current_resource_id
