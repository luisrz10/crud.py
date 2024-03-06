from flask import Flask 
from flask_cors import CORS
from flask import jsonify, request 
import pymysql

app=Flask(__name__)

CORS (app)

def addcors(response):
    response.headers['access-control-allow-origin'] = '*'
    response.headers['access-control-allow-origin'] = 'options, GET, POST, DELETE'
    return response

def conectar (vhost, vuser, vpass, vdb):

    conn = pymysql.connect(host=vhost, user=vuser, passwd=vpass, db=vdb, charset = 'utf8mb4')
    return conn


@app.route("/")
def consulta_general():

    try:
        conn=conectar('localhost', 'root', '','gestor_contrasena')
        cur = conn.cursor()
        cur.execute(""" SELECT * FROM baul """)
        datos = cur.fetchall()
        data=[]

        for row in datos:
            dato={'id_baul': row[0], 'plataforma': row[1], 'usuario': row[2], 'clave' :row[3]} 
            data.append(dato)

        cur.close()
        conn.close()
        return jsonify({'baul': data, 'mensaje': 'Baul de contraseñas'})

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})

@app.get("/consulta_individual/<codigo>") 
def consulta_individual(codigo):

    try:
        conn=conectar('localhost', 'root', '','gestor_contrasena')
        cur = conn.cursor() 
        cur.execute(""" SELECT * FROM baul where id_baul='{0}' """.format(codigo))

        datos=cur.fetchone()
        cur.close()
        conn.close()

        if datos!= None:
            dato={'id_baul':datos[0], 'plataforma':datos[1], 'usuario':datos[2], 'clave':datos[3]} 
            return jsonify({'baul': dato, 'mensaje': 'Registro encontrado'})

        else:
            return jsonify({'mensaje': 'Registro no encontrado'})

    except Exception as ex:

        return jsonify({'mensaje': 'Error'})

@app.post("/registro/")
def registro():
    try:
        conn = conectar('localhost', 'root', '', 'gestor_contrasena')
        cur = conn.cursor()
        query = "insert into baul (plataforma, usuario, clave) values \
            ('{0}', '{1}', '{2}')".format(request.json['plataforma'], request.json['usuario'], request.json['clave'])
        x=cur.execute(query)
        conn.commit()
        cur.close() 
        conn.close()

        return jsonify({'mensaje': 'Registro agregado'})

    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error'})

@app.delete("/eliminar/<codigo>")
def eliminar (codigo):
    try:
        conn=conectar('localhost', 'root', '', 'gestor_contrasena')
        cur = conn.cursor()
        x=cur.execute(""" delete from baul where id_baul={0}""".format(codigo))
        conn.commit()
        cur.close()
        conn.close()

        return jsonify({'mensaje': 'eliminado'})

    except Exception as ex:

        print(ex)

        return jsonify({'mensaje': 'Error'})

@app.put("/actualizar/<codigo>")
def actualizar (codigo):
    try:
        conn=conectar('localhost', 'root', '', 'gestor_contrasena') 
        cur = conn.cursor()
        query = query = "update baul set plataforma='{0}', usuario='{1}',clave='{2}' where id_baul={3}""".format(request.json['plataforma'], request.json['usuario'], request.json['clave'], codigo)
        x=cur.execute(query)

        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Registro Actualizado'})
        
    except Exception as ex:

        print(ex)

        return jsonify({'mensaje': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)