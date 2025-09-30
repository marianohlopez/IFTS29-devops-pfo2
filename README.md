# PARTE 2 - Proyecto Flask + MySQL + Cliente en Docker

Este proyecto implementa una API en Flask conectada a una base de datos MySQL, junto con un cliente Python interactivo que permite registrar usuarios, iniciar sesión y acceder a una página de tareas.

Todo está contenerizado con Docker y Docker Compose.

---

## 🖥️ Servicios

### 🔹 Servidor Flask (`server/app.py`)

- Expuesto en `http://localhost:5000`
- Endpoints:
  - `POST /registro` → Registra usuario en la BD
  - `POST /login` → Verifica credenciales
  - `GET /tareas` → Devuelve página HTML

### 🔹 Base de datos MySQL

- Imagen oficial: `mysql:8.0`
- Credenciales configuradas en `docker-compose.yml`:
  - Usuario: `user`
  - Password: `password`
  - Base de datos: `usuariosdb`

### 🔹 Cliente Python (`client/client.py`)

Aplicación de consola que permite:

1. Registrar usuario
2. Iniciar sesión
3. Ver tareas

---

## ⚙️ Ejecución

### Construir y levantar los contenedores

- docker-compose up --build

### Ejecutar el cliente por consola

- docker-compose run client

### Puertos utilizados

- Servidor Flask → localhost:5000

- Base de datos MySQL → localhost:3306

### Problemas y soluciones

- Problema: Al iniciar el servidor Flask, la base de datos no estaba lista aún.
- Solución: Se usó depends_on en docker-compose.yml para garantizar que db se levante antes que server.

### Imagenes:

![images](assets/images.png)

![containers](assets/containers.png)
