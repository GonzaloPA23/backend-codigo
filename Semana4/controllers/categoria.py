from flask_restful import Resource, request
from models import CategoriaModel
from dtos import CategoriaRequestDto
from utilitarios import conexion
from decorators import validator_usuario_admin
# get_jwt_identity > devolvera la identificación del usuario de la token
from flask_jwt_extended import jwt_required, get_jwt_identity

class CategoriasController(Resource):
    @validator_usuario_admin # sirve para indicar que este endpoint necesita una token para poder acceder a el
    def post(self):
        # security:
        #    - Bearer: [] -> acá se almacena el token para poder acceder a este endpoint (post) -> se debe enviar en el header de la petición 
        """
        Creacion de una categoria
        ---
        operationId: post_categoria
        description: Creacion de una nueva categoria con la imagen
        tags:
            - Categoria
        parameters:
            - in: body
              name: body
              schema:
                properties:
                    nombre:
                        type: string
                        example: 'Lorem'
                    fechaCreacion:
                        type: string
                        example: '2023-08-01T14:15:00'
                    imagen:
                        type: string
                        example: 'https://www.google.com'
        security:
            - Bearer: []            
        responses:
            201:
              description: Categoria creada exitosamente
              schema:
                 $ref: '#/definitions/Categoria'
        """
        dto = CategoriaRequestDto()
        # identificador = get_jwt_identity()
        # print(identificador)
        try:
            dataVerificada = dto.load(request.get_json())
            nuevaCategoria = CategoriaModel(**dataVerificada)
            conexion.session.add(nuevaCategoria)
            conexion.session.commit()
            return {
                'message': 'Categoria creada exitosamente',
                'content': ''
            },201
        except Exception as e:
            # rollback > retroceder el estado antes de que se de el error en la base de datos
            conexion.session.rollback()
            return {
                'message': 'Error al crear la categoria',
                'content': e.args
            }, 400
        
    def get(self):
        """ 
        file: getCategoria.yml
        """
        categorias = conexion.session.query(CategoriaModel).all()
        dto = CategoriaRequestDto(many=True)
        resultado = dto.dump(categorias, many=True)

        return {
            'content': resultado
        },200