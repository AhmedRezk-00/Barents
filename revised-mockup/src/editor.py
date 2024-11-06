import tkinter as tk

from src.graphManager import testRun

def create_editor(root):
    # Set up grid configuration for layout
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=20)
    root.columnconfigure(2, weight=1)
    root.rowconfigure((0, 1), weight=2)

    # Button to run test graph
    test_button = tk.Button(root, text='run test graph', command=(lambda: testRun()), bg='grey')
    test_button.grid(row=0, column=0, sticky='nesw', pady=5, padx=5)

    # Canvas for drawing squares and enabling drag-and-drop
    mainCanvas = tk.Canvas(root, bg='white', bd=5, relief='ridge')
    mainCanvas.grid(row=0, column=1, sticky='nesw', pady=5, padx=5, rowspan=2)

    # Button to generate a square
    generate_button = tk.Button(root, text="Generate Square", command=(lambda: create_square(mainCanvas)))
    generate_button.grid(row=1, column=0, sticky='nesw', pady=5, padx=5)

    # Bind events for drag-and-drop functionality on the canvas
    mainCanvas.bind("<Button-1>", lambda event: on_square_click(event, mainCanvas))
    mainCanvas.bind("<B1-Motion>", lambda event: on_square_drag(event, mainCanvas))
    mainCanvas.bind("<ButtonRelease-1>", lambda event: on_square_release(event))

    # Initialize global variables to keep track of the current square and its offsets
    global current_square, offset_x, offset_y
    current_square = None
    offset_x = 0
    offset_y = 0

    squareInfo = tk.Frame(root)
    squareInfo.grid(row=0, column=2, sticky='nesw', padx=5, pady=5, rowspan=2)

def create_square(canvas):
    # Set a fixed position and size for the square
    x1, y1, size = 200, 200, 50
    # Draw the square on the canvas
    canvas.create_rectangle(x1, y1, x1 + size, y1 + size, fill="blue")

def on_square_click(event, canvas):
    global current_square, offset_x, offset_y
    # Identify the closest item (square) to the click position
    item = canvas.find_closest(event.x, event.y)
    if item:
        current_square = item  # Store the item for dragging
        # Calculate the offset to maintain square position relative to cursor
        offset_x = event.x - canvas.coords(item)[0]
        offset_y = event.y - canvas.coords(item)[1]

def on_square_drag(event, canvas):
    global current_square
    if current_square:
        # Update the square's position based on the cursor movement
        new_x = event.x - offset_x
        new_y = event.y - offset_y
        canvas.coords(current_square, new_x, new_y, new_x + 50, new_y + 50)

def on_square_release(event):
    global current_square
    # Release the current square once the mouse button is released
    current_square = None