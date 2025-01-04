import rdflib as rdf
import os
import re

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
        match os.path.splitext(file_name)[1]:
            case '.xml':
                rdf_graph.serialize(format="xml", destination=file_name)
            case '.ttl':
                rdf_graph.serialize(format="ttl", destination=file_name)
            case '.jsonld':
                rdf_graph.serialize(format="json-ld", destination=file_name)
            case '.nt':
                rdf_graph.serialize(format="nt", destination=file_name)
            case '.n3':
                rdf_graph.serialize(format="n3", destination=file_name)
            case _:
                rdf_graph.serialize(destination=file_name)      

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
        # remove all triples with old resource name
        rdf_graph.remove((s,p,o))
        # re-add all triples with new name of resource
        rdf_graph.add((rdf.URIRef(dl + new_name),p,o))
    for s, p, o in rdf_graph.triples((None, None,rdf.URIRef(dl + resource_name))):
        rdf_graph.remove((s,p,o))
        rdf_graph.add((s,p,rdf.URIRef(dl + new_name)))

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
        return""
    else:
        print('rdf_manager: get_transformation_function: unexpected resource given, it doesnt match the information layer')
        
# function to set the zone literal of a given knowledge level resource
def set_zone(resource, zone):
    rdf_graph.set((rdf.URIRef(dl + resource), dl.zone, rdf.Literal(zone)))

# function to return data zone of a given data sink, if given resource is a data sink
def get_zone(resource):
    # check if given resource is a data sink 
    if get_level(resource) == knowledge_layer.value:
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.zone):
            return str(o)
        return""
    else:
        print('rdf_manager: get_zone: unexpected resource given, it doesnt match the knowledge layer')

#issue99: returns order to swap the elements, of the part-of-set, or not
def swap(first_id, second_id, second_index_id):
    first_resource = resource_dictionary[first_id]
    second_resource = resource_dictionary[second_id]
    first_resource_level = get_level(first_resource);
    second_resource_level = get_level(second_resource);
 
    #at least one recource has to be a transformation
    if(first_resource_level == "Information Layer" or second_resource_level == "Information Layer"):
        # if first is source or second is sink, make relationship from first to second
        if(first_resource_level == "Data Layer" or second_resource_level == "Knowledge Layer"):
            return "dont swap";
        
        # if first is sink or second is source, make relationship from second to first
        if(first_resource_level == "Knowledge Layer" or second_resource_level == "Data Layer"):
            return "swap";
       
        # if both are transformations:
        #   if the last clicked-on resource isnt at the second (last) index of the part-of-set: 
        #       swap (move first-clicked element to first index)
        #   else: 
        #       dont swap
        if(first_resource_level == second_resource_level == "Information Layer"):
            if(second_id != second_index_id):
                return "swap"
            else:
                return "dont swap"

        else:
            #throw error 
            return "error";
    else:
        # throw error
        return "error";


# function to set partof relationship given two resources, with one of them being a information level resource (transformation)
def set_part_of(first_id, second_id):
    first_resource = resource_dictionary[first_id]
    second_resource = resource_dictionary[second_id]
    # check if exactly one id refers to transformatiion
    if (get_level(first_resource) == information_layer.value) ^ (get_level(second_resource) == information_layer.value):
        if get_level(first_resource) == information_layer.value:
            if get_level(second_resource) == data_layer.value:
                # first is transform, second is source
                rdf_graph.set((rdf.URIRef(dl + second_resource), dl.partOf, rdf.URIRef(dl + first_resource)))
            else:
                # first is transform, second is sink
                rdf_graph.set((rdf.URIRef(dl + first_resource), dl.partOf, rdf.URIRef(dl + second_resource)))
        if get_level(second_resource) == information_layer.value:
            if get_level(first_resource) == data_layer.value:
                # second is transform first is source
                rdf_graph.set((rdf.URIRef(dl + first_resource), dl.partOf, rdf.URIRef(dl + second_resource)))
            else:
                # second is transform second is sink 
                rdf_graph.set((rdf.URIRef(dl + second_resource), dl.partOf, rdf.URIRef(dl + first_resource)))
    else:
        print('rdf_manager: set_part_of: unexpected parameters: exactly one resource most belong to the information layer')
    #     rdf_graph.set((rdf.URIRef(dl + subject), dl.partOf, rdf.Literal(object)))

def delete_part_of(first_id, second_id):
    first_resource = resource_dictionary[first_id]
    second_resource = resource_dictionary[second_id]
    for s, p, o in rdf_graph.triples((rdf.URIRef(dl + first_resource), dl.partOf, rdf.URIRef(dl + second_resource))):
        rdf_graph.remove((s,p,o))
    for s, p, o in rdf_graph.triples((rdf.URIRef(dl + second_resource), dl.partOf,rdf.URIRef(dl + first_resource))):
        rdf_graph.remove((s,p,o))

# function to set source literal of a given data level resource
def set_source(resource, source):
    rdf_graph.set((rdf.URIRef(dl + resource), dl.source, rdf.Literal(source)))

# function to return source of a given data source. 
def get_source(resource):
    # check if given resource is a data source
    if get_level(resource) == data_layer.value:
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.source):
            return str(o)
        return""
    else:
        print('rdf_manager: get_source: unexpected resource given, it doesnt match the data layer')

# function to delete single resource from graph 
def delete_resource(resource_id):
    resource_name = resource_dictionary[resource_id]
    for s, p, o in rdf_graph.triples((rdf.URIRef(dl + resource_name), None, None)):
        rdf_graph.remove((s,p,o))
    for s, p, o in rdf_graph.triples((None, None,rdf.URIRef(dl + resource_name))):
        rdf_graph.remove((s,p,o))

# function that returns true if a given resource id refers to a resource that is already member of a partof relationship
def is_sink_part_of(resource_ids):
    for id in resource_ids:
        if get_level(resource_dictionary[id]) == knowledge_layer.value:
            for s, p, o in rdf_graph.triples((None, dl.partOf, rdf.URIRef(dl + resource_dictionary[id]))):
                    return True
    return False

def is_resource_valid(resource_name):
    if resource_name in resource_dictionary:
        return False 
    pattern = r'^[a-zA-Z0-9_-]+$'
    reserved_names = ['transformation_resource_', 'sink_resource_', 'source_resource_']
    if not re.match(pattern, resource_name):
        return False
    if any(resource_name.startswith(prefix) for prefix in reserved_names):
        return False
    return True

# function to set database location of data level resource
def set_location(resource, location):
    if get_level(resource) == data_layer.value or get_level(resource) == knowledge_layer.value:
        rdf_graph.set((rdf.URIRef(dl + resource), dl.dbLocation, rdf.Literal(location)))
    else:
        print('rdf_manager: set_source_location: unexcpected resource give, it doesnt match the data or knowledge layer')

# function to get database location of data level resource
def get_location(resource):
    # check if given resource is a data source
    if get_level(resource) == data_layer.value or get_level(resource) == knowledge_layer.value:
        for o in rdf_graph.objects(subject=rdf.URIRef(dl + resource), predicate=dl.dbLocation):
            return str(o)
        return""
    else:
        print('rdf_manager: get_location: unexpected resource given, it doesnt match the data or knowledge layer')
