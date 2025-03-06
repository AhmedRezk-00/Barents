# BFP-BARENTS
*Realisierung eines Konzepts für eine bedarfsgerechte Datenaufbereitung.*

Dieses Repository realisiert im Rahmen eines Bachelor-Forschungsprojekts an der Universität Stuttgart einen Prototyp bezüglich des papers ["Demand-Driven Data Provisioning in DataLakes: BARENTS — A Tailorable Data Preparation Zone"](https://www.ipvs.uni-stuttgart.de/departments/as/publications/stachch/iiwas_21_barents.pdf).

## Autoren

| Name        | Matrikelnummer | e-mail   | Studiengang             |
| ----------- | -------------- | -------- | ----------------------- |
| Luke Mayr   | 3593022        | st177937 | B. Sc. Medieninformatik |
| Metin Arab  | 3587258        | st178931 | B. Sc. Informatik       |
| Tabea Steeb | 3315718        | st156637 | B. Sc. Informatik       |
| Ahmed Rezk  | 3391499        | st163697 | B. Sc. Informatik       |

## Projekte 
Im Rahmen des Forschungsprojekts erstellen wir einen Prototyp.
Dieser ist im entsprechendenden Ordner, "prototype", zu finden. 
Dazu gehört ein Frontend, mit dem RDF-Ontologien erstellt werden können und ein backend, welches diese Ontologien verarbeiten kann.

Es gibt drei Mockups, mit denen graphische und logische Umsetzung des GUIs getestet wurde. 
Mehr Infos: [Mockups](mockups/README.md)

## Setup

### Depenencies, etc.
Wir verwenden verschiedene Libraries: rdflib, customtkinter, PIL, sqlite
Sind diese noch nicht installiert, dann führe folgende Befehle im Terminal aus:
pip install rdflib
pip install customtkinter
pip install pillow
pip install sqlite3

### Installation

## Programmausführung
Aktuell kann der prototype von der Datei "frontend.py" ausgeführt werden.
