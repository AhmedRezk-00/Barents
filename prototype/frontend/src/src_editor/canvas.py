import tkinter as tk 
import customtkinter as ctk
import src.shared_resources
from src.src_editor.right_sidebar import update_right_sidebar
import src.rdf_manager as rdf_manager
from src.src_editor.left_sidebar import toggle_part_of

# variables to store the last clicked resource
current_resource_id = None
# variables to handle drag and drop
offset_x = 0
offset_y = 0

lines = {}
lines_swapped = {}  #(line,boolean)-list

# function to create canvas of editor. rdf graph resources should be displayed here 
def create_canvas(root):
    # create canvas widget
    root.columnconfigure(0, weight = 1)
    root.columnconfigure(1, weight=0)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=0)
    # create canvas with scrollregion which sort of defines minimum size of canvas 
    canvas = tk.Canvas(root, relief='solid', highlightbackground='black',
                       scrollregion=(0, 0, 2400, 2400)) 
    canvas.grid(row=0, column=0, sticky='nesw')


    # add buttons to change scrollregion horizontally
    horizontal_frame = ctk.CTkFrame(root, height=50)
    horizontal_frame.grid(row=1, column=0, sticky='nesw')
    horizontal_frame.grid_propagate(False)
    horizontal_frame.columnconfigure((0,1), weight=1)
    horizontal_frame.rowconfigure((0,1), weight=1)
    horizontal_increase_button = ctk.CTkButton(horizontal_frame, text='+', command=lambda: horizontal_scrollregion(canvas, 'increase'), width=100, height=10)
    horizontal_increase_button.grid(row=1, column=1, pady=5)
    horizontal_decrease_button = ctk.CTkButton(horizontal_frame, text='-', command=lambda: horizontal_scrollregion(canvas, 'decrease'), width=100, height=10)
    horizontal_decrease_button.grid(row=1, column=0, pady=5)
    x_scroll = tk.Scrollbar(horizontal_frame, orient='horizontal', command=canvas.xview)
    x_scroll.grid(row=0, column=0, sticky='nesw', columnspan=2)

    # add buttons to change scrollregion vertically
    vertical_frame = ctk.CTkFrame(root, width=50)
    vertical_frame.grid(row=0, column=1, sticky='nesw')
    vertical_frame.grid_propagate(False)
    vertical_frame.columnconfigure((0,1), weight=1)
    vertical_frame.rowconfigure((0,1), weight=1)
    vertical_increase_button = ctk.CTkButton(vertical_frame, text='+', command=lambda: vertical_scrollregion(canvas, 'increase'), width=10, height=100)
    vertical_increase_button.grid(row=1, column=1, padx=5)
    vertical_decrase_button = ctk.CTkButton(vertical_frame, text='-', command=lambda: vertical_scrollregion(canvas, 'decrease'), width=10, height=100)
    vertical_decrase_button.grid(row=0, column=1, padx=5)
    y_scroll = tk.Scrollbar(vertical_frame, orient='vertical', command=canvas.yview)
    y_scroll.grid(row=0, column=0, sticky='nesw', rowspan=2)

    canvas.config(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

    # define shared_resources.canvas to be this canvas
    src.shared_resources.canvas = canvas

    # events for drag and drop & right sidebar customization 
    canvas.bind('<Button-1>', lambda event: on_click(event, canvas))
    canvas.bind("<B1-Motion>", lambda event: on_drag(event, canvas))
    canvas.bind("<ButtonRelease-1>", lambda event: on_drop(event))

    canvas.config(scrollregion=canvas.bbox('all'))

#function to change canvas scrollregion horizontally
def horizontal_scrollregion(canvas, type):
    x1, y1, x2, y2 = canvas.cget("scrollregion").split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    if type=='increase':
        x2 = x2+1000
    if type=='decrease':
        x2 = x2-1000

        items = canvas.find_all()
        if items:
            bbox = canvas.bbox(*items)
            x2 = max(x2, bbox[2]+100)
        x2 = max(x2, 450)

    canvas.config(scrollregion=(x1,y1,x2,y2))

    canvas.config(scrollregion=(x1,y1,x2,y2))

#function to change canvas scrollregion horizontally
def vertical_scrollregion(canvas, type):
    x1, y1, x2, y2 = canvas.cget("scrollregion").split()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

    if type=='increase':
        y2 = y2+1000
    if type=='decrease':
        y2 = y2-1000
        
        items = canvas.find_all()
        if items:
            bbox = canvas.bbox(*items)
            y2 = max(y2, bbox[3]+100)
        y2 = max(y2, 450)
        print(y2)

    canvas.config(scrollregion=(x1,y1,x2,y2))

# function to handle on_click event
def on_click(event, canvas):
    global current_resource_id
    if(src.shared_resources.editor_mode == 'default'):
        default_on_click(event, canvas) 
    if(src.shared_resources.editor_mode == 'part_of'):
        canvas_x = canvas.canvasx(event.x)
        canvas_y = canvas.canvasy(event.y)
        if canvas.find_overlapping(canvas_x, canvas_y, canvas_x, canvas_y):
            current_resource_id = canvas.find_overlapping(canvas_x, canvas_y, canvas_x, canvas_y)[0]
            if 'resource' in canvas.gettags(current_resource_id):
                src.shared_resources.part_of_set.add(current_resource_id)
                if len(src.shared_resources.part_of_set) > 1:
                    id1, id2 = list(src.shared_resources.part_of_set)[0], list(src.shared_resources.part_of_set)[1]
                    if not ((id1, id2) in lines or (id2, id1) in lines) :
                        swap = rdf_manager.swap(id1, id2, current_resource_id) 
                        rdf_manager.set_part_of(id1, id2) 
                        if (swap == "swap"):
                            # arrow ends at second resource
                            Coords1 = canvas.coords(id2)
                            Coords2 = canvas.coords(id1)
                        elif (swap == "dont swap"):
                            # yrrow ends at first resource
                            Coords1 = canvas.coords(id1)
                            Coords2 = canvas.coords(id2)
                        if(swap == "swap" or swap == "dont swap"):
                            x1, y1 = Coords1[0] + 25, Coords1[1] + 25  
                            x2, y2 = Coords2[0] + 25, Coords2[1] + 25  
                            line = canvas.create_line(x1, y1, x2, y2, fill="black", width=2, arrow="last", tags=f"line tag:{id2} tag:{id1}")
                            lines[(id1, id2)] = line
                            lines_swapped[line] = True
                    src.shared_resources.part_of_set = set()
        else:
            toggle_part_of()
            current_resource_id = None
    else:
        pass
    
def default_on_click(event, canvas):
    global current_resource_id
    # check if theres any items on canvas to drag and drop
    canvas_x = canvas.canvasx(event.x)
    canvas_y = canvas.canvasy(event.y)
    if canvas.find_overlapping(canvas_x, canvas_y, canvas_x, canvas_y):
        current_resource_id = canvas.find_overlapping(canvas_x, canvas_y, canvas_x, canvas_y)[0]
        if 'resource' in canvas.gettags(current_resource_id):
            global offset_x, offset_y
            offset_x = event.x - canvas.coords(current_resource_id)[0]
            offset_y = event.y - canvas.coords(current_resource_id)[1]

            # update right sidebar 
            update_right_sidebar(current_resource_id)
        if 'line' in canvas.gettags(current_resource_id):
            id1, id2 = None, None
            for (resource1, resource2), line_id in lines.items():
                if line_id == current_resource_id:
                    id1, id2 = resource1, resource2
            if id1 and id2:
                del lines[(id1, id2)]
                rdf_manager.delete_part_of(id1, id2)
            canvas.delete(current_resource_id)
    else:
        current_resource_id = None

# function to handle drag event
def on_drag(event, canvas):
    if(src.shared_resources.editor_mode == 'default'):
        default_on_drag(event, canvas) 
    else:
        pass

def default_on_drag(event, canvas):
    global current_resource_id
    # check if there's any resource selected to drag
    if current_resource_id:
        if 'resource' in canvas.gettags(current_resource_id):
            new_x = event.x - offset_x
            new_y = event.y - offset_y

            #issue12: new_x and new_y have to be within canvas
            new_x = moveIntoCanvasX(canvas, new_x, canvas.canvasx(canvas.winfo_width()));
            new_y = moveIntoCanvasY(canvas, new_y, canvas.canvasy(canvas.winfo_height()));

            canvas.coords(current_resource_id, new_x, new_y, new_x+50, new_y+50)
            text = canvas.find_withtag(f"tag:{current_resource_id}")
            if text:
                canvas.coords(text[0], new_x+25, new_y+60)

            for (id1, id2), line in lines.items():
                if id1 == current_resource_id or id2 == current_resource_id:
                    coords1 = canvas.coords(id1)
                    coords2 = canvas.coords(id2)
                    if lines_swapped[line]==True:
                        x1, y1 = coords2[0]+25, coords2[1]+25 
                        x2, y2 = coords1[0]+25, coords1[1]+25 
                    if lines_swapped[line]==False:
                        x1, y1 = coords1[0]+25, coords1[1]+25 
                        x2, y2 = coords2[0]+25, coords2[1]+25 
                    canvas.coords(line, x1, y1, x2, y2)

#issue12: checks and potentially moves data_source-x-value within canvas-borders
def moveIntoCanvasX(canvas, new_x, max_width):
    #border-x-values 
    #800x450 canvas (frontend.py); radius=25 (left_sidebar.add_data_source)
    left_border = canvas.canvasx(0)
    right_border = max_width

    #checks (and updates) x
    if new_x < left_border: 
        return left_border
    elif new_x+50 > right_border:   
       return right_border-50
    else: return new_x

# checks and potentially moves data_source-y-value within canvas-borders
def moveIntoCanvasY(canvas, new_y, max_height):
    #border-y-values
    #800x450 canvas (frontend.py); radius=25 (left_sidebar.add_data_source)
    upper_border = canvas.canvasy(0)
    lower_border = max_height

    #checks (and updates) y
    if new_y+50 > lower_border: 
        return lower_border-50
    elif new_y < upper_border: 
        return upper_border
    else: return new_y

# function to handle  drop event
def on_drop(event):
    if(src.shared_resources.editor_mode == 'default'):
        default_on_drop(event) 
    else:
        pass

def default_on_drop(event): 
    # NOTE: resetting current_resource_id would also reset right_sidebar selection unless an extra variable is introduced
    pass

# function to return current_resource_id 
def get_current_resource_id():
    return current_resource_id