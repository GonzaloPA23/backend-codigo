from functools import wraps # sirve para poder decorar una funcion
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from models import UsuarioModel, TipoUsuario
from flask_jwt_extended.exceptions import NoAuthorizationError
from utilitarios import conexion

# custom decorator 
def validator_usuario_admin(funcion):
    # wraps > envuelve la función o método donde vamos a utilizar esta funcion para devolvernos toda su configuracion (parametros y otros)
    @wraps(funcion)
    def wrapper(*args, **kwargs):
        # es donde voy a hacer la validación 
        print(args)
        # decodifica la token de la peticion (de los headers de autorizacion)
        data = verify_jwt_in_request()
        id = data[1].get('sub')
        
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id = id).first()
        if not usuarioEncontrado:
            raise NoAuthorizationError('El usuario no existe')
        print(usuarioEncontrado.tipoUsuario) # 1 > admin, 2 > usuario normal

        if usuarioEncontrado.tipoUsuario != TipoUsuario.ADMIN:
            raise NoAuthorizationError("El usuario no tiene los permisos suficientes") # el raise sirve para lanzar un error personalizado 
        # si la validación es exitosa lo dejaré pasar a la función que viene despues de este decorador
        return funcion(*args, **kwargs)
    
    return wrapper # retorna la funcion wrapper decorada con el jwt_required