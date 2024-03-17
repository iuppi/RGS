TIPS & ZO

VENV:

Setting up a new environment: 

#maak een venv:
   python -m venv venv

#admin level over 9000:
   Set-ExecutionPolicy RemoteSigned -Scope Process

#activeer venv:
 .\venv\Scripts\activate

#install requirements: 
 pip install -r requirements.txt

#update requirements
pip freeze > requirements.txt


Websites: 

RGS: https://www.referentiegrootboekschema.nl/definitieve-versie-rgs-taxonomie-36

NT: https://www.sbr-nl.nl/werken-met-sbr/taxonomie/documentatie-nederlandse-taxonomie



Gekke mapjes: data\input\ = voor boekhoud RGS bestand

data\output\ = nu voor mijn noob print.python

data\zip\ = voor zipjes van de taxonomie

zip_files\extracted_files = gebruikt in zip.py (uitpakken in windows geeft pathing issues)

XBLR = voor de uitgepakte taxonomie

META-INF = voor de uitgepakte taxonomie

NTt18 = versie van de taxonomie

Rendering = voor KVK rapportage

rgs = koppeling RGS met taxonomie


----

Arella = tool die met de taxonomie (XBLR) werkt.


📦data
 ┣ 📂input
 ┃ ┗ 📂xml
 ┣ 📂output
 ┃ ┗ 📜print_output.txt
 ┣ 📂zip
 ┗ 📂zip_files
 ┃ ┗ 📂extracted_files