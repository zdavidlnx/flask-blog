# blog.py -- controller

# imports

from flask import Flask, render_template, request, session, flash, redirect, url_for
import sqlite3

# Configuación
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = b'L\xe8Q\x93Y\xb4\x86rn(\xad\xeex7\x8ck\x03umD\x9e"r#'


app = Flask(__name__)

# Se coge la configuración de la aplicación buscando variables en MAYUSCULAS
app.config.from_object(__name__)


# Conexión con la BBDD
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    status_code = 200
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or request.form['passowrd'] != app.config['PASSWORD']:
            error = 'Credenciales no válidas. Pruebe de nuevo.'
            status_code = 401
        else:
            session['logged_in'] = True
            return redirect(url_for('main'))

    return render_template('login.html', error=error), status_code


@app.route('/main')
def main():
    return render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
