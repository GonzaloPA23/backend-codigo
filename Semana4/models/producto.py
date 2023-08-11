from utilitarios import conexion
from sqlalchemy import Column, ForeignKey, types
from sqlalchemy.orm import relationship

class ProductoModel(conexion.Model):
    __tablename__='productos'

    id = Column(type_=types.Integer, primary_key=True, autoincrement=True)
    nombre = Column(type_=types.Text, nullable=False)
    descripcion = Column(type_=types.Text)
    precio = Column(type_=types.Float, nullable=False)
    precioDscto = Column(type_=types.Float, name='precio_dscto')
    imagen = Column(type_=types.Text)
    disponibilidad = Column(type_=types.Boolean, default=True)
    stock = Column(type_=types.Integer, nullable=False)
    categoriaId = Column(ForeignKey(column='categorias.id'), type_=types.Integer
    , name='categoria_id')

    # colocar el nombre de la clase que se va a relacionar
    # backref > crea un atributo virtual (se crea al momento de llamar a una/muchas categoria en la clase CategoriaModel)

    # relationship > con el relationship hace que se muestre la información de la categoría relacionada al producto
    categoria = relationship('CategoriaModel', backref='productos')