from flask import Flask, render_template, request
# from requests import request
import pyodbc
import json

basededatos = Flask(__name__)
def conectar():
    s = "" #servidor
    d = "Base de Datos"
    u = '' #usuario
    p = '' #contraseña
    cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER="+s+";DATABASE="+d+";UID="+u+";PWD="+p)
    conn = pyodbc.connect(cnxn)
    return conn

@basededatos.route('/verificar', methods=['GET']) 
def verificar():

    conn = conectar()
    cursor = conn.cursor()

    # obtener estudiante id a partir de uid de TUI
    query = cursor.execute("SELECT * FROM estudiante WHERE uid = %s", request.args.get("uid"))
    if query == 0:
        print("Estudiante no encontrado")
        cursor.close()
        conn.close()
        return {"valido":0, "nombre":"juanito" , "apellido1":"eeeeehh", "rol":"2025157516-1"}
    
    estudiante = cursor.fetchall()[0]
    print("estudiante id:", estudiante.id)

    # verificar 
    cursor.execute("SELECT valido FROM pase_usm WHERE estudiante_id = %s", estudiante.id)
    valido = cursor.fetchall()[0]
    
    print("validez:", valido)

    cursor.close()
    conn.close()
    return {"valido":valido, "nombre":"juanito" , "apellido1":"eeeeehh", "rol":"2025157516-1"}
    #return json.dumps()        


"""
@basededatos.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'GET':
        return render_template('agregar.html')
    elif request.method == 'POST':
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estudiantes(id_tui,rol,rut,correo,apellido1,apellido2,nombre,cod_carrera,anio_ingreso")
        conn.commit()
        conn.close()
        return render_template('agregar.html')
"""

if (__name__ == '__main__'):
    basededatos.run(debug=True)