import rdflib as rdf

mainGraph = rdf.Graph()
dl = rdf.Namespace("http://barents.dl/")
mainGraph.bind("dl", dl)

uniqueId = 1

knowledgeLevel = rdf.Literal("Knowledge Layer")
informationLevel = rdf.Literal("Information Layer")
dataLevel = rdf.Literal("Data Layer")

subject_dictionary = []

# function to add data layer ressource
def addDataSource(number):
    # TODO: add proper check for duplicate names
    global uniqueId
    mainGraph.add((rdf.URIRef(dl + "unnamedRessource" + str(uniqueId)), dl.layer, dataLevel))
    add_to_dictionary(number, "unnamedRessource" + str(uniqueId))
    uniqueId += 1

# function to add knowledge layer ressource
def addDataSink(number):
    # TODO: add proper check for duplicate names
    global uniqueId
    mainGraph.add((rdf.URIRef(dl + "unnamedRessource" + str(uniqueId)), dl.layer, knowledgeLevel))
    add_to_dictionary(number, "unnamedRessource" + str(uniqueId))
    uniqueId += 1

# function to export rdf graph as .xml
def exportGraph():
    mainGraph.serialize(format="xml", destination="resultsRDF.xml")

def resetGraph():
    global mainGraph
    del mainGraph
    mainGraph = rdf.Graph()
    mainGraph.bind("dl", dl)

# function to add information level ressource
def addTransformation(number):
    # TODO: add proper check for duplicate names
    global uniqueId
    mainGraph.add((rdf.URIRef(dl + "unnamedRessource" + str(uniqueId)), dl.layer, informationLevel))
    add_to_dictionary(number, "unnamedRessource" + str(uniqueId))
    uniqueId += 1

def renameTriples(ressource, newName):
    for s, p, o in mainGraph.triples((rdf.URIRef(dl + ressource), None, None)):
        mainGraph.remove((s,p,o))
        # add check if newname is avialble
        mainGraph.add((rdf.URIRef(dl + newName),p,o))

def add_to_dictionary(index, subject):
    if len(subject_dictionary) <= index:
        subject_dictionary.extend([None] * (index + 1 - len(subject_dictionary)))
    subject_dictionary[index] = subject