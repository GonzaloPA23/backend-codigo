from flask_restful import Resource, request
from models import ProductoModel
from models import CategoriaModel
from decorators import validator_usuario_admin
from dtos import ProductoRequestDto, ProductoResponseDto
from utilitarios import conexion


class ProductosController(Resource):
    @validator_usuario_admin
    def post(self):
        data = request.get_json()
        dto = ProductoRequestDto()
        try:
            dataValidada = dto.load(data)
            nuevoProducto = ProductoModel(**dataValidada)
            conexion.session.add(nuevoProducto)
            conexion.session.commit()
            dtoRpta = ProductoResponseDto()

            return {
                "message": "Producto creado exitosamente",
                "content": dtoRpta.dump(nuevoProducto),
            }
        except Exception as error:
            conexion.session.rollback()
            return {
                "message": "Ocurrio un error al crear el producto",
                "content": error.args,
            }

    def get(self):
        # SELECT * FROM productos;
        productosEncontrados = conexion.session.query(ProductoModel).all()

        # SELECT productos.id, categorias.id, categoria.nombre FROM productos JOIN categorias ON productos.categoria_id = categorias.id
        # podemos indicar que columnas queremos que nos devuelva
        # NOTA: al hacer uso del with_entities se pierde la instancia y se devuelve en forma de tupla la información
        # el join al ya tener relationships se vuelve implicito a no ser que querramos crear un join inexistente
        data = (
            conexion.session.query(ProductoModel)
            .join(CategoriaModel)
            .with_entities(ProductoModel.id, CategoriaModel.id, CategoriaModel.nombre)
            .all()
        )
        print(
            conexion.session.query(ProductoModel)
            .join(CategoriaModel)
            .with_entities(ProductoModel.id, CategoriaModel.id, CategoriaModel.nombre)
        )
        # print(data[0]) # (1, 1, 'Cuchillos elegantes')

        # otra forma de hacer la consulta
        # conexion.session.query(ProductoModel).join(CategoriaModel)
        # print(conexion.session.query(ProductoModel).join(CategoriaModel)) # para hacer un inner join entre las tablas productos y categorias

        dto = ProductoResponseDto(many=True)
        return {"content": dto.dump(productosEncontrados)}
