from flask import Flask, request #el request sirve para mostrar la información que nos quiere enviar el cliente
from datetime import datetime
from psycopg2 import connect
from uuid import UUID


conexion = connect(
    database="minimarket",
    user="postgres",
    password="@Goldenboy2310@",
    host="localhost",
    port="5432",
)
# __name__ > indicara si el archivo en el cual estamos es el archivo principal o no (__main__)
# en flask solamente se puede tener una instancia de la clase por proyecto para evitar tener varios servidores en el mismo proyecto
app = Flask(__name__)


# indicando que la ruta '/' aceptará GET y POST
@app.route("/", methods=["GET", "POST"])
def inicio():
    # modificar el comportamiento del metodo route de la clase Flask para evitar modificar el metodo en la misma clase, es como si estuvieramos sobreescribiendo el metodo route pero sin modificarlo directamente en la clase Flask, parecido a override en java o c# o polimorfismo en python o javascript.
    # request > nos permite acceder a los datos que nos envia el cliente (FE)
    print(request.method)

    if request.method == "GET":
        return {"message": "Bienvenido a mi API de Flask"}
    elif request.method == "POST":
        return {
            "message": "La hora del servidor es: %s" % (datetime.now()),
        }


@app.route("/categorias", methods=["GET", "POST"])
def manejoCategorias():
    if request.method == "GET":
        # Creamos el cursor para poder interactuar con nuestra bd
        cursor = ( # este cursor es el que realiza la peticion a la base de datos
            conexion.cursor()
        )  # devuelve un cursor para realizar operaciones en la base de datos
        # Indicamos la query a realizarse en la base de datos
        cursor.execute("SELECT * FROM categorias;")
        # devolvera todos los resultados
        data = cursor.fetchall() # fetchall > devuelve todos los resultados, fetchone > devuelve un solo resultado, fetchmany(5) > devuelve los primeros 5 resultados
        # cerramos la conexion
        cursor.close()

        resultado = []
        # retornamos los datos
        for categoria in data:
            dataCategoria = {
                "id": categoria[0],
                "nombre": categoria[1],
                "estado": categoria[2],
                "color": categoria[3],
                "fechaCreacion": categoria[4],
            }
            resultado.append(dataCategoria)
            print(dataCategoria)

        return {
            "content": resultado,
        }
    elif request.method == "POST":
        print(request.json)
        body = request.json
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO categorias(nombre, estado, color) VALUES (%s, %s, %s);",
            (body.get("nombre"), body.get("estado"), body.get("color")),
        )
        # Sirve para guardar los cambios hechos en la base de datos de manera permanente
        conexion.commit()
        cursor.close()

        return {"message": "Categoria creada exitosamente"}


# con los <> indicamos que es una variable dinamica que se puede cambiar en el futuro y que se puede acceder a ella con el nombre que le damos en el <> en este caso id
@app.route("/categoria/<string:id>", methods=["GET", "PUT"])
def manejoUnaCategoria(
    id,
):  # acá recibimos el id que se envia en la ruta > debe ser el mismo nombre que le dimos en la ruta
    try:
        UUID(id, version=4)
    except ValueError:
        return {
            "message": "El id no es UUID valido"
        }, 400  # Bad Request (Solicitud incorrecta)
    cursor = conexion.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM categorias WHERE id = %s", (id,))
        resultado = cursor.fetchone()

        # if resultado == None:
        if not resultado:
            return {
                "message": "No existe la categoria"
            }, 404  # Not found (No encontrado)

        return {
            "content": {
                "id": resultado[0],
                "nombre": resultado[1],
                "estado": resultado[2],
                "color": resultado[3],
                "fechaCreacion": resultado[4],
            }
        }, 200  # Ok (Todo Bien) - valor por defecto
    elif request.method == "PUT":
        body = request.json
        cursor.execute(
            "UPDATE categorias SET nombre = %s, estado = %s, color = %s WHERE id = %s",
            (body.get("nombre"), body.get("estado"), body.get("color"), id),
        )
        return {"message": "Categoria actualizada exitosamente"}


if __name__ == "__main__":
    # si es el archivo principal se ejecutara el servidor
    # debug=True > nos permite que cada vez que hagamos un cambio en el archivo, se reinicie el servidor
    # app.run(debug=True, port=8000)
    app.run(debug=True)
