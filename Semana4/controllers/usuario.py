from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDto, UsuarioResponseDto
from bcrypt import gensalt, hashpw

class RegistroController(Resource):
    def post(self):
        try:
            dto = UsuarioRequestDto() # este es de la clase UsuarioRequestDto
            dataValidada = dto.load(request.get_json())
            
            # generar el hash de la contraseña
            # creara un texto aleatorio
            salt = gensalt() # expresado en bytes
            password = dataValidada.get('password')

            # convertimos la contraseña a bytes
            passworBytes = bytes(password, 'utf-8')

            # mezclamos el password con el salt generado y lo convertimos a string
            passwordHaseada = hashpw(password=passworBytes, salt=salt).decode('utf-8') # mezcla el texto aleatorio con la contraseña y genera un hash

            # reemplazamos la contraseña por el hash generado
            dataValidada['password'] = passwordHaseada

            # fin del hashing de la contraseña

            nuevoUsuario = UsuarioModel(**dataValidada)
            
            conexion.session.add(nuevoUsuario)
            conexion.session.commit()

            dtoResponse = UsuarioResponseDto() # este es de la clase UsuarioResponseDto

            return {
                'message': 'Usuario creado exitosamente',
                'content': dtoResponse.dump(nuevoUsuario)
            }, 201
        
        except Exception as e:
            return {
                'message': 'Error al crear el usuario',
                'content': e.args
            }, 400