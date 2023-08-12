from models import UsuarioModel
from utilitarios import conexion
from flask_restful import Resource, request
from dtos import UsuarioRequestDto, UsuarioResponseDto, LoginRequestDto, CambiarPasswordRequestDto
from bcrypt import gensalt, hashpw, checkpw
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from mensajeria import cambiarPassword

class RegistroController(Resource):
    def post(self):
        """ 
        file: registroUsuarioSwagger.yml
        """
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
        """
        file: loginSwagger.yml
        """
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

            # identity > es el dato que se va a codificar en el token, identicador para indicar a quien le pertenecera esta token
            token = create_access_token(identity=usuarioEncontrado.id)
            print(token)
            return{
                'message': token
            }
        except Exception as e:
            return {
                'message': 'Error al hacer el login',
                'content': e.args
            }, 400
        
class UsuarioController(Resource):
    # obliga a que para ingresar a este metodo se tenga que proveer una token por el header de authorization
    @jwt_required() # obliga al controlador que se le pase una token para poder acceder a este controlador
    def get(self):
        # extraer del payload de la jwt el identity que es a quien le pertenece esta token
        identity = get_jwt_identity() #
        print(identity)
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = identity).first()

        if not usuarioEncontrado:
            return {
                'message': 'El usuario no existe',
            }, 404
        
        dto = UsuarioResponseDto()
        return {
            'content': dto.dump(usuarioEncontrado)
        }
    
class CambiarPasswordController(Resource):
    @jwt_required()
    def post(self):
        data = request.get_json()
        dto = CambiarPasswordRequestDto()
        try:
            dataValidada = dto.load(data)
            identity = get_jwt_identity()
            # buscar si el usuario existe en la base de datos, si no existe, devolver un error
            usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = identity).first()

            if not usuarioEncontrado:
                return {
                    'message': 'El usuario no existe',
                }, 404

            # validar si la contraseña actual es la misma que la que esta en la base de datos (dataValidada.get('password'))
            # NOTE: tienen que convertirlo a un byte para poder compararlos con el checkpw
            password = bytes(dataValidada.get('password'),'utf-8')
            hashedPassword = bytes(usuarioEncontrado.password,'utf-8') # password hasheado

            if checkpw(password, hashedPassword) == False:
                return {
                    'message': 'La contraseña actual es incorrecta',
                }, 400
            
            # hashear la nueva password y la van a guardar en el usuario actual
            nuevaPassword = bytes(dataValidada.get('nuevoPassword'),'utf-8')
            
            salt = gensalt() # expresado en bytes
            hashNuevaPassword = hashpw(nuevaPassword, salt).decode('utf-8') # mezcla el texto aleatorio con la contraseña y genera un hash
            usuarioEncontrado.password = hashNuevaPassword
            conexion.session.commit()

            cambiarPassword(usuarioEncontrado.correo)
            return {
                'message': 'Contraseña cambiada exitosamente'
            }
        except Exception as e:
            return {
                'message': 'Error al cambiar la contraseña',
                'content': e.args
            }, 400