from flask_restful import Resource, request
from decorators import validator_usuario_admin
from os import path
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import send_file

class SubirImagenController(Resource):
    # si utilizamos el decorador personalizado y este se ubica en otra posicion del proyexto, entonces tendremos que setear el archivo de swagger en la ubicacion de ese decorador
    @validator_usuario_admin
    def post(self):
        """
        file: controllers\\subirImagenSwagger.yml
        """
        #.format(path.join('controller', 'subirImagenSwagger.yml'))
        # path join > sirve para unir varias carpetas y archivos en un formato que pueda ser leido por el sistema operativo
        # c:\\user\\eduardo > linux
        # c:/user/eduardo > ps windows
        # c:\user\eduardo > cmd windows
    
        imagen = request.files.get('imagen') 

         #https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
        mimetypeValidos = ['image/png', 'image/jpeg','image/jpg','image/svg+xml','image/tiff']
        if not imagen:
            return{ 
                'message': 'Se necesita una imagen'
            },400
        
        # validar tipos de archivos 
        print(imagen.filename) # nombre del archivo
        print(imagen.name) # nombre de la llave en mi form-data
        print(imagen.mimetype) # tipo de archivo
        
        if imagen.mimetype not in mimetypeValidos:
            return{
                'message': 'Formato de imagen no permitido'
            },400

        # extrae el microsegundo de la hora actual
        id = datetime.now().strftime('%f')

        # quita algun caracter que pueda generar conflictos al momento de buscar el archivo en el servidor
        filename = id + secure_filename(imagen.filename) 

        # procedemos con el guardado de la imagen
        ruta = path.join('imagenes',filename)
        imagen.save(ruta)

        return{
            'message': 'Imagen subida exitosamente',
            'content': {
                'imagen': f'imagenes/{filename}'
            }
        }

class DevolverImagenController(Resource):
    def get(self,nombreImagen):
        ruta = path.join('imagenes',nombreImagen)

        #validamos si tenemos el archivo en nuestro servidor 
        resultado = path.isfile(ruta) # devuelve True si existe el archivo en la ruta especificada
        
        # si no existe el archivo, entonces devolver un mensaje de error
        if not resultado:
            return {
                'message': 'No existe la imagen'
            }, 404     
        
        print(nombreImagen)
        print(resultado)
        
        # sirve para enviar un archivo en particular para que lo pueda leer el cliente
        return send_file(ruta) # devuelve el archivo en la ruta especificada