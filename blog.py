# blog.py -- controller

# imports

from flask import Flask, render_template, request, session, flash, redirect, url_for
import sqlite3

# Configuación
DATABASE = 'blog.db'


app = Flask(__name__)

# Se coge la configuración de la aplicación buscando variables en MAYUSCULAS
app.config.from_object(__name__)


# Conexión con la BBDD
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


@app.route('/')
def login():
    return render_template('login.html')

@app.route('/main')
def main():
    return  render_template('main.html')

if __name__ == '__main__':
    app.run(debug=True)
