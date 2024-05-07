CREATE TABLE Usuario (
    id VARCHAR(20) PRIMARY KEY,
    nombre VARCHAR(50),
    usuario VARCHAR(50) UNIQUE,
    contraseña VARCHAR(15),
    email VARCHAR(30) UNIQUE
);


