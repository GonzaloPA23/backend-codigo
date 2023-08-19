# aca declararemos las urls de la app gestion
from django.urls import path
# cuando colocamos '.' indicamos que se trata de un archivo en el mismo nivel, sin embargo, cuando no colocamos el '.' estaremos indicando que sera una libreria o un archivo externo
from .views import paginaInicio,devolverHoraServidor,CategoriasController,CategoriaController

urlpatterns = [
    path('inicio', paginaInicio), # path sirve para declarar las urls de la app, recibe 2 parametros, el primero es la url y el segundo es la funcion que se ejecutara cuando se ingrese a esa url
    path('status',devolverHoraServidor),
    path('categorias',CategoriasController.as_view()), # para poder usar una clase como una vista, debemos usar el metodo as_view() de la clase
    path('categoria/<id>',CategoriaController.as_view())
]
