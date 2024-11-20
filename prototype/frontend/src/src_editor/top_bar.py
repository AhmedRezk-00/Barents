import customtkinter as ctk
from src.rdf_manager import export_graph, reset_graph
import src.shared_resources
from tkinter import filedialog
from tkinter.messagebox import askyesno
from PIL import Image


HEADER_FONT = ("Helvetica", 16, "bold")


ImageSource="prototype/frontend/src/images/Barents.png"
Barents_image = ctk.CTkImage(light_image=Image.open(ImageSource),dark_image=Image.open(ImageSource),size=(100, 100))

# function to create top bar widget 
def create_top_bar(root):
    # create grid layout of top_bar
    root.columnconfigure((0,1,2,3,4,5,6,7), weight=1)
    root.rowconfigure(0, weight=1)

    # define an export button that exports the rdf graph as an xml file
    export_button = ctk.CTkButton(root, command=(lambda: export_button_function()), text='Export Graph',font=HEADER_FONT,fg_color="dark blue")
    export_button.grid(row=0, column=0, sticky='nesw')

    # reset button that resets rdf graph and canvas on click
    reset_button = ctk.CTkButton(root, command=(lambda: reset_canvas()), text='Reset graph',fg_color="red",font=HEADER_FONT)
    reset_button.grid(row=0, column=1, sticky='nesw')
    logo_button = ctk.CTkButton(root, text='',fg_color="transparent",font=HEADER_FONT, image=Barents_image,height=100, width= 100,hover=False,border_width=0 )
    logo_button.grid(row=0, column=7, sticky='e')

# function that resets the rdf graph as well as the canvas 
def reset_canvas():
    # open dialog window asking user to confirm deletion 
    if(askyesno(title="BFP-BARENTS: Confirm Deletion",message="Are you sure you want to delete the current graph?")):
        reset_graph()
        src.shared_resources.canvas.delete('all')

# function that opens a dialog window to select where graph is exported to and then exports graph there
def export_button_function():
    export_graph(filedialog.asksaveasfilename(title="Save RDF Graph As", defaultextension=".xml", filetypes=[("RDF/XML File", "*.xml"), ("Turtle", "*.ttl"), ("JSON-LD", "*.jsonld"), ("N-Triples", "*.nt"), ("Notation-3", "*.n3"), ("All Files", "*.*")]), )
