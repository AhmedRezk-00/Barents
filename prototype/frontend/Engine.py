import sqlite3
from rdflib import Graph, Namespace
import pandas as pd

def main():
    ontology = Graph()
    ontology.parse("C:/Users/UNI/Desktop/Bachleorforschung/BFP-BARENTS/prototype/frontend/eweeeeee.xml", format="xml")
    namee = Namespace("http://barents.dl/")
    for s, p, o in ontology:
         if p == namee.source:
            db_path = f"{o}"
    
    print(f"Database path: {db_path}")
    conn = sqlite3.connect(db_path)
    conn.close()
    
                
              

if __name__ == "__main__":
    main()
