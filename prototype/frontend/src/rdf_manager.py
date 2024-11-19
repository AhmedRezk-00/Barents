import rdflib as rdf

# initialize graph. changes made to the graph should reflect in the editor.
rdf_graph = rdf.Graph()
# define and bind namespace for rdf_graph thats specific to barents
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
    if file_name:
        rdf_graph.serialize(format="xml", destination=file_name)

# function to delete all triples from rdf graph
def reset_graph():
    global rdf_graph
    # graph is deleted and initialized again 
    del rdf_graph
    rdf_graph = rdf.Graph()
    rdf_graph.bind("dl", dl)

# function to add data level resource. id will be the unique id given to the respective canvas item
def add_data_source(id):
    new_resource = 'source_resource_' + str(id)
    rdf_graph.add((rdf.URIRef(dl + new_resource), dl.layer, data_layer))
    add_to_dictionary(id, new_resource)

# function to add knowledge level resource. id will be the unique id given to the respective canvas item
def add_data_sink(id):
    new_resource = 'sink_resource_' + str(id)
    rdf_graph.add((rdf.URIRef(dl + new_resource), dl.layer, knowledge_layer))
    add_to_dictionary(id, new_resource)

# function to ass information level resource. id will be the unique id given to the respective canvas item
def add_transformation(id):
    new_resource = 'transformation_resource_' + str(id)
    rdf_graph.add((rdf.URIRef(dl + new_resource), dl.layer, information_layer))
    add_to_dictionary(id, new_resource)

# function to set type of given transformation. 
def set_transformation_type(resource, transformation_type):
    # check if given resource is a transformation 
    if get_level(resource) == information_layer.value:
        rdf_graph.set((rdf.URIRef(dl + resource), dl.type, rdf.Literal(transformation_type)))
    else:
        print('rdf_manager: set_transformation_type: unexpected resource given, it doesnt match the information layer')

# function to set function that defines given transformation
def set_transformation_function(resource, transformation_function):
    # check if given resource is a transformation 
    if get_level(resource) == information_layer.value:
        rdf_graph.set((rdf.URIRef(dl + resource), dl.function, rdf.Literal(transformation_function)))
    else:
        print('rdf_manager: set_transformation_function: unexpected resource given, it doesnt match the information layer')

# function to rename all triples belonging to a given resource
def rename_triples(resource_name, new_name):
    for s, p, o in rdf_graph.triples((rdf.URIRef(dl + resource_name), None, None)):
        # TODO: add check if new_name is available
        # remove all triples with old resource name
        rdf_graph.remove((s,p,o))
        # re-add all triples with new name of resource
        rdf_graph.add((rdf.URIRef(dl + new_name),p,o))
    # TODO: add code to rename triples where the given resource appears as an object instead of subject

# helper function to ensure new resources are added properly to dictionary
# resource should be the string of the URIRef starting after the dl namespace
def add_to_dictionary(id, resource):
    if len(resource_dictionary) <= id:
        resource_dictionary.extend([None] * (id - len(resource_dictionary) + 1))
    resource_dictionary[id] = resource

# function that returns the level at which a given resource belongs. 
def get_level(resource):
    if(resource):
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.layer):
            return str(o)
    else:
        print('rdf_manager: get_level: parameter is none')

# function to return the type of a transformation, if given resource is a transformation
def get_transformation_type(resource):
    # check if given resource is a transformation
    if get_level(resource) == information_layer.value:
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.type):
            return str(o)
    else:
        print('rdf_manager: get_transformation_type: unexpected resource given, it doesnt match the information layer')
        
# function to return function of a given transformation, if given resource is a transformation 
def get_transformation_function(resource):
    # check if given resource is a transformation
    if get_level(resource) == information_layer.value:
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.function):
            return str(o)
    else:
        print('rdf_manager: get_transformation_function: unexpected resource given, it doesnt match the information layer')

# function to set the zone literal of a given knowledge level resource
def set_zone(resource, zone):
    # TODO: possibly implement check to see if resource belongs to knowledge level
    rdf_graph.set((rdf.URIRef(dl + resource), dl.zone, rdf.Literal(zone)))

# function to return data zone of a given data sink, if given resource is a data sink
def get_zone(resource):
    # check if given resource is a data sink 
    if get_level(resource) == knowledge_layer.value:
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.zone):
            return str(o)
    else:
        print('rdf_manager: get_zone: unexpected resource given, it doesnt match the knowledge layer')

# function to set partof relationship given two resources, with one of them being a information level resource (transformation)
def set_part_of(subject, object):
    # check if exactly one of the given resources is a transformatiion 
    if get_level(subject) == information_layer ^ get_level(object) == information_layer:
        rdf_graph.set((rdf.URIRef(dl + subject), dl.zone, rdf.Literal(object)))
    else:
        print('rdf_manager: set_part_of: unexpected parameters: exactly one resource most belong to the information layer')

# function to set source literal of a given data level resource
def set_source(resource, source):
    # TODO:  possibly check if resource belongs to data level
    rdf_graph.set((rdf.URIRef(dl + resource), dl.source, rdf.Literal(source)))

# function to return source of a given data source. 
def get_source(resource):
    # check if given resource is a data source
    if get_level(resource) == data_layer.value:
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.source):
            return str(o)
    else:
        print('rdf_manager: get_source: unexpected resource given, it doesnt match the data layer')