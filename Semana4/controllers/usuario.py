from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDto, UsuarioResponseDto, LoginRequestDto
from bcrypt import gensalt, hashpw, checkpw

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

class LoginController(Resource):
    def post(self):
        dto = LoginRequestDto()
        try:
            dataValidada = dto.load(request.get_json())
            # busco si el usuario existe
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(correo = dataValidada.get('correo')).first()

            if not usuarioEncontrado:
                return {
                    'message': 'El usuario no existe',
                }, 404

            password = bytes(usuarioEncontrado.password,'utf-8') # password hasheado
            passwordIngresado = bytes(dataValidada.get('password'),'utf-8')

            # validará si es la misma contraseña o no
            resultado = checkpw(passwordIngresado, password)
            
            if resultado == False:
                return {
                    'message': 'La contraseña es incorrecta',
                }, 400

            return{
                'message': 'Bienvenido si eres!'
            }
        except Exception as e:
            return {
                'message': 'Error al hacer el login',
                'content': e.args
            }, 400