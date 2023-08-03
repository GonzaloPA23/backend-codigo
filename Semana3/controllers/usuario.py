from models.usuario import UsuarioModel
from flask_restful import Resource, request
from base_de_datos import conexion
from dtos.usuario import UsuarioRequestDTO
from marshmallow.exceptions import ValidationError
from sqlalchemy.exc import IntegrityError

class UsuariosController(Resource):
    # cuando creamos un metodo con el mismo nombre que el metodo http, si se llama a este metodo se ingresara al metodo de la clase
    def get(self):
        
        # SELECT * FROM usuarios;
        usuarios = conexion.session.query(UsuarioModel).all() # retorna una lista de instacia de la clase UsuarioModel
        dto = UsuarioRequestDTO()
        # dump > para convertir un objeto a un diccionario y si son muchos, se le pasa el parametro many=True para que las itere
        resultado = dto.dump(usuarios, many=True)
        print(usuarios)
        print(resultado)
        return {"content": resultado}

    def post(self):
        #data = request.json # sirve para obtener los datos que se envian por el body -> data:dict = request.get_json()
        data:dict = request.get_json()
        dto = UsuarioRequestDTO()

        try:
            # load > para cargar la información y esta validara si es correcta, si no es correcta se emitira un error
            dataValidada = dto.load(data)
            print(dataValidada)
            nuevoUsuario = UsuarioModel(**dataValidada) # ** > sirve para desempaquetar un diccionario y convertirlo en un objeto de tipo UsuarioModel 
            # nuevoUsuario = UsuarioModel(
            #     nombre=data.get('nombre',''),
            #     apellido=data.get('apellido',''),
            #     correo=data.get('correo'),
            #     telefono=data.get('telefono'),
            #     linkedinUrl = data.get('linkedinUrl'),
            # )
            # # Agregamos el nuevo usuario a la base de datos osea agregamos el nuevo registro a la cola del cursor
            conexion.session.add(nuevoUsuario)
            # # guardamos de manera permanetne nuestro usuario en la bd, si hay un error de validación aca se emitira
            conexion.session.commit()

            return {"message": "Usuario creado exitosamente "}, 201
        except ValidationError as error:
            return {
                'message': 'Error al crear el usuario',
                'content': error.args
            },400
        
        except IntegrityError as error:
            return {
                'message': 'Error al crear el usuario',
                'content': 'El usuario ya existe'
            },400
        except Exception as error:
            # siempre el Exception va al final (despues de todos los anteriores Excepts) porque es el que captura cualquier error, además me permite saber que tipo de error es
            return {
                'message': 'Error al crear el usuario',
                'content': error.args
            },400
        

class UsuarioController(Resource):
    #put > sirve para actualizar un recurso
    def put(self,id):
        # SELECT * FROM usuarios WHERE id = '....';
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario a actualizar no existe',
            },404
        data = request.get_json()
        dto = UsuarioRequestDTO()

        try:
            dataValidada = dto.load(data)
            # UPDATE usuarios SET nombre = '....', apellido = '....', correo = '....', telefono = '....', linkedinUrl = '....' WHERE id = '....';
            usuarioActualizados = conexion.session.query(UsuarioModel).filter_by(id=id).update(dataValidada)
            print(usuarioActualizados)
            conexion.session.commit()
            return {
                'message': 'Usuario actualizado exitosamente'
            }
        except ValidationError as error:
            return{
                'message': 'Error al actualizar el usuario',
                'content': error.args
            },400
        except IntegrityError as error:
            # profe una consulta, ese error de correo usted lo pone pq solo se tiene el correo como un tipo unico... si tuviera otra columna, como sabría de que error es? pero al momento de lanzar el contenido del mensaje ... ACA LA SOLUCION
            errorTexto: str = error.args[0]
            columna = errorTexto.split('la llave')[1]
            if columna.find('correo'):
                return{
                    'message': 'Error al actualizar el usuario',
                    'content': 'El correo ya existe'
                },400
            elif columna.find('nombre'):
                return {
                    'message': 'Error al actualizar el usuario',
                    'content': 'El nombre ya existe'
                },400
            
    def delete(self,id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario a eliminar no existe',
            },404
        
        # DELLETE FROM usuarios WHERE id = '....';
        conexion.session.query(UsuarioModel).filter_by(id=id).delete()
        conexion.session.commit()
        return {
            'message': 'Usuario eliminado exitosamente'
        },200
    
    def get(self,id):
        usuarioEncontrado = conexion.session.query(UsuarioModel).filter_by(id=id).first()
        if not usuarioEncontrado:
            return {
                'message': 'El usuario no existe',
            },404
        
        dto = UsuarioRequestDTO()
        usuarioConvertido = dto.dump(usuarioEncontrado)
        return {
            'content': usuarioConvertido
        }