from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from marshmallow import fields
from models import UsuarioModel, TipoUsuario
from marshmallow_enum import EnumField

class UsuarioRequestDto(SQLAlchemyAutoSchema):
    # correo = auto_field() # cuando queremos agregar solamente para lectura o escritura,
    # Sobrescribo mi atributo correo y le agrego validaciones adicionales (tiene que ser correo valido)
    correo = fields.Email(required=True) # error_messages={'required': 'El correo es obligatorio', 'invalid': 'El correo no tiene un formato valido'
    class Meta:
        model = UsuarioModel

class UsuarioResponseDto(SQLAlchemyAutoSchema):
    tipoUsuario = EnumField(TipoUsuario)
    class Meta:
        model = UsuarioModel