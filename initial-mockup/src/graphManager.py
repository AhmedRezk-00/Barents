import rdflib as rdf

uniqueId = 0

mainGraph = rdf.Graph()
dl = rdf.Namespace("http://barents.dl/")
mainGraph.bind("dl", dl)

knowledgeLevel = rdf.Literal("Knowledge Layer")
informationLevel = rdf.Literal("Information Layer")
dataLevel = rdf.Literal("Data Layer")

def exportGraph():
    mainGraph.serialize(format="xml", destination="resultsRDF.xml")

def add_dataSource(source):
    global uniqueId
    resource = rdf.URIRef(dl + "unnamedResource" + str(uniqueId))
    mainGraph.add((resource, dl.layer, dataLevel))
    uniqueId += 1
    mainGraph.add((resource, dl.source, rdf.Literal(source)))
    
def addTransformation(type):
    global uniqueId
    resource = rdf.URIRef(dl + "unnamedTransformation" + str(uniqueId))
    transformationLiteral = rdf.Literal("something went wrong")
    match type:
        case "filter":
            transformationLiteral = rdf.Literal("filter")
        case "map":
            transformationLiteral = rdf.Literal("map")
        case "reduce":
            transformationLiteral = rdf.Literal("reduce")
        case "procedure":
            transformationLiteral = rdf.Literal("procedure")
        case _:
            transformationLiteral = rdf.Literal("something went wrong")
    mainGraph.add((resource, dl.type, transformationLiteral))
    mainGraph.add((resource, dl.layer, informationLevel))
    uniqueId += 1

def add_dataSink(zone):
    global uniqueId
    resource = rdf.URIRef(dl + "unnamedDataSink" + str(uniqueId))
    mainGraph.add((resource, dl.layer, knowledgeLevel))
    uniqueId += 1
    mainGraph.add((resource, dl.zone, rdf.Literal(zone + str(uniqueId))))
    uniqueId += 1

def deleteGraph():
    global mainGraph
    del mainGraph
    mainGraph = rdf.Graph()
    mainGraph.bind("dl", dl)
