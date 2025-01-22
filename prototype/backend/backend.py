
import sqlite3 as sql
import rdflib as rdf

rdf_graph = rdf.Graph()
dl = rdf.Namespace("http://barents.dl/")
rdf_graph.bind("dl", dl)
knowledge_layer = rdf.Literal("Knowledge Layer")
information_layer = rdf.Literal("Information Layer")
data_layer = rdf.Literal("Data Layer")

def process_rdf(rdf_location):

    setup_chocolate_db()
    rdf_graph.parse(rdf_location)
    # create list of sources 
    sources = set()
    for s, p, o in rdf_graph.triples((None, dl.layer, data_layer)):
        sources.add(s)

    # create list of transformations 
    transformations = set()
    for s, p, o in rdf_graph.triples((None, dl.layer, information_layer)):
        transformations.add(s)

    unlocked_transformations = set()
    # iterate over transformations. if transformation is possible to run, run it and add its sink to sources. then remove the transformation from the list
    while transformations:
        for transformation in transformations:
            required_sources = set()

            for s, p, o in rdf_graph.triples((None, dl.partOf, transformation)):
                required_sources.add(s)

            if all(source in sources for source in required_sources):
                # run transformation
                run_transformation(transformation, required_sources)
                # THIS SHOULD BE SINK FOLLOWING TRANSFORMATION, NOT TRANSFORMATION ITSELF
                sources.add(transformation)
                # remove transformation
                unlocked_transformations.add(transformation)
                
            required_sources.clear()

        transformations = transformations - unlocked_transformations
        unlocked_transformations.clear()

    print('all transformations have been exhausted')
    # move results from transformations to actual data sinks 

def run_transformation(transformation, sources):
    transformation_type = rdf_graph.value(transformation, dl.type).strip()
    match transformation_type:
        case "filter":
            filter(transformation, sources)
        case "map":#TODO
            ...
        case _:
            print('unsupported filter type')

def setup_chocolate_db():
    con = sql.connect("C:/Users/UNI/Desktop/Database/candy.db")
    cur = con.cursor()

    # Drop the table if it exists
    cur.execute("DROP TABLE IF EXISTS chocolate")
    
    cur.execute("CREATE TABLE IF NOT EXISTS chocolate(name, hazelnut, walnut)")
    cur.execute("""INSERT INTO chocolate VALUES
                ('plain chocolate', false, false),
                ('hazelnut chocolate', true, false),
                ('walnut chocolate', false, true)
                """)
    
    # Print the table contents
    print("\nChocolate Table Contents:")
    cur.execute("SELECT * FROM chocolate")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    con.commit()
    con.close()

def filter(transformation, sources):
    sink = rdf_graph.value(transformation, dl.partOf)
    sinkColumn = str(sink).split('/')[-1]
    sinkTable = rdf_graph.value(sink, dl.zone)
    sinkDB = rdf_graph.value(sink, dl.dbLocation)
    lambda_function= rdf_graph.value(transformation, dl.function)
    source_dbs = set()
    for source in sources:
        source_dbs.add((rdf_graph.value(source, dl.dbLocation), rdf_graph.value(source, dl.source)))
    
    for source_db in source_dbs:
        con_source = sql.connect(source_db[0])
        con_sink = sql.connect(sinkDB)
        cur_source = con_source.cursor()
        cur_sink = con_sink.cursor()

        cur_source.execute(f"SELECT * from {source_db[1]}")
        # filter rows
        rows = cur_source.fetchall()
        filter_function = eval(lambda_function)
        filter =[row for row in rows if filter_function(row)]
        cur_source.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{source_db[1]}'")
        create_table_sql = cur_source.fetchone()
        check_for_table = create_table_sql[0].replace('CREATE TABLE', 'CREATE TABLE IF NOT EXISTS')
        check_for_table = check_for_table.replace(source_db[1], sinkTable)
        cur_sink.execute(check_for_table)
        placeholders = ', '.join(['?'] * len(filter[0])) if filter else ''
      # if row returns true for any of the lambda functions, remove row 
        cur_sink.executemany(f"INSERT INTO {sinkTable} VALUES ({placeholders})", filter)
        
        con_source.commit()
        con_sink.commit()

        con_source.close()
        con_sink.close()

    
##set up the process RDF button at the begining of the code
if __name__ == "__main__":
    # Provide the path to your RDF file
    rdf_file_path = "C:/Users/UNI/Desktop/names.xml"
    process_rdf(rdf_file_path)