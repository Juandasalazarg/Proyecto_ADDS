
import psycopg2

def agregar_usuario(nombre, usuario, contrasena, email):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("INSERT INTO usuario (nombre, usuario, contraseña, email) VALUES (%s, %s, %s, %s)",
                       (nombre, usuario, contrasena, email))
        connection.commit()

    finally:
        cursor.close()
        connection.close()

def borrar_usuario(usuario, contrasena):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("DELETE FROM Usuario WHERE usuario = %s AND contraseña = %s", (usuario, contrasena))
        connection.commit()

    finally:
        cursor.close()
        connection.close()

def actualizar_usuario(usuario, nombre, nuevo_usuario, nueva_contrasena, nuevo_email):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("UPDATE Usuario SET nombre = %s, usuario = %s, contraseña = %s, email = %s WHERE usuario = %s",
                       (nombre, nuevo_usuario, nueva_contrasena, nuevo_email, usuario))
        connection.commit()

    finally:
        cursor.close()
        connection.close()

def consultar_usuario(usuario):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Usuario WHERE usuario = %s", (usuario,))
        user_data = cursor.fetchone()

        if user_data:
            return user_data  # Devuelve la información del usuario como una tupla
        else:
            return None  # Retorna None si no se encuentra ningún usuario con ese nombre de usuario

    finally:
        cursor.close()
        connection.close()
