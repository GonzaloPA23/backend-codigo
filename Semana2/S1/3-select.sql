-- Hacer uso del SELECT 

SELECT nombre,correo FROM alumnos;
SELECT * FROM alumnos;

-- Para agregar filtros usamos la clausula WHERE
SELECT * FROM alumnos WHERE matriculado = true;

-- Para agregar mas de un filtro usamos AND
-- El texto debe ir entre comillas simples, ya que las dobles se usan para definir nombres de tablas con caracteres especiales o bases de datos
SELECT * FROM alumnos WHERE matriculado = true AND nombre = 'Juan';

-- Listar los nombres y fecha de nacimiento de los alumnos que sean Maria Roberto o Maximo 
SELECT nombre,fecha_nacimiento FROM alumnos WHERE nombre = 'Maria' OR nombre = 'Roberto' OR nombre = 'Maximo';

-- IN > Para simplificar la consulta anterior podemos usar IN
SELECT nombre,fecha_nacimiento FROM alumnos WHERE nombre IN ('Maria','Roberto','Maximo');

-- Devolver todos los alumnos que estén matriculados y que su nombre sea Juanito o su apellido sea Tari Ramos
SELECT * FROM alumnos WHERE matriculado = true AND (nombre = 'Juan' OR apellidos = 'Tari Ramos');
