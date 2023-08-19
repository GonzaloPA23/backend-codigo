from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from rest_framework.request import Request
from rest_framework.views import APIView
from .models import CategoriaModel
from .serializers import CategoriaSerializer
from rest_framework import status

# ejemplo de como renderizar plantillas 
def paginaInicio(request):
    print(request)
    data = {
        'usuario': {
            'nombre': 'Gonzalo',
            'apellido': 'Peredo'
        },
        'hobbies':[
            {
                'descripcion': 'Ir al cine'
            },
            {
                'descripcion': 'Jugar videojuegos'
            }
        ]
    }

    return render(request,'inicio.html',{'data':data})

@api_view(http_method_names=['GET','POST'])
def devolverHoraServidor(request: Request):
    print(request.method)

    if request.method == 'GET':
        return Response(data={
            'content': datetime.now()
        })
    elif request.method == 'POST':
        return Response(data={
            'content': 'Para saber la hora realiza un GET'
        })
    
class CategoriasController(APIView):
    def get(self,request: Request):
        # SELECT * FROM categorias;
        categorias = CategoriaModel.objects.all()
        print(categorias)
        serializador = CategoriaSerializer(instance=categorias,many=True)
        return Response(data={
            'content': serializador.data
        })
    
    def post(self, request:Request):
        # donde se guarda la info proveniente del cliente
        data = request.data
        print(data)
        # data > validar la información entrante y ver que cumpla con los parametros necesarios
        serializador = CategoriaSerializer(data=data)
        validacion = serializador.is_valid()

        if validacion == True:
            nuevaCategoria = serializador.save()
            print(nuevaCategoria)
            return Response(data={
                'content': 'Se creo la categoria exitosamente'
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message': 'Hubo un error al crear la categoria',
                'content': serializador.errors # me da un listado con los errores
            },status=status.HTTP_400_BAD_REQUEST)
        
class CategoriaController(APIView):
    def get(self,request:Request, id:str):
        categoriaEncontrada = CategoriaModel.objects.filter(id=id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Categoria no encontrada'
            },status=status.HTTP_404_NOT_FOUND)
        serializador = CategoriaSerializer(instance=categoriaEncontrada)
        return Response(data={
            'content': serializador.data
        })
    
    def put(self,request:Request, id:str):
        categoriaEncontrada = CategoriaModel.objects.filter(id=id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Categoria no encontrada'
            },status=status.HTTP_404_NOT_FOUND)
       
        data = request.data
        serializador = CategoriaSerializer(data=data)
        dataValida = serializador.is_valid()
        if dataValida:
            serializador.validated_data # la data convertida a un diccionario con los campos que necesita el modelo, si se le llegase a pasar algun campo que no utiliza este automaticamente no se guardaria en este atributo
            serializador.update(categoriaEncontrada, serializador.validated_data)
            return Response(data={
                'content': 'Se actualizo la categoria exitosamente'
            },status=status.HTTP_202_ACCEPTED)
        else:
            return Response(data={
                'message': 'Hubo un error al actualizar la categoria',
                'content': serializador.errors
            },status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request:Request, id:str):
        categoriaEncontrada = CategoriaModel.objects.filter(id=id).first()
        if not categoriaEncontrada:
            return Response(data={
                'message': 'Categoria no encontrada'
            },status=status.HTTP_404_NOT_FOUND)
        
        CategoriaModel.objects.filter(id=id).delete()
        return Response(data={
            'content': 'Se elimino la categoria exitosamente'
        },status=status.HTTP_200_OK)