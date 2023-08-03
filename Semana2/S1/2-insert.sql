-- DML (Data Manipulation Language)
-- INSERT > Insertar registros
-- UPDATE > Actualizar registros
-- DELETE > Eliminar registros
-- SELECT > Consultar registros

INSERT INTO alumnos(id, nombre, apellidos, correo, fecha_nacimiento, matriculado) VALUES
                    (DEFAULT, 'Juan', 'Perez', 'jperez@gmail.com', '1990-01-01', DEFAULT);

INSERT INTO alumnos(id, nombre, apellidos, correo, fecha_nacimiento, matriculado) VALUES
                    (DEFAULT, 'Rosa', 'Zegarra', 'rosaZ23@gmail.com', '1999-02-01', DEFAULT),
                    (DEFAULT, 'Monica', 'Galindo', 'mongalindo@gmail.com', '1995-03-01', DEFAULT);


