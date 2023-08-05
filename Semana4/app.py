from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from utilitarios import conexion
from flask_cors import CORS
from os import environ
from dotenv import load_dotenv
from urllib.parse import quote_plus
from models import *



# sirve para cargar mis variables declaradas en el archivo .env como si fueran variables de entorno
load_dotenv()

app = Flask(__name__)

if environ.get("PYTHON_VERSION"):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL")
else:    
    passwordBd = environ.get("DATABASE_URL").split(":")[2].split("@localhost")[0]
    passwordConvertida = quote_plus(passwordBd)
    urlBd = environ.get("DATABASE_URL").replace(passwordBd, passwordConvertida)
    #print(passwordBd)
    app.config['SQLALCHEMY_DATABASE_URI'] = urlBd
# CORS > Cross Origin Resource Sharing (sirve para indicar quien puede tener acceso a mi API, indicando el dominio (origins), las cabeceras (allow_headers), y los metodos (methods))
CORS(app, origins='*')
api = Api(app)

conexion.init_app(app)

Migrate(app, conexion)

if __name__ == '__main__':
    app.run(debug=True)