from flask_sqlalchemy import SQLAlchemy
# Acá se crea la instancia de la clase SQLAlchemy para poder interactuar con la base de datos; SQLAlchemy es una libreria que nos permite interactuar con la base de datos de una manera mas sencilla accediendo a los datos de la base de datos como si fueran objetos de python (ORM)
conexion = SQLAlchemy()