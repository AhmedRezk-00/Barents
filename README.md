# BFP-BARENTS
*Realisierung eines Konzepts für eine bedarfsgerechte Datenaufbereitung.*

Dieses Repository realisiert im Rahmen eines Bachelor-Forschungsprojekts an der Universität Stuttgart einen Prototyp bezüglich des papers ["Demand-Driven Data Provisioning in DataLakes: BARENTS — A Tailorable Data Preparation Zone"](https://www.ipvs.uni-stuttgart.de/departments/as/publications/stachch/iiwas_21_barents.pdf).

## Authors

|  Name          | Matrikelnummer | e-mail   | Studiengang             |
|  -----------   | -------------- | -------- | ----------------------- |
|  Luke Mayr     | 3593022        | st177937 | B. Sc. Medieninformatik |
|  Metin Arab    | 3587258        | st178931 | B. Sc. Informatik       |
|  Tabea Steeb   | 3315718        | st156637 | B. Sc. Informatik       |
|  Ahmed Rezk    | 3391499        | st163697 | B. Sc. Informatik       |
|  Omar Aboulazm | 3392281        | st163760 | B. Sc. W-Informatik     |

## Description
For the research project we created a prototype.
A GUI that lets users create an RDF graph based on BARENTS ontology and a prototype backend that processes the RDF graph.
Both can be found in the folder prototype.  
There are three mockups that were used to test the graphical and logical implementation of the GUI.
for more Info: [Mockups](mockups/README.md)

## Setup

### Dependencies and Requirements
- Python 3.7 or higher
- External packages (need installation):
  - customtkinter
  - rdflib
  - Pillow
- Standard library modules (pre-installed with Python):
  - sqlite3
  - re
  - sys
  - os
  - tkinter (on Linux, may require additional installation: [How to install tkinter on Linux](https://www.geeksforgeeks.org/how-to-install-tkinter-on-linux/))

### Installation
1. Clone this repository
2. Install required dependencies
   

## Running the Application
1. Navigate to the project directory:
   ```
   cd path/to/bfp_barents
   python prototype/frontend/frontend.py
   ```

   Note: Replace `python` with `python3` if your system uses that command instead.

## Usage
1. Create the RDF graph with GUI.
2. To save the Graph press the "Export" button.
3. To process an RDF graph press the "Process RDF" button and navigate to the RDF/XML file
