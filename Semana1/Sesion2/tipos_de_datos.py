# string (str)
x = "Que bendición"
print(type(x))

# integer (int)
x = 20
print(type(x))

# float (float)
x = 20.5
print(type(x))

# complex (complex)
x = 1j
print(type(x))

# list (list)
x = ["manzana", "platano", "cereza"]
print(type(x))

# tuple (tuple)
x = ("manzana", "platano", "cereza")
print(type(x))

# range (range)
x = range(6)
print(type(x))

# dict (dict)
x = {
    "nombre": "John", 
    "edad": 36
}
print(type(x))
# print(x["nombre"]) -> John

# set (set) -> una especie de array pero con llaves -> inmutable
x = {"manzana", "platano", "cereza"}
print(type(x))

# frozenset (frozenset)
x = frozenset({"manzana", "platano", "cereza"})
print(type(x))

# bool (bool)
x = True
print(type(x))

# bytes (bytes)
x = b"Hello"
print(type(x))

# bytearray (bytearray)
x = bytearray(5)
print(type(x))

# memoryview (memoryview)
x = memoryview(bytes(5))
print(type(x))

# None (NoneType)
x = None
print(type(x))
