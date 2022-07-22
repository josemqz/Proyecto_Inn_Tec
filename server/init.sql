CREATE DATABASE IF NOT EXISTS inn_tec_db;
USE inn_tec_db;

CREATE TABLE IF NOT EXISTS estudiantes
    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_tui INT NOT NULL,
    rol VARCHAR(20) NOT NULL,
    rut VARCHAR(20) NOT NULL,
    correo VARCHAR(255),
    apellido1 VARCHAR(100),
    apellido2 VARCHAR(100),
    nombre VARCHAR(100) NOT NULL,
    cod_carrera INT NOT NULL,
    anio_ingreso INT
    );

CREATE TABLE IF NOT EXISTS pase_usm
    (id INTEGER PRIMARY KEY AUTO_INCREMENT,
    estudiante_id INT,
    FOREIGN KEY (estudiante_id) REFERENCES estudiantes(id),
    valido BOOLEAN NOT NULL,
    fecha_ultima_vac DATE NOT NULL
    );