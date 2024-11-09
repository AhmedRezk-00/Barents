import rdflib as rdf

# initialize graph. changes made to the graph should reflect in the editor.
rdf_graph = rdf.Graph()
# define namespace for rdf_graph thats specific to barents
dl = rdf.Namespace("http://barents.dl/")
rdf_graph.bind("dl", dl)

# array that stores all resources created in rdf graph at any given id of items on the canvas
resource_dictionary = []

# variables to store rdf literal of layer information to ensure consistency
knowledge_layer = rdf.Literal("Knowledge Layer")
information_layer = rdf.Literal("Information Layer")
data_layer = rdf.Literal("Data Layer")

# function to export rdf_graph as an .xml file 
def export_graph(file_name):
    rdf_graph.serialize(format="xml", destination=file_name + '.xml')

# function to delete all triples from rdf graph
def reset_graph():
    pass

# function to add data level resource
def add_data_source(id):
    new_resource = 'unnamed_ressource_' + str(id)
    rdf_graph.add((rdf.URIRef(dl + new_resource), dl.layer, data_layer))
    # TODO: add_to_dictionary(id, new_ressource)

# function to add knowledge level resource
def add_data_sink():
    pass

# function to ass information level resource
def add_transformation():
    pass

# function to set type of given transformation
def set_transformation_type():
    pass

# function to set expression that defines given transformation
def set_transformation_expression():
    pass

# function to rename all triples belonging to a given subject
def rename_triples():
    pass

# helper function to ensure new resources are added properly to dictionary
def add_to_dictionary():
    pass

# function that returns the level at which a given resource belongs. 
def return_level():
    pass

# function to set the zone literal of a given knowledge level resource
def set_zone():
    pass

# function to set partof relationship given two resources, with one of them being a information level resource (transformation)
def set_part_of():
    pass

# function to set source literal of a given data level resource
def set_source():
    pass