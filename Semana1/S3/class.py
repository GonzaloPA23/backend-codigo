# this is a class
class MyClass:
    number = 12323
    text = "Hello world"
    state = True


values = MyClass()

# Print the attributes of the values object
# print(values.number) #12323
# print(values.text) #Hello world


class Car:
    # Este método nos permite inicializar los atributos de la clase
    def __init__(self, color, model, year):
        self.color = color
        self.model = model
        self.year = year

    # Este método nos permite representar el objeto como un string
    def __str__(self):
        return f"Car with the color {self.color}, model {self.showModel()} and year {self.year}"  

    # Este método nos permite mostrar el modelo del auto
    def showModel(self):
        return self.model
    
auto = Car("red", "Mitsubishi", 2019)
print(auto) #Car with the color red, model Mitsubishi and year 2019
# print("Color of the auto: ", auto.color) #red
# print("Model of the auto: ", auto.model) #Mitsubishi
# print("Year of the auto: ", auto.year) #2019


""" 
    Crear un objeto operaciones, que tenga los siguientes métodos:
    - Suma
    - Resta

    Y los atributos se deben ingresar por el objeto.
    print(operacion.suma())
    print(operacion.resta())
"""

class Operations:
    def __init__(self, number1:float, number2:float):
        self.number1 = number1
        self.number2 = number2
    
    def __str__(self):
        return f"Operations with the numbers {self.number1} and {self.number2}"

    def suma(self) -> float:
        return self.number1 + self.number2
    
    def resta(self) -> float:
        return self.number1 - self.number2
    

operacion = Operations(10.34, 5.00)
print(operacion)
print(operacion.suma())
print(operacion.resta())