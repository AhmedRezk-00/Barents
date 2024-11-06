import tkinter as tk

def create_canvas(canvas):
    global mainCanvas
    mainCanvas = tk.Canvas(canvas, bg='white', bd=5, relief='ridge')
    canvas.rowconfigure(0, weight=1)
    canvas.columnconfigure(0, weight=1)
    mainCanvas.grid(row=0, column=0, sticky='nesw', pady=5, padx=5)\
    
def create_square():
    mainCanvas.create_rectangle(50, 50, 100, 100, fill="blue")