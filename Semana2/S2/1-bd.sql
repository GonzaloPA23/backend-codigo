-- Creamos un nuevo usuario para que pueda acceder a nuestro servidor
-- CREATE ROLE "ederi" WITH LOGIN SUPERUSER PASSWORD 'password';
CREATE DATABASE minimarket;
-- DATE -> YYYY-MM-DD
-- DATETIME -> 31/10/2020 12:00:00.123
-- Mostramos la hora y fecha actual del servidor
SELECT NOW();
-- > el valor por defecto es DATETIME
-- Mostramos la fecha actual del servidor
SELECT CURRENT_DATE;
-- Mostramos la hora actual del servidor
SELECT CURRENT_TIME;
-- Mostramos la hora y fecha actual del servidor
SELECT CURRENT_TIMESTAMP;
-- > el valor que se guarda será el now() del servidor
-- Mostramos la hora y fecha actual del servidor
SELECT LOCALTIMESTAMP;
-- Mostramos la hora y fecha actual del servidor
SELECT LOCALTIME;
--Crear una tabla llamada categorías en la cual se tiene las sgtes columnas
-- id autoincrementable pk
-- nombre texto no puede ser nula y tiene que ser unica
-- estado que va a ser boolean y su valor por defecto va a ser true
-- color y este será un texto que puede ser nula
-- fecha_creacion que va a ser fecha y su valor por defecto sera now()
CREATE TABLE categorias (
    id SERIAL NOT NULL PRIMARY KEY,
    nombre TEXT NOT NULL UNIQUE,
    estado BOOLEAN DEFAULT true,
    color TEXT NULL,
    fecha_creacion TIMESTAMP(3) DEFAULT NOW()
);
-- CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; > extensión que sirve para el uuid 
CREATE TABLE categorias (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    -- para que se genere un uuid automaticamente, no será correlativo
    nombre TEXT NOT NULL UNIQUE,
    estado BOOLEAN DEFAULT true,
    color TEXT NULL,
    fecha_creacion TIMESTAMP(3) DEFAULT NOW()
);
-- Abarrotes true #ABABCD
-- limpieza true #1E2C9F
-- Frutas false #159358
INSERT INTO categorias (nombre, estado, color)
VALUES ('Abarrotes', true, '#ABABCD'),
    ('Limpieza', true, '#1E2C9F'),
    ('Frutas', false, '#159358'),
    ('Otros', true, '#000000');
--Creación de la tabla productos
CREATE TABLE productos(
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nombre TEXT NOT NULL,
    precio FLOAT NOT NULL,
    foto TEXT,
    disponible BOOLEAN,
    categoria_id UUID NOT NULL,
    -- Así se crean las relaciones
    -- primero ponemos un nombre a la relación
    -- luego usamos una columna de la tabla local y creamos la referencia TABLA_FORANEA(COLUMNA)
    CONSTRAINT fk_categorias FOREIGN KEY (categoria_id) REFERENCES categorias(id) -- CONSTRAINT > sirve para indicar que es una llave foranea
);
INSERT INTO productos (nombre, precio, foto, disponible, categoria_id)
VALUES -- Los 3 primeros son de abarrotes
    (
        'Serrucho',
        14.50,
        'https://picsum.photos/200',
        true,
        'a7aa1c9c-de96-4673-a0eb-9a70df853dc6'
    ),
    (
        'Esponja de lavar',
        4.80,
        'https://picsum.photos/200',
        false,
        'a7aa1c9c-de96-4673-a0eb-9a70df853dc6'
    ),
    (
        'Paño de microfibra',
        9.90,
        'https://picsum.photos/200',
        true,
        'a7aa1c9c-de96-4673-a0eb-9a70df853dc6'
    ),
    -- Los 5 son de Limpieza
    (
        'Detergente',
        24.90,
        'https://picsum.photos/200',
        true,
        'd4c077bc-560c-4df1-90ac-e8d42d0257fe'
    ),
    (
        'Cepillo dental',
        12.50,
        'https://picsum.photos/200',
        false,
        'd4c077bc-560c-4df1-90ac-e8d42d0257fe'
    ),
    (
        'Shampoo',
        34.00,
        'https://picsum.photos/200',
        true,
        'd4c077bc-560c-4df1-90ac-e8d42d0257fe'
    ),
    (
        'Cloro',
        5.20,
        'https://picsum.photos/200',
        true,
        'd4c077bc-560c-4df1-90ac-e8d42d0257fe'
    ),
    (
        'Mr. Musculo',
        19.80,
        'https://picsum.photos/200',
        false,
        'd4c077bc-560c-4df1-90ac-e8d42d0257fe'
    ),
    -- Los 4 son de Frutas
    (
        'Uva',
        4.00,
        'https://picsum.photos/200',
        true,
        'd16d3c0b-eed4-4a4d-b435-1e19ea052355'
    ),
    (
        'Manzana',
        2.90,
        'https://picsum.photos/200',
        true,
        'd16d3c0b-eed4-4a4d-b435-1e19ea052355'
    ),
    (
        'Membrillo',
        1.50,
        'https://picsum.photos/200',
        false,
        'd16d3c0b-eed4-4a4d-b435-1e19ea052355'
    ),
    (
        'Kion',
        1.50,
        'https://picsum.photos/200',
        true,
        'd16d3c0b-eed4-4a4d-b435-1e19ea052355'
    );
