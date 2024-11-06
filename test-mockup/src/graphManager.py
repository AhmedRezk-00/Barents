import rdflib as rdf

mainGraph = rdf.Graph()
dl = rdf.Namespace("http://barents.dl/")
mainGraph.bind("dl", dl)

literals = []

knowledgeLevel = rdf.Literal("Knowledge Layer")
informationLevel = rdf.Literal("Information Layer")
dataLevel = rdf.Literal("Data Layer")

uniqueId = 0

# function to export rdf graph as .xml
def exportGraph():
    mainGraph.serialize(format="xml", destination="resultsRDF.xml")
    
def resetGraph():
    global mainGraph
    del mainGraph
    mainGraph = rdf.Graph()
    mainGraph.bind("dl", dl)

# function to add literals, which can both represent data zones and data sources (as in data lakes, banks, etc.) 
def addLiteral(literal):
    # perhaps use rdflib containers here instead
    literals.append(rdf.Literal(literal))
def renameTriples(ressource, newName):
    for s, p, o in mainGraph.triples((rdf.URIRef(dl + ressource), None, None)):
        mainGraph.remove((s,p,o))
        # add check if newname is avialble
        mainGraph.add((rdf.URIRef(dl + newName),p,o))

# function to add data layer ressource
def addDataSource():
    # add proper check for duplicate names
    global uniqueId
    mainGraph.add((rdf.URIRef(dl + "unnamedRessource" + str(uniqueId)), dl.layer, dataLevel))
    uniqueId += 1
def addDataSink():
    # add proper check for duplicate names
    global uniqueId
    mainGraph.add((rdf.URIRef(dl + "unnamedRessource" + str(uniqueId)), dl.layer, knowledgeLevel))
    uniqueId += 1

def addTransformation():
    # add proper check for duplicate names
    global uniqueId
    mainGraph.add((rdf.URIRef(dl + "unnamedTransformation" + str(uniqueId)), dl.layer, informationLevel))
    uniqueId += 1
def setTransformationType(subject, transformationType):
    mainGraph.set((rdf.URIRef(dl + subject), dl.type, rdf.Literal(transformationType)))
def setTransformationFunction(subject, function):
    mainGraph.set((rdf.URIRef(dl + subject), dl.function, rdf.Literal(function)))

def setZone(subject, object):
    mainGraph.set((rdf.URIRef(dl + subject), dl.zone, rdf.Literal(object)))
def setPartOf(subject, object):
    mainGraph.set((rdf.URIRef(dl + subject), dl.partOf, rdf.URIRef(dl + object)))
def addSourceToResource(name, source):
    mainGraph.add((rdf.URIRef(dl + name), dl.source, rdf.Literal(source)))

# code-only example to generate ontology from barents paper to cover core functionality 
def testRun():
    pass
    #- create rdf file 
    resetGraph()
    #- add chocolate literal (will probably only be backend)
    addLiteral('chocolate')
    #- add 2 data layer ressources
    addDataSource()
    addDataSource()
    # rename data layer resource walnut
    renameTriples('unnamedRessource0', 'walnut')
    # rename data layer resource hazelnut
    renameTriples('unnamedRessource1', 'hazelnut')
    # define source relationship for walnut and hazelnut
    addSourceToResource('walnut', 'chocolate')
    addSourceToResource('hazelnut', 'chocolate')
    # add transformation ressource to information layer
    addTransformation()
    # rename transformation ressource peptides
    renameTriples('unnamedTransformation2', 'peptides')
    # select transformation type as filter 
    setTransformationType('peptides', 'filter')
    # add partof relationship to hazelnut and walnut based on filter 
    setPartOf('hazelnut', 'peptides')
    setPartOf('walnut', 'peptides')
    # add function to peptides 
    setTransformationFunction('peptides', 'lambda x : x.hazelnut or x.walnut')
    # add allergens literal (will probably only be backend)
    addLiteral('allergens')
    # add knowledge level ressource 
    addDataSink()
    # rename knowledge level ressource results
    renameTriples('unnamedRessource3', 'results')
    # add zone relationship to results
    setZone('results', 'allergens')
    # add partof relationship to peptides based on results ressource
    setPartOf('peptides', 'results')
    #- export rdf 
    exportGraph()

if __name__ == '__main__': 
    testRun()