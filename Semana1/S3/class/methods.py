import hashlib # this is a library to encrypt the password

class Password:
    def quitarEspacios(self, nombre:str) -> str:
        return nombre.replace(" ", "")
    
    def convertirMinusculas(self, nombre_sin_espacios:str) -> str:
        return nombre_sin_espacios.lower()

    def encriptarPassword(self, nombre_validado:str) -> str:
        return hashlib.sha1(nombre_validado.encode()).hexdigest()
    
        