-- Operador Like e ILIKE
-- Like > respetará las mayusculas y minusculas
SELECT *
FROM productos
WHERE nombre LIKE '%Musculo%';
-- % > sirve para indicar que puede haber cualquier caracter antes o después de la palabra
-- ILIKE > no respetará las mayusculas y minusculas
SELECT *
FROM productos
WHERE nombre ILIKE '%musculo%';
--
SELECT *
FROM productos
WHERE nombre ILIKE '%m%';
-- devolvera los productos que tengan una m en cualquier posición
SELECT *
FROM productos
WHERE nombre ILIKE 'm%';
-- devolvera los productos que empiecen con m
SELECT *
FROM productos
WHERE nombre ILIKE 'm%a%';
-- devolvera los productos que empiecen con m y tengan una a en cualquier posición
SELECT *
FROM productos
WHERE nombre ILIKE 'c_o%';
-- devolvera los productos que empiecen con c y tengan una o en la tercera posición
--Selecciona todos los productos cuyo precio sea menor o igual que 10
SELECT *
FROM productos
WHERE precio <= 10;
-- Selecciona los productos con precio mayor a 10
SELECT *
FROM productos
WHERE precio > 10;
-- Ejercicios
-- 1) Mostrar todos los productos que tengan la letra 'u' o la letra 'e'
SELECT *
FROM productos
WHERE nombre ILIKE '%u%'
    OR nombre ILIKE '%e%';
-- 2) Mostrar todos los productos que esten disponibles y que su precio sea mayor a 10
SELECT *
FROM productos
WHERE disponible = true
    AND precio > 10;
-- 3) Mostrar todos los productos que no esten disponibles o que su precio sea más de 15 o menor que 5
SELECT *
FROM productos
WHERE disponible = 'false'
    OR precio > 15
    OR precio < 5;
-- USO DEL JOIN 
-- LEFT JOIN > devolvera todo lo de la izquierda (categorias) y opcionalemente lo de la derecha (productos)
SELECT *
FROM categorias
    LEFT JOIN productos ON categorias.id = productos.categoria_id;
-- devolvera la categoria aunque no tenga productos
-- INNER JOIN > devolvera todo lo que hay en comun tanto en categorias como en productos
SELECT *
FROM categorias
    INNER JOIN productos ON categorias.id = productos.categoria_id;
-- devolvera la categoria solo si tiene productos
SELECT *
FROM categorias
    RIGHT JOIN productos ON categorias.id = productos.categoria_id;
-- devolvera los productos aunque no tengan categorias
-- EJERCICIOS 
SELECT categorias.nombre
FROM categorias
    LEFT JOIN productos ON categorias.id = productos.categoria_id;
-- devolvera el nombre de la categoria aunque no tenga productos
-- Una manera de aplicar alias a las columnas
SELECT categorias.nombre AS "nombre de la categoria",
    productos.nombre AS "nombre del producto"
FROM categorias
    LEFT JOIN productos ON categorias.id = productos.categoria_id;
-- devolvera el nombre de la categoria y del producto aunque no tenga productos
-- Una manera de aplicar alias a las tablas
SELECT c.nombre AS "nombre de la categoria",
    p.nombre AS "nombre del producto"
FROM categorias AS c
    LEFT JOIN productos AS p ON c.id = p.categoria_id;
-- devolvera el nombre de la categoria y del producto aunque no tenga productos
-- Devolver todos los productos con sus categorias que valgan más que 5 soles y que su estado de la categoria sea verdadero
SELECT *
FROM productos
    INNER JOIN categorias ON productos.categoria_id = categorias.id
WHERE productos.precio > 5
    AND categorias.estado = true;
-- Devolver todas las categorias con sus productos que valgan más que 5 soles y que su estado de la categoria sea verdadero
SELECT *
FROM categorias
    LEFT JOIN productos ON categorias.id = productos.categoria_id
WHERE productos.precio > 5
    AND categorias.estado = true;