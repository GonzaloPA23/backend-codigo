from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from utilitarios import conexion
from flask_cors import CORS
from os import environ
from dotenv import load_dotenv
from urllib.parse import quote_plus
from models import *
from flasgger import Swagger
from controllers import CategoriasController, RegistroController, LoginController, SubirImagenController, DevolverImagenController, ProductosController
from flask_jwt_extended import JWTManager
# LOAD > convierte un string en formato json a un diccionario
from json import load
from datetime import timedelta

# sirve para cargar mis variables declaradas en el archivo .env como si fueran variables de entorno
load_dotenv()
swaggerData = load(open('swagger_data.json', 'r'))

#Para añadir más confuguraciones a la documentación, revisar la documentación de flasgger
#https://github.com/flasgger/flasgger#customize-default-configurations
swaggerConfig = {
    'headers': [], #las cabeceras que van a aceptar nuestra documentación 
    'specs': [
        {
            'endpoint': '', #el endpoint inicial de nuestra documentación
            'route': '/',
        }
    ],
    'static_url_path': '/flasgger_static', #cargar los archivos staticos que serian el css y js de la libreria
    #'swagger_ui': True, #indicar si queremos cargar la interfaz grafica de swagger o no
    'specs_route': '/documentacion/', #el endpoint en el cual ahora se ingresara a mi swagger
}

app = Flask(__name__)

if environ.get("PYTHON_VERSION"):
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get("DATABASE_URL")
else:    
    passwordBd = environ.get("DATABASE_URL").split(":")[2].split("@localhost")[0]
    passwordConvertida = quote_plus(passwordBd)
    urlBd = environ.get("DATABASE_URL").replace(passwordBd, passwordConvertida)
    #print(passwordBd)
    app.config['SQLALCHEMY_DATABASE_URI'] = urlBd

# servira para firmar las tokwns
app.config['JWT_SECRET_KEY'] = environ.get('JWT_SECRET')
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(hours=1, minutes=15) #tiempo de expiracion de la token

JWTManager(app)

Swagger(app,template=swaggerData, config=swaggerConfig)
# CORS > Cross Origin Resource Sharing (sirve para indicar quien puede tener acceso a mi API, indicando el dominio (origins), las cabeceras (allow_headers), y los metodos (methods))
CORS(app, origins='*')
api = Api(app)

conexion.init_app(app)

Migrate(app, conexion)

# rutas
api.add_resource(CategoriasController, '/categorias')
api.add_resource(RegistroController, '/registro')
api.add_resource(LoginController, '/login')
api.add_resource(SubirImagenController, '/subir-imagen')
api.add_resource(DevolverImagenController,'/imagenes/<nombreImagen>')
api.add_resource(ProductosController, '/productos')

if __name__ == '__main__':
    app.run(debug=True)