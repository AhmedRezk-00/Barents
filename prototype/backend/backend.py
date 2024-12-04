import sys
import rdflib as rdf
import sqlite3 as sql

rdf_location= sys.argv[1]
rdf_graph = rdf.Graph()
dl = rdf.Namespace("http://barents.dl/")
rdf_graph.bind("dl", dl)

knowledge_layer = rdf.Literal("Knowledge Layer")
information_layer = rdf.Literal("Information Layer")
data_layer = rdf.Literal("Data Layer")


# function that processes data as described in rdf given by file location
def process_rdf(rdf_location):
    rdf_graph.parse(rdf_location)
    sources = []

    # iterate over all sinks 
    for ss, sp, so in rdf_graph.triples((None, dl.layer, knowledge_layer)):
        if rdf_graph.value(ss, dl.dbLocation):
            sink_conn =sql.connect(rdf_graph.value(ss, dl.dbLocation))
            # iterate over all transformations that lead into those sinks 
            for ts, tp, to in rdf_graph.triples((None, dl.partOf, ss)):
                # iterate over all sourcers that lead into those transformation
                for s, p, o in rdf_graph.triples((None, dl.partOf, ts)):
                    # if the current transformation is a filter
                    transformation_type = rdf_graph.value(ts, dl.type)
                    if transformation_type == 'filter':
                        pass
            sink_conn.close()

process_rdf(rdf_location)

# def example_sqlite():
#     conn = sqlite3.connect('testResources/Chinook_Sqlite.sqlite')
#     cursor = conn.cursor()

#     cursor.execute("SELECT * FROM Album LIMIT 5")
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row)


#     conn.commit()

#     conn.close()