miNombre = "Gonzalo_De_La_Cruz"
# Imprimir la primera letra de mi nombre convertido en mayusucula y el resto en minuscula
# Output esperado: Hola soy: GONZALO de la cruz
# Forma 1
separador = miNombre.split("_")
print("Hola soy:", separador[0].upper(), " ".join(separador[1:]).lower())
# Forma 2
print("Hola soy:", separador[0].upper(), separador[1].lower(), separador[2].lower(), separador[3].lower())

""" 
    Ejercicio Resuelto por el profesor
"""

myName = "Eduardo_De_Rivera"
# Imprimir la primera letra de mi nombre convertido en mayusucula y el resto en minuscula
# Output esperado: Hola soy: Eduardo de rivera

myNameList = myName.split("_")
nameUpper = myNameList[0].upper()
apellidoLower = myNameList[1].lower()
apellido2Lower = myNameList[1].lower()
resultado = f"Hola soy: {nameUpper} {apellidoLower} {apellido2Lower}"
print(resultado)