import tkinter as tk
from src.graphManager import *
from src.leftSidebar.dataSourcePanel import create_dataSource_panel
from src.leftSidebar.dataSinkPanel import create_dataSink_panel
from src.leftSidebar.transformationPanel import create_transformation_panel

def create_leftSidebar(left_sidebar):
    left_sidebar.columnconfigure(0, weight=1)
    left_sidebar.rowconfigure((0,1,2), weight=1)

    transformation_panel = tk.Frame(left_sidebar, bd=1, relief="solid")
    transformation_panel.grid(row=1, column=0, sticky='nesw')
    create_transformation_panel(transformation_panel)
    

    dataSink_panel = tk.Frame(left_sidebar, bd=1, relief="solid")
    dataSink_panel.grid(row=2, column=0, sticky='nesw')
    create_dataSink_panel(dataSink_panel)

    dataSource_panel = tk.Frame(left_sidebar, bd=1, relief="solid")
    dataSource_panel.grid(row=0, column=0, sticky='nesw')
    create_dataSource_panel(dataSource_panel)