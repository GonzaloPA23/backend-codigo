# https://docs.djangoproject.com/en/4.2/topics/db/models/
from django.db import models
from uuid import uuid4

# Create your models here.


class CategoriaModel(models.Model):
    opcionesNivelAzucar = (
        # si usaramos formularios dentro de django
        # bd , lo que mostramos en el formulario
        ["MA", "MUY_ALTO"],
        ["ALTO", "ALTO"],
        ["MEDIO", "MEDIO"],
        ["BAJO", "BAJO"],
        ["MUY_BAJO", "MUY_BAJO"],
        ["CERO", "CERO"],
    )

    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    nombre = models.TextField(null=False)
    nivelAzucar = models.TextField(
        name="nivel_azucar",
        null=False,
        choices=opcionesNivelAzucar
    )

    class Meta:
        db_table = 'categorias'

class GolosinaModel(models.Model):
    tipoProcedencia = (
        ["NACIONAL", "NACIONAL"],
        ["IMPORTADO", "IMPORTADO"],
    )
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    nombre = models.TextField(null=False)
    fechaVencimiento = models.DateField(editable=True, null=False, name="fecha_vencimiento")
    precio = models.FloatField(null=False)
    procedencia = models.TextField(choices=tipoProcedencia,default="NACIONAL")

    # relacion de muchos a uno
    # on delete > cuando se elimine un registro de la categoria y esta tenga golosinas, como deberia actuar la base de datos? SUS OPCIONES SON
    # CASCADE > elimina la categoria y elimnar sus golosinas
    # PROTECT > no se puede eliminar la categoria si tiene golosinas, lanzara un error de tipo ProtectedError
    # RESTRICT > evitara la elimicacion pero lanzara un error de tipo RestrictedError
    # SET_NULL > si se elimina la categoria, las golosinas que pertenecian a esta categoria, tendran el campo categoria_id en null (NOTA: no se tiene que poner null=False)
    # SET_DEFAULT > si se elimina la categoria, las golosinas que pertenecian a esta categoria, tendran el campo categoria_id en el valor por defecto 
    # DO_NOTHING > no se debe utilizar esto, deja el id en esta columna a pesar que ya no exista por enede generara mala integridad de datos

    # related_name > crea un atributo virtual en mi otro modelo para poder acceder a todos sus golosinas desde la categoria, si no se define este parametro usara el siguiente formato
    # NOMBRE_MODELO_set > GolosinaModel_set
    # internamente cuando se mande a llamar a este atributo generara un join entre las tablas de manera dinamica (no siempre se crea el join, solo cuando se llama)
    categoria = models.ForeignKey(to=CategoriaModel, db_column="categoria_id", on_delete=models.PROTECT, related_name='golosinas')

    class Meta:
        db_table = 'golosinas'
        # unicidad entre dos o mas columnas

        # jamas se podra repetir en un registro el nombre y la fecha de vencimiento
        # constraint | restriccion
        # nombre de las columnas no de los atributos
        unique_together = [['nombre', 'fecha_vencimiento']] 