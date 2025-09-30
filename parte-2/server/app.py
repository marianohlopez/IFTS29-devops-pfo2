from flask import Flask, request, jsonify, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "password")
DB_NAME = os.getenv("DB_NAME", "usuariosdb")

# Inicializar BD


def init_db():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.close()
    conn.close()

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            usuario VARCHAR(50) UNIQUE NOT NULL,
            contraseña VARCHAR(255) NOT NULL
        )
    """)
    conn.commit()
    cursor.close()
    conn.close()


init_db()

# Registro


@app.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({"error": "Faltan datos"}), 400

    hash_pass = generate_password_hash(contraseña)

    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (%s, %s)",
                       (usuario, hash_pass))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    except mysql.connector.Error:
        return jsonify({"error": "El usuario ya existe o error en DB"}), 400

# Login


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    contraseña = data.get("contraseña")

    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute(
        "SELECT contraseña FROM usuarios WHERE usuario = %s", (usuario,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row and check_password_hash(row[0], contraseña):
        return jsonify({"mensaje": f"Bienvenido {usuario}"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# Tareas


@app.route("/tareas", methods=["GET"])
def tareas():
    html = """
    <html>
        <head><title>Tareas</title></head>
        <body>
            <h1>Bienvenido a la gestión de tareas</h1>
        </body>
    </html>
    """
    return render_template_string(html)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
