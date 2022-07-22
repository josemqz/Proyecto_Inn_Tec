from flask import Flask, render_template, request
# from requests import request
#import pyodbc
import json
import mysql.connector

basededatos = Flask(__name__)
def conectar():
    configDB = {
        'user': 'inntec',
        'password': '123456',
        'host': 'localhost',
        'database':'inn_tec_db'
    }
    conn = mysql.connector.connect(**configDB)
    return conn

@basededatos.route('/verificar', methods=['GET']) 
def main():

    conn = conectar()
    if not conn.is_connected():
        print("Error en conexion de base de datos")
        exit(1)
    print("Base de datos conectada")
    cursor = conn.cursor()

    # obtener estudiante id a partir de uid de TUI
    print(request.args.get("uid"))
    query = cursor.execute("SELECT * FROM estudiantes WHERE id_tui=" + str(request.args.get("uid")))
    
    estudiante = cursor.fetchall()
    print("estudiante:", estudiante)
    if estudiante == []:
        print("Estudiante no encontrado")
        cursor.close()
        conn.close()
        return {"valido":0, "nombre":"juanito" , "apellido1":"eeeeehh", "rol":"2025157516-1"}

    estudiante = estudiante[0]
    print("estudiante id:", estudiante.id)

    # verificar 
    cursor.execute("SELECT valido FROM pase_usm WHERE estudiante_id = " + estudiante.id)
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
    basededatos.run(debug=True, host='0.0.0.0')