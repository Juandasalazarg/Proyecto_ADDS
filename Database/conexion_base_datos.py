import psycopg2

def agregar_usuario(id, nombre, usuario, contraseña, email):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("INSERT INTO usuario (id, nombre, usuario, contraseña, email) VALUES (%s, %s, %s, %s, %s)",
                       (id, nombre, usuario, contraseña, email))
        connection.commit()

    finally:
        cursor.close()
        connection.close()



def borrar_usuario(id):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("DELETE FROM Usuario WHERE id = %s", (id,))
        connection.commit()

    finally:
        cursor.close()
        connection.close()


def actualizar_usuario(id, nombre, usuario, contraseña, email):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("UPDATE Usuario SET nombre = %s, usuario = %s, contraseña = %s, email = %s WHERE id = %s",
                       (nombre, usuario, contraseña, email, id))
        connection.commit()

    finally:
        cursor.close()
        connection.close()




def consultar_usuario(id):
    try:
        connection = psycopg2.connect(
            host='localhost',
            user='postgres',
            password='123456789',
            database='Proyecto_ADDS'
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM Usuario WHERE id = %s", (id,))
        user_data = cursor.fetchone()

        if user_data:
            return user_data  # Devuelve la información del usuario como una tupla
        else:
            return None  # Retorna None si no se encuentra ningún usuario con ese id

    finally:
        cursor.close()
        connection.close()


