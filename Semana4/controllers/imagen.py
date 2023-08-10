from flask_restful import Resource, request
from decorators import validator_usuario_admin

class SubirImagenController(Resource):
    @validator_usuario_admin
    def post(self):
        """
        file: subirImagenSwagger.yml
        """
        print(request.files)
        return{
            'message': 'Imagen subida exitosamente',
        }