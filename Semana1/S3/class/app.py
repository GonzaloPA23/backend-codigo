from methods import Password

""" 
Convertir el nombre del usuario en una contraseña
    - Quitar los espacios entre palabras
    - Todo tiene que estar en minúsculas
    - Encriptar la contraseña
"""

nombre = "Eduardo De Rivera"

# Instanciar el objeto ObjectPassword de la clase Password
ObjectPassword = Password()

# Llamar a los métodos de la clase Password
nombre_sin_espacios = ObjectPassword.quitarEspacios(nombre)
nombre_en_minusculas = ObjectPassword.convertirMinusculas(nombre_sin_espacios)
password_encriptada = ObjectPassword.encriptarPassword(nombre_en_minusculas)

# Imprimir los resultados
print("El nombre sin espacios: ", nombre_sin_espacios)
print("El nombre en minusculas: ", nombre_en_minusculas)
print("La contraseña encriptada: ", password_encriptada)
