import customtkinter as ctk
from PIL import Image, ImageTk
import src.rdf_manager as rdf_manager
import src.shared_resources
import os
 #load images
path_Source="prototype/frontend/src/images/DataSource.png"
Source="prototype/frontend/src/images/Arrow3.png"
DataSinkPath="prototype/frontend/src/images/DataSink.png"
Transformations="prototype/frontend/src/images/Transformations.png"

# set image variables 
DataSource_image = ctk.CTkImage(light_image=Image.open(path_Source),
                                  dark_image=Image.open(path_Source),
                                  size=(100, 100))

Arrow_Img=ctk.CTkImage(light_image=Image.open(Source),
                                  dark_image=Image.open(Source),
                                  size=(80, 80))
DataSink_Img=ctk.CTkImage(light_image=Image.open(DataSinkPath),
                                  dark_image=Image.open(DataSinkPath),
                                  size=(60, 70))
Transformation_Img=ctk.CTkImage(light_image=Image.open(Transformations),
                                  dark_image=Image.open(Transformations),
                                  size=(60, 60))
#function that resizes the images to be able to appear on the canvas
def canvas_images():
    global DataSource_Canvas, DataSink_canvas, Transformation_Canvas
    DataSource_Canvas = ImageTk.PhotoImage(Image.open(path_Source).resize((100, 100)))
    DataSink_canvas =ImageTk.PhotoImage(Image.open(DataSinkPath).resize((75, 75)))
    Transformation_Canvas =ImageTk.PhotoImage(Image.open(Transformations).resize((75, 75)))


# function to create left sidebar
def create_left_sidebar(root):
    #canvas ImaSges
    canvas_images() 
    # divide left sidebar into grids to grid components
    root.columnconfigure(0, weight=1)

    root.rowconfigure((0,1,2,3), weight=1)

    # man frame of left sidebar to grid other elements
    frame=ctk.CTkFrame(root,fg_color="#2b2b2b",bg_color="transparent")
    frame.grid(row=0, column=0, rowspan=4,sticky="nsew",padx=10,pady=10)
    frame.columnconfigure(0,weight=1)
    frame.rowconfigure((0,1,2,3),weight=1)
   
    # button to add generic data level resource
    data_source_button = ctk.CTkButton( frame, text='' ,command=( lambda: add_data_source()), image=DataSource_image,compound="right",fg_color="#333333", hover_color="#4a90e2",corner_radius=30)
    data_source_button.grid(column=0, row=0, sticky = 'nsew', pady=10)

    # button to add generic knowledge level resource
    data_sink_button = ctk.CTkButton(frame, text='Data Sink',image=DataSink_Img,compound="top",fg_color="#333333",font=("Helvetica", 12), command=(lambda: add_data_sink()), hover_color="#4a90e2", corner_radius=30)
    data_sink_button.grid(column=0, row=2, sticky='nsew', pady=10)

    # button to add generic information level resource
    transformation_button = ctk.CTkButton( frame,text='Transformation',image=Transformation_Img,compound="top", fg_color="#333333",command=(lambda: add_transformation()),hover_color="#4a90e2",font=("Helvetica", 12),corner_radius=30)
    transformation_button.grid(column=0, row=1, sticky='nsew', pady=10)

    # button to add partof relationships. currently non functional
    global part_of_button
    part_of_button = ctk.CTkButton(frame,text='Set Part Of Relationships',image=Arrow_Img,compound="top",fg_color="#333333", command=(lambda: toggle_part_of()),hover_color="#4a90e2" ,font=("Helvetica", 12),corner_radius=30)
    part_of_button.grid(column=0, row=3, sticky='nsew', pady=10)

# function to creates data source and adds its corresponding image to the canvas 
def add_data_source():
    DataSource_x1 = src.shared_resources.canvas.canvasx(200)
    DataSource_y1 = src.shared_resources.canvas.canvasy(150)
    DataSource = src.shared_resources.canvas.create_image(DataSource_x1, DataSource_y1, tags='resource',image=DataSource_Canvas)
    rdf_manager.add_data_source(DataSource)
    name = rdf_manager.resource_dictionary[DataSource]
    src.shared_resources.canvas.create_text(DataSource_x1, DataSource_y1+60, text=name, tags=f"tag:{DataSource}")

# function to add data sink to rdf graph and and a corresponding image to represent it on canvas
def add_data_sink():
    DataSink_x1 = src.shared_resources.canvas.canvasx(200)
    DataSink_y1 = src.shared_resources.canvas.canvasy(450)
    DataSink = src.shared_resources.canvas.create_image(DataSink_x1, DataSink_y1,image=DataSink_canvas,tags='resource')
    rdf_manager.add_data_sink(DataSink)
    name = rdf_manager.resource_dictionary[DataSink]
    src.shared_resources.canvas.create_text(DataSink_x1, DataSink_y1+60, text=name, tags=f"tag:{DataSink}")

# function to add transformation to rdf graph and a corresponding image to represent it on canvas
def add_transformation():
    Transformation_x1 = src.shared_resources.canvas.canvasx(200)
    Transformation_y1 = src.shared_resources.canvas.canvasy(300)
    Transformation = src.shared_resources.canvas.create_image(Transformation_x1, Transformation_y1,image=Transformation_Canvas,tags='resource')
    rdf_manager.add_transformation(Transformation)
    name = rdf_manager.resource_dictionary[Transformation]
    src.shared_resources.canvas.create_text(Transformation_x1, Transformation_y1+60, text=name, tags=f"tag:{Transformation}")

# function to enter part_of mode, changes color of canvas, and show instructions
def toggle_part_of():  
    src.shared_resources.part_of_set = set()
    if src.shared_resources.editor_mode == 'part_of':
        src.shared_resources.canvas.config(bg='white')
        src.shared_resources.set_editor_mode('default')
        part_of_button.configure(text='Set Part Of Relationships')
        src.shared_resources.canvas.delete('text_for_canvas_1')
        src.shared_resources.canvas.delete('text_for_canvas_2')
    else:
        src.shared_resources.set_editor_mode('part_of')
        src.shared_resources.canvas.config(bg='lightblue')
        part_of_button.configure(text='Exit Part Of Mode')
        text_canvas_1="\nPossible Combinations:\nData Source-->Transformation\nTransformation-->Data Sink\nData Sink-->Transformation"
        src.shared_resources.canvas.create_text(800,675,text=text_canvas_1, fill='black', font=("Helvetica", 14), tags='text_for_canvas_1')
        text_canvas_2="Click on items to establish 'part of' relationships."
        src.shared_resources.canvas.create_text(475,70,text=text_canvas_2, fill='black', font=("Helvetica", 14), tags='text_for_canvas_2')