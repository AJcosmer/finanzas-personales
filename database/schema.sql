CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255)
);

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50)
);

CREATE TABLE movimientos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    categoria_id INT,
    tipo ENUM('ingreso','gasto'),
    monto DECIMAL(10,2),
    descripcion TEXT,
    fecha DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);
