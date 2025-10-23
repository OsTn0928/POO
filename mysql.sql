-- =========================================
-- CREACIÓN DE BASE DE DATOS
-- =========================================
CREATE DATABASE IF NOT EXISTS hotel_reservas;
USE hotel_reservas;
-- =========================================
-- TABLA TIPO_CLIENTES
-- =========================================
CREATE TABLE tipo_clientes (
id_tipo_cliente INT AUTO_INCREMENT PRIMARY KEY,
nombre_tipo VARCHAR(50) NOT NULL UNIQUE,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME NULL,
deleted BOOLEAN DEFAULT 0
);
-- =========================================
-- TABLA CLIENTES
-- =========================================
CREATE TABLE clientes (
id_cliente INT AUTO_INCREMENT PRIMARY KEY,
rut VARCHAR(12),
nombre_completo VARCHAR(100) NOT NULL,
correo VARCHAR(100),
telefono VARCHAR(15),
id_tipo_cliente INT NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME NULL,
deleted BOOLEAN DEFAULT 0,
FOREIGN KEY (id_tipo_cliente) REFERENCES tipo_clientes(id_tipo_cliente)
);
-- =========================================
-- TABLA TIPOS_HABITACION
-- =========================================
CREATE TABLE tipos_habitacion (
id_tipo_habitacion INT AUTO_INCREMENT PRIMARY KEY,
nombre_tipo VARCHAR(50) NOT NULL UNIQUE,
precio_noche DECIMAL(10,2) NOT NULL,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME NULL,
deleted BOOLEAN DEFAULT 0

);
-- =========================================
-- TABLA HABITACIONES
-- =========================================
CREATE TABLE habitaciones (
id_habitacion INT AUTO_INCREMENT PRIMARY KEY,
numero_habitacion VARCHAR(10) NOT NULL UNIQUE,
id_tipo_habitacion INT NOT NULL,
estado VARCHAR(20) DEFAULT 'disponible',
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME NULL,
deleted BOOLEAN DEFAULT 0,
FOREIGN KEY (id_tipo_habitacion) REFERENCES tipos_habitacion(id_tipo_habitacion)
);
-- =========================================
-- TABLA PERSONAL
-- =========================================
CREATE TABLE personal (
id_personal INT AUTO_INCREMENT PRIMARY KEY,
nombre_completo VARCHAR(100),
cargo VARCHAR(50),
correo VARCHAR(100),
telefono VARCHAR(15),
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME NULL,
deleted BOOLEAN DEFAULT 0
);
-- =========================================
-- TABLA RESERVAS
-- =========================================
CREATE TABLE reservas (
id_reserva INT AUTO_INCREMENT PRIMARY KEY,
id_cliente INT NOT NULL,
id_habitacion INT NOT NULL,
id_personal INT NOT NULL,
fecha_ingreso DATE,
fecha_salida DATE,
estado VARCHAR(20),
created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
updated_at DATETIME NULL,
deleted BOOLEAN DEFAULT 0,
FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
FOREIGN KEY (id_habitacion) REFERENCES habitaciones(id_habitacion),
FOREIGN KEY (id_personal) REFERENCES personal(id_personal)
);

