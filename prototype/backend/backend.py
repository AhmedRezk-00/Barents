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

    # iterate over all sinks 
    for ss, sp, so in rdf_graph.triples((None, dl.layer, knowledge_layer)):
        if rdf_graph.value(ss, dl.dbLocation):
            # iterate over all transformations that lead into those sinks 
            for ts, tp, to in rdf_graph.triples((None, dl.partOf, ss)):
                # iterate over all sourcers that lead into those transformation
                for s, p, o in rdf_graph.triples((None, dl.partOf, ts)):
                    # if the current transformation is a filter
                    transformation_type = rdf_graph.value(ts, dl.type)
                    if transformation_type.value == 'filter':
                        sink_conn =sql.connect(rdf_graph.value(ss, dl.dbLocation))
                        source_conn =sql.connect(rdf_graph.value(s, dl.dbLocation))
                        sink_cursor = sink_conn.cursor()
                        source_cursor = source_conn.cursor()

                        query = f"SELECT {str(s).split('/')[-1]} FROM {rdf_graph.value(s, dl.source)} LIMIT 5"
                        source_cursor.execute(query)
                        rows = source_cursor.fetchall()
                        
                        filter_lambda = eval(rdf_graph.value(ts, dl.function))
                        filtered_rows = [row for row in rows if filter_lambda(row[0])]

                        sink_table = rdf_graph.value(ss, dl.zone)
                        if sink_table:
                            sink_cursor.execute(f"CREATE TABLE IF NOT EXISTS {sink_table} (data TEXT)")
                            sink_cursor.executemany(
                                f"INSERT INTO {sink_table} (data) VALUES (?)", 
                                filtered_rows
                            )
                            sink_conn.commit()

                        sink_conn.close()
                        source_conn.close()

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