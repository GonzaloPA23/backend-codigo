from flask import Flask
from urllib.parse import (
    quote_plus,
)  # sirve para codificar la contraseña de la base de datos -> usa caracteres especiales y los codifica para que no haya problemas
from base_de_datos import conexion
from models.mascota import MascotaModel
from flask_migrate import Migrate
from flask_restful import Api
from controllers.usuario import UsuariosController, UsuarioController
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint
from os import environ

app = Flask(__name__)
api = Api(app)
# origins > indica los dominios que pueden acceder a mi api -> si no se le indica nada, por defecto solo el dominio donde se encuentra alojado el backend puede acceder a la api (*)
# methods > indica los metodos a los que se puede acceder, por defecto todo (*)
# allow_headers > indica las cabeceras que se pueden enviar desde el frontend, por defecto todo (*)
CORS(
    app,
    origins=["https://editor.swagger.io", "https://mifrontend.com"],
    methods=["GET", "POST", "PUT", "DELETE"],
    # authorization > sirve para indicar que el header authorization puede ser enviado desde el frontend, para cuestiones de autorización
    # content-type > sirve para indicar que el header content-type puede ser enviado desde el frontend, ver la información que nos está enviando el cliente
    # accept > sirve para indicar que el header accept puede ser enviado desde el frontend, ver que es lo que aceptará el cliente
    allow_headers=["authorization", "content-type", "accept"],
)

# endpoint donde se podra acceder a la documentación
SWAGGGER_URL = "/docs"
# donde se almacena mi archivo a la documentación
API_URL = "/static/documentation_swagger.json"

configuracionSwagger = get_swaggerui_blueprint(
    SWAGGGER_URL,
    API_URL,
    config={
        # el nombre de la pestaña del navegador
        "app_name": "Documentación de Directorio de Mascotas"
    },
)

# agregar otra aplicación que no sea Flask a nuestro proyecto de Flask
app.register_blueprint(configuracionSwagger)

# config > sirve para indicar la configuracion de la base de datos -> guarda todas las variables de nuestro proyecto de Flask
# SQLALCHEMY_DATABASE_URI > sirve para indicar la ruta de la base de datos
# CONNECTION STRING >                        dialecto://usuario : password@host:puerto/nombre_base_de_datos
# los dialectos pueden ser : mysql, postgresql, sqlite, oracle, mssql
# postgresql://<usuario>:<contraseña>@<host>:<puerto>/<nombre_base_de_datos>
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@Goldenboy2310@@localhost:5432/directorio'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environ.get('DATABASE_URL')
# app.config[
#     "SQLALCHEMY_DATABASE_URI"
# ] = "postgresql://postgres:%s@localhost:5432/directorio" % quote_plus("@Goldenboy2310@")

# inicializar mi aplicación de flask sql alchemy
# dentro de la aplicación de flask tendremos nuestra conexion a la base de datos
conexion.init_app(app)
api.init_app(app)  # sirve para inicializar la clase Api

# https://flask-migrate.readthedocs.io/en/latest/index.html#alembic-configuration-options
# app > sirve para que migrate use la cadena de conexion dentro del config
# db > sirve para indicar la conexión que ya está realizada por nuestra configuración previa
Migrate(app, conexion)

""" 
@app.route('/crear-tablas',methods=['GET'])
def crearTablas():
    # creará todas las tablas declaradas en el proyecto 
    conexion.create_all()
    return {"message": "Creación ejecutada exitosamente"} 
    
"""
# Acá agregamos todas las rutas de nuestros controladores
api.add_resource(UsuariosController, "/usuarios")
api.add_resource(UsuarioController, "/usuario/<int:id>")

if __name__ == "__main__":
    app.run(debug=True)
