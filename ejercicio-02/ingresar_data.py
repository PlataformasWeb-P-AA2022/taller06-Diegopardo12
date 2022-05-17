from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from genera_base import Pais

import requests
import json

engine = create_engine('sqlite:///basdemo.db')


Session = sessionmaker(bind=engine)
session = Session()

# leer el archivo de datos

#archivo = open("data/data-personas-001.json", "r")
archivo = requests.get("https://pkgstore.datahub.io/core/country-codes/country-codes_json/data/616b1fb83cbfd4eb6d9e7d52924bb00a/country-codes_json.json")

#datos_json =  json.load(archivo) # paso los datos del archivo a json
data = archivo.json()


for d in data:
    print(d)
    print(len(d.keys()))
    p = Pais(nombre_pais=d['CLDR display name'], capital=d['Capital'], continente=d['Continent'], \
            dial=d['Dial'],geoname_ID=d['Geoname ID'],itu = d['ITU'],lenguajes = d['ITU'],idependiente = d['is_independent'])
    session.add(p)

# confirmar transacciones

session.commit()
