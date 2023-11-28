from flask import Flask, render_template, request

app = Flask(__name__)

# Diccionario global con nombres de usuario y contraseñas válidas
usuarios_validos = {'joel': '1234', 'admin': 'admin1234'}

@app.route('/formulari', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Obtener datos del formulario
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        # Verificar si el usuario y la contraseña son válidos
        if usuario in usuarios_validos and usuarios_validos[usuario] == contrasena:
            # Respuesta OK si las credenciales son válidas
            return f'OK: Bienvenido, {usuario}!'
        else:
            # Respuesta ERROR si las credenciales son inválidas
            return 'ERROR: Credenciales inválidas. Vuelve a intentarlo.'

    # Si el método es GET, mostrar el formulario
    return '''
        <form method="post" action="/formulari">
            <label for="usuario">Usuario:</label>
            <input type="text" id="usuario" name="usuario" required><br>
            <label for="contrasena">Contraseña:</label>
            <input type="password" id="contrasena" name="contrasena" required><br>
            <input type="submit" value="Iniciar sesión">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)

