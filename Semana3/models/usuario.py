from sqlalchemy import Column, types 
from base_de_datos import conexion

# Model > sirve para indicar que esta clase se convertira en un Modelo y por ende creara la tabla respectiva en la base de datos 
class UsuarioModel(conexion.Model):
    # type_ > para indicar el tipo de dato en la base de datos
    # primary_key > para indicar que es una llave primaria
    # autoincrement > para indicar que se autoincrementa
    # nullable > para indicar que no puede ser nulo
    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    apellido = Column(type_=types.Text)
    correo = Column(type_=types.Text, unique=True, nullable=False)
    telefono = Column(type_=types.Text, nullable=True)
    # en el ORM trabajar con CamelCase y en la base de datos con snake_case sirve para de una manera adicional, proteger los verdaderos nombres de las columnas de la base de datos
    linkedinUrl = Column(name='linkedin_url', type_=types.Text)
    #__tablename__ > sirve para indicar el nombre de la tabla en la base de datos, si no se le proporciona, usará el nombre de la clase
    __tablename__ = 'usuarios'