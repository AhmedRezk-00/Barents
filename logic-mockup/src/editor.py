import tkinter as tk
from src.rdfManager import addDataSource, addDataSink, addTransformation, subject_dictionary, renameTriples, returnLayer, knowledgeLevel, informationLevel, dataLevel
import src.sharedResources

lastClicked = None

def create_editor(root):
    root.rowconfigure(0, weight=1)
    root.columnconfigure((0,2), weight=1)
    root.columnconfigure(1, weight=5)

    # canvas to drag and drop nodes on
    canvas = tk.Canvas(root, background='gray10', relief='solid', highlightbackground = "gray20", highlightcolor= "gray20")
    canvas.grid(row=0, column=1, sticky='nesw', padx=5, pady=5)

    # left sidepanel used for adding new components to canvas
    left_sidepanel = tk.Frame(root, background='gray20', relief='solid', highlightbackground = "gray20", highlightcolor= "gray20")
    left_sidepanel.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)
    left_sidepanel.rowconfigure((0,1,2), weight=1)
    left_sidepanel.columnconfigure(0, weight=1)

    # data source button to add data source ressource to canvas
    dataSource_button = tk.Button(left_sidepanel, background='gray10', relief='solid', text='add generic data source', fg='gray80', command=(lambda:create_source(canvas)))
    dataSource_button.grid(row=0, column=0, sticky='nesw', padx=5, pady=5)

    # data sink button to add data sink ressource to canvas
    dataSink_button = tk.Button(left_sidepanel, background='gray10', relief='solid', text='add generic data sink', fg='gray80', command=(lambda:create_sink(canvas)))
    dataSink_button.grid(row=1, column=0, sticky='nesw', padx=5, pady=5)

    # transformation button to add transformation ressource to canvas
    transformation_button = tk.Button(left_sidepanel, background='gray10', relief='solid', text='add generic transformation', fg='gray80', command=(lambda:create_transformation(canvas)))
    transformation_button.grid(row=2, column=0, sticky='nesw', padx=5, pady=5)

    # right sidepanel used for customizing components of canvas, this is done by adding or changing information of the unerlying rdf
    right_sidepanel = tk.Frame(root, background='gray20', relief='solid', highlightbackground = "gray20", highlightcolor= "gray20")
    right_sidepanel.grid(row=0, column=2, sticky='nesw', padx=5, pady=5)
    right_sidepanel.columnconfigure(0, weight=1)
    right_sidepanel.rowconfigure((0,1,2), weight=1)

    global ressource_info_label, entry_content
    entry_content = tk.StringVar(value="")
    ressource_info_label = tk.Label(right_sidepanel, text='ressource name:', bg='gray20', fg='gray80')
    ressource_info_label.grid(row=0, column=0, sticky='new')
    ressource_entry = tk.Entry(right_sidepanel, textvariable=entry_content)
    ressource_entry.grid(row=0, column=0, sticky='ew')
    ressource_entry_button = tk.Button(right_sidepanel, background='gray10', relief='solid', text='submit subject name', foreground='gray80', command=(lambda:submit_entry()))
    ressource_entry_button.grid(row=0, column=0, sticky='esw')

    global transformation_panel
    transformation_panel = tk.Label(right_sidepanel, text='last clicked transformation') 

    # events for drag and drop, as well as components customization
    # TODO: introduce drag and drop events. first introduce simple renaming to support rdfmanager renametriples()
    canvas.bind('<Button-1>', lambda event: on_click(event, canvas))
    canvas.bind("<B1-Motion>", lambda event: on_drag(event, canvas))
    canvas.bind("<ButtonRelease-1>", lambda event: on_release(event))

    global current_square, offset_x, offset_y
    current_square = None
    offset_x = 0
    offset_y = 0

    src.sharedResources.canvas = canvas


def create_source(canvas):
    square = canvas.create_rectangle(50, 50, 100, 100, fill='gray30')
    addDataSource(square)

def create_sink(canvas):
    square = canvas.create_rectangle(50, 50, 100, 100, fill='blue')
    addDataSink(square)

def create_transformation(canvas):
    square = canvas.create_rectangle(50, 50, 100, 100, fill='red')
    addTransformation(square)

def on_click(event, canvas):
    ressource = canvas.find_closest(event.x, event.y)

    global lastClicked
    lastClicked = ressource[0]
    entry_content.set(subject_dictionary[lastClicked])
    match str(returnLayer(subject_dictionary[lastClicked])):
        case 'Data Layer':
            print('data')
            transformation_panel.grid_forget()
        case 'Knowledge Layer':
            print('knowledge')
            transformation_panel.grid_forget()
        case 'Information Layer':
            print('information')
            transformation_panel.grid(row=1, column=0)


    global current_square, offset_x, offset_y
    current_square = ressource
    offset_x = event.x - canvas.coords(ressource)[0]
    offset_y = event.y - canvas.coords(ressource)[1]

def on_drag(event, canvas):
    global current_square
    if current_square:
        new_x = event.x - offset_x
        new_y = event.y - offset_y
        canvas.coords(current_square, new_x, new_y, new_x + 50, new_y + 50)

def on_release(event):
    global current_square
    current_square = None

def submit_entry():
    renameTriples(subject_dictionary[lastClicked], str(entry_content.get()))
    subject_dictionary[lastClicked] = str(entry_content.get())