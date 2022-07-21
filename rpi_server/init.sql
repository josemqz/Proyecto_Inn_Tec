CREATE DATABASE IF NOT EXISTS inn_tec_db;
USE inn_tec_db;

CREATE TABLE IF NOT EXISTS estudiantes
    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
    rol VARCHAR(255) NOT NULL,
    rut VARCHAR(20) NOT NULL,
    apellido1 VARCHAR(100),
    apellido2 VARCHAR(100),
    nombre VARCHAR(100) NOT NULL,
    carrera VARCHAR(255) NOT NULL,
    anio_ingreso INT
    );

CREATE TABLE IF NOT EXISTS pase_usm
    (id INTEGER PRIMARY KEY AUTO_INCREMENT ,
    alumno_id INTEGER FOREIGN KEY REFERENCES estudiantes(id),
    fecha_ultima_vac DATE NOT NULL,
    valido BOOLEAN NOT NULL,
    );