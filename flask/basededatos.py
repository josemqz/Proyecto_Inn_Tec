from flask import Flask, render_template
from requests import request
import pyodbc

basededatos = Flask(__name__)
def conectar():
    s = "" #servidor
    d = "Base de Datos"
    u = '' #usuario
    p = '' #contraseña
    cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+s+";DATABASE="+d+";UID="+u+";PWD="+p)
    conn = pyodbc.connect(cnxn)
    return conn

@basededatos.route('/')
def main():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * dbo.TUI")
    tablas=[]
    for row in cursor.fetchall:
        tablas.append({"id_tui":row[0],"rol":row[1],"rut":row[2],"correo":row[3],"apellido1":row[4],"apellido2":row[5],"nombre":row[6],"cod_carrera":row[7],"año_ingreso":row[8]})
    conn.close()
    return render_template('index.html',tablas=tablas)

@basededatos.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'GET'
        return render_template('agregar.html')
    elif request.method == 'POST':
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estudiantes(id_tui,rol,rut,correo,apellido1,apellido2,nombre,cod_carrera,anio_ingreso")
        conn.commit()
        conn.close()
        return render_template('agregar.html')

if (__name__ == '__main__'):
    basededatos.run(debug=True)