from flask import Flask
import mysql.connector
import os

app = Flask(__name__)

# --- Configuración de la Conexión a la Base de Datos ---
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'mi-clave-secreta')
DB_NAME = os.getenv('DB_NAME', 'db_parte1')

# --- Definición de la Ruta Principal ---
@app.route('/')
def mostrar_registros():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        cursor.execute("SELECT mensaje FROM registros")
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        
        html_output = "<h1>Conexión Exitosa</h1>"
        html_output += "<h2>Mensaje recuperado de la Base de Datos MySQL:</h2><ul>"
        for row in rows:
            html_output += f"<li>{row[0]}</li>"
        html_output += "</ul>"
        return html_output

    except Exception as e:
        return f"<h1>Error de Conexión</h1><p>No se pudo conectar a la base de datos. Error: {e}</p>"

# --- Punto de Entrada para Ejecutar la Aplicación ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)