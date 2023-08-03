-- SQL > Structured Query Language 

-- DDL > Data Definition Language
-- CREATE > Crear tablas o bases de datos
-- ALTER > Modificar la estructura de nuestras tablas o columnas 
-- DROP > Eliminar tablas, columnas o bases de datos
-- TRUNCATE > Eliminar todos los registros de una tabla
-- COMMENT > Agregar comentarios a una tabla o columna
-- RENAME > Renombrar una tabla, columnas o bases de datos

CREATE DATABASE prueba; -- Crear una base de datos
-- NOTA: para los comando PSQL, porque empiezan con \, no es necesario terminarlos con ;
\c prueba; -- > Conectarse a una base de datos

CREATE TABLE alumnos (
    id SERIAL NOT NULL PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellidos TEXT,
    correo TEXT NOT NULL UNIQUE, -- UNIQUE > significa que el valor no se puede repetir en otro registro
    fecha_nacimiento DATE NOT NULL,
    matriculado BOOLEAN DEFAULT true -- DEFAULT > sirve para setear un valor por defecto en el caso que no se ingrese
);