# Variables en python
numero = 5

# imprimir variable
print(numero)

# Sintaxis de Python

if numero == 5:
    print("El numero es 5")

""" 
    Comentario de varias lineas
    Este es otro comentario
"""

# Declarar multiples variables
numero1, numero2, numero3 = 1, 2, 3

# Variables

variable_global = ""

def funcion():
    variable_global = "Esta es una variable global"
    return variable_global

print(funcion())

# Variables globales
def miFuncion2():
    global b
    b = "Esta es una variable global desde miFuncion2"
    return b

print(miFuncion2())