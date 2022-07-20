CREATE DATABASE IF NOT EXISTS inn_tec_db;
USE inn_tec_db;
CREATE TABLE IF NOT EXISTS estudiantes
    (id INTEGER PRIMARY KEY,
    rol VARCHAR(255),
    rut VARCHAR(255),
    apellido1 VARCHAR(255),
    apellido2 VARCHAR(255),
    carrera VARCHAR(255),
    anio_ingreso INT);

CREATE TABLE IF NOT EXISTS pase_usm
    (id INTEGER PRIMARY KEY,
    alumno_id INTEGER FOREIGN KEY,
    fecha_ultima_vac DATE,
    valido BOOLEAN,
    );