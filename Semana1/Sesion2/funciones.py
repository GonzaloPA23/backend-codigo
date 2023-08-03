def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b == 0:
        return "No se puede dividir entre 0"
    else:
        return a / b

# recursividad en funciones

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))