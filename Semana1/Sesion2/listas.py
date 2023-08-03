#Slicing de una lista dentro de una lista
lista = [[1,2,3],[4,5,6],[7,8,9]]
print(lista[0][1:2])


alumnos = ["Gonzalo", "Eduardo", "Jorge", "Luis", "Javier"]
print(alumnos)
print("Este es el resultado de un slicing [:2]: ", alumnos[:2])

# Agregar un elemento al final de la lista
alumnos.append("Juan")
print("Este es el resultado de un append: ", alumnos)

# Remover un elemento de la lista
alumnos.remove("Jorge")
alumnos.pop(0)

print("Este es el resultado de un remove: ", alumnos)

# Extender una lista con otro
alumnos.extend(["Jorge", "Luis", "Javier"])
print("Este es el resultado de un extend", alumnos)

# Insertar un elemento en una posición específica
alumnos.insert(0, "Gonzalo")
print("Este es el resultado de un insert", alumnos)

# Ordenar una lista
alumnos.sort()
print("Este es el resultado de un sort", alumnos)

# Ordenar una lista de forma inversa
alumnos.sort(reverse=True)
print("Este es el resultado de un sort reverse", alumnos)
