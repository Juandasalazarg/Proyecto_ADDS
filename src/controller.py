# app.py
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import sys
from models import agregar_usuario, consultar_usuario, borrar_usuario, actualizar_usuario

app = Flask(__name__)

@app.route('/')
def inicio_sesion():
    return render_template('inicio_sesion.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        email = request.form['email']
       
        # inserción en la base de datos
        agregar_usuario(nombre, usuario, contrasena, email)
        
        return redirect(url_for('inicio_sesion'))  # Redirige a la página de inicio de sesión

    return render_template('registro.html')

@app.route('/inicio_sesion', methods=['GET', 'POST'])
def iniciar_sesion():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']
        
        # Simulación de autenticación en la base de datos
        user_data = consultar_usuario(usuario)
        if user_data and user_data[2] == contrasena:  # Supone que la contraseña está en el tercer índice
            print("Usuario inició sesión:", usuario, contrasena, file=sys.stdout)
            # Aquí podrías redirigir a otra página o realizar alguna acción adicional
            return redirect(url_for('inicio_sesion'))  # Redirige a la página de inicio de sesión
        else:
            return "Usuario o contraseña incorrectos"  # Devuelve un mensaje de error

    return render_template('inicio_sesion.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == "__main__":
    app.run(debug=True)
