-- Active: 1709726230832@@127.0.0.1@3306@gestor_contrasena
CREATE DATABASE IF NOT EXISTS gestor_contrasena;
use gestor_contrasena; 
CREATE TABLE `baul` (
`id_baul` int NOT NULL AUTO_INCREMENT,
`plataforma` varchar(80) NOT NULL,
`usuario` varchar(80) NOT NULL,
`clave` varchar(80) NOT NULL,
PRIMARY KEY (`id_baul`),
UNIQUE KEY `Plataforma` (`Plataforma`,`usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4;

SELECT * FROM baul;

INSERT INTO baul (plataforma, usuario, clave) VALUES ('MySpace', 'MrA', '1234');
INSERT INTO baul (plataforma, usuario, clave) VALUES ('Tuenti', 'MrB', '5678');
INSERT INTO baul (plataforma, usuario, clave) VALUES ('Hi5', 'MrX', '9032');
INSERT INTO baul (plataforma, usuario, clave) VALUES ('Orkut', 'MrZ', '8596');