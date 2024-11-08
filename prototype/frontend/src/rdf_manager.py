import rdflib as rdf

# initialize graph. changes made to the graph should reflect in the editor.
rdf_graph = rdf.Graph()
# define namespace for rdf_graph thats specific to barents
dl = rdf.Namespace("http://barents.dl/")
rdf_graph.bind("dl", dl)

# function to export rdf_graph as an .xml file 
def export_graph(file_name):
    rdf_graph.serialize(format="xml", destination=file_name + '.xml')