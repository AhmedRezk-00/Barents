import customtkinter as ctk
from PIL import Image
import src.rdf_manager as rdf_manager
import src.shared_resources
import os
 #load images
path_Source="prototype/frontend/src/images/DataSource.png"
Source="prototype/frontend/src/images/Arrow3.png"
DataSinkPath="prototype/frontend/src/images/DataSink2.png"
Transformations="prototype/frontend/src/images/Transformations.png"

DataSource_image = ctk.CTkImage(light_image=Image.open(path_Source),
                                  dark_image=Image.open(path_Source),
                                  size=(120, 120))

Arrow_Img=ctk.CTkImage(light_image=Image.open(Source),
                                  dark_image=Image.open(Source),
                                  size=(120, 120))
DataSink_Img=ctk.CTkImage(light_image=Image.open(DataSinkPath),
                                  dark_image=Image.open(DataSinkPath),
                                  size=(120, 120))
Transformation_Img=ctk.CTkImage(light_image=Image.open(Transformations),
                                  dark_image=Image.open(Transformations),
                                  size=(120, 120))





# function to create left sidebar
def create_left_sidebar(root):
    # divide left sidebar into grids to grid components
    root.columnconfigure(0, weight=1)

    root.rowconfigure((0,1,2,3), weight=1)

    frame=ctk.CTkFrame(root,fg_color="transparent",bg_color="transparent")
    frame.grid(row=0, column=0, rowspan=4,sticky="nsew",padx=10,pady=10)
    frame.columnconfigure(0,weight=1)
    frame.rowconfigure((0,1,2,3),weight=1)
   
    # button to add generic data level resource
    data_source_button = ctk.CTkButton( frame, text='' ,command=( lambda: add_data_source()), image=DataSource_image,compound="right",fg_color="dark blue",corner_radius=30)
    data_source_button.grid(column=0, row=0, sticky = 'nsew', pady=10)

    # button to add generic knowledge level resource
    data_sink_button = ctk.CTkButton(frame, text='Data Sink',image=DataSink_Img,compound="top",fg_color="dark blue",text_color="deepsky blue3", command=(lambda: add_data_sink()), corner_radius=30)
    data_sink_button.grid(column=0, row=1, sticky='nsew', pady=10)

    # button to add generic information level resource
    transformation_button = ctk.CTkButton( frame,text='Transformation',image=Transformation_Img,compound="top", fg_color="dark blue",text_color="deepsky blue3",command=(lambda: add_transformation()),corner_radius=30)
    transformation_button.grid(column=0, row=2, sticky='nsew', pady=10)

    partOf_button = ctk.CTkButton(frame,text='Part Of Relationship',text_color="deepsky blue3",image=Arrow_Img,compound="top",fg_color="dark blue" ,corner_radius=30)
    partOf_button.grid(column=0, row=3, sticky='nsew', pady=10)


# function to create rectangle to represent data source on canvas and add data source to rdf graph
def add_data_source():
    square = src.shared_resources.canvas.create_rectangle(50, 50, 100, 100, fill='gray30')
    rdf_manager.add_data_source(square)
    name = rdf_manager.get_name(rdf_manager.resource_dictionary[square])
    src.shared_resources.canvas.create_text(75, 110, text=name, tags=f"text_{square}")

# function to add data sink to rdf graph and rectangle to represent it on canvas
def add_data_sink():
    square = src.shared_resources.canvas.create_rectangle(50, 50, 100, 100, fill='olive')
    rdf_manager.add_data_sink(square)
    name = rdf_manager.get_name(rdf_manager.resource_dictionary[square])
    src.shared_resources.canvas.create_text(75, 110, text=name, tags=f"text_{square}")

def add_transformation():
    square = src.shared_resources.canvas.create_rectangle(50, 50, 100, 100, fill='teal')
    rdf_manager.add_transformation(square)
    name = rdf_manager.get_name(rdf_manager.resource_dictionary[square])
    src.shared_resources.canvas.create_text(75, 110, text=name, tags=f"text_{square}")
