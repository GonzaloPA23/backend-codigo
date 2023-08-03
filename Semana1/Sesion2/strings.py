cadenaCaracteres = "Hola Mundo"
# Indexing
print(cadenaCaracteres[0])
# Slicing
print(cadenaCaracteres[2:7]) # -> la posición 7 no se incluye
# slice = cadenaCaracteres[2:5]
# print(slice)

print(cadenaCaracteres[:5]) # -> desde el inicio hasta la posición 5 (no incluida)
print(cadenaCaracteres[2:]) # -> desde la posición 2 hasta el final
print(cadenaCaracteres[-5:-2]) # -> desde la posición 5 empezando desde el final hasta la posición 2 empezando desde el final

# convertir a mayúsculas
print(cadenaCaracteres.upper())

# convertir a minúsculas
print(cadenaCaracteres.lower())

# quitar espacios en blanco al inicio y al final
print("Quitando los espacios en blanco: ", cadenaCaracteres.strip())

# reemplazar caracteres
print(cadenaCaracteres.replace("H", "J")) # -> reemplaza la H por la J

# dividir una cadena de caracteres
print(cadenaCaracteres.split(" ")) # -> divide la cadena de caracteres por el espacio en blanco

# concatenar cadenas de caracteres
print(cadenaCaracteres + " " + "desde Python")

# help(str) -> ayuda de los métodos de la clase str
nombre = "Gonzalo"
# Formatear cadena de caracteres
print("Hola {} bienvenido a Código {}".format("Gonzalo","Python"))
print(f"Hola {nombre} bienvenido a Código Python otra forma de formatear cadenas de caracteres")