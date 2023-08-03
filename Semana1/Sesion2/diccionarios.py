# Importando librerias
from pprint import pprint

miDiccionario = {
    "Alemania": "Berlin",
    "Francia": "Paris",
    "Reino Unido": "Londres",
    "España": "Madrid",
    "Peru": "Lima",
    "otrosDatos": {
        "poblacion": 1000000,
        "presidencia": "Martin Vizcarra",
        "tags": ["turismo", "comida"],
    },
}

# Imprimir el valor de una llave
print(miDiccionario["Peru"])

# Agregar un elemento al diccionario
miDiccionario["Italia"] = "Roma"
pprint(miDiccionario)
