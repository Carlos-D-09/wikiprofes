from conexionbaseDatos import cursor, bd #Archivo de conexiones
import hashlib, mysql.connector

def existeUsuario(correo):
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:                #Evalua la existencia del usuario mediante el correo
        return True

    return False

def existeProfesor(correo):
    query = "SELECT COUNT(*) FROM maestro WHERE correo = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:                #Evalua la existencia del profesor(usuario) mediante el correo
        return True

    return False

def crearUsuario(nombres, apellidos, correo, contra):
    if existeUsuario(correo) == True:
        return False
    else:
        h = hashlib.new("sha256", bytes(contra, "utf-8"))
        h = h.hexdigest()                                   #La creacion del usuario y su insercion en la BD 
        insertar = "INSERT INTO usuario \
                    (Nombre(s), Apellido(s), correo, key) \
                    VALUES(%s, %s, %s, %s)"
        cursor.execute(insertar, (correo, h))

        return True

def crearUsuarioProfesor(nombres, apellidos, correo, contra):
    if existeProfesor(correo) == True:
        return False
    else:
        h = hashlib.new("sha256", bytes(contra, "utf-8"))
        h = h.hexdigest()                                   #La creacion del profesor(usuario) y su insercion en la BD
        insertar = "INSERT INTO maestro \
                    (Nombre(s), Apellido(s), correo, key) \
                    VALUES(%s, %s, %s, %s)"
        cursor.execute(insertar, (correo, h))

        return True

def iniciarSesionUsuario(correo, contra):
    h = hashlib.new("sha256", bytes(contra, "utf-8"))
    h = h.hexdigest()
    query = "SELECT id FROM usuario WHERE correo = %s AND user_key = %s"
    cursor.execute(query, (correo, h))
    consulta = cursor.fetchone()
    if consulta:                                            #Inicio de sesion del usuario mediante correo y contraseña
        usuario = {
            'Id' : consulta[0],
            'Nombre(s)' : consulta[1],
            'Apellido(s)' : consulta[2],
            'Correo' : consulta[3]
        }
        return usuario
    
    else:
        return False

def iniciarSesionProfesor(correo, contra):
    h = hashlib.new("sha256", bytes(contra, "utf-8"))
    h = h.hexdigest()
    query = "SELECT id FROM maestro WHERE correo = %s AND user_key = %s"
    cursor.execute(query, (correo, h))
    consulta = cursor.fetchone()                            #Inicio de sesion del profesor(usuario) mediante correo y contraseña
    if consulta:
        maestro = {
            'Id' : consulta[0],
            'Nombre(s)' : consulta[1],
            'Apellido(s)' : consulta[2],
            'Correo' : consulta[3]
        }
        return maestro

    else:
        return False

def add_profesor(profesor):
    nombre = profesor['nombre']
    NRC = profesor['NRC']
    codigo_materia = profesor['codigo_materia']         #Añadir profesor(no usuario) a evaluar mediante el nombre, NRC, codigo y promedio.
    promedio = profesor['promedio']

    insertar = "INSERT INTO profesor \
        (nombre, NRC, codigo_materia, promedio) \
        VALUES (%s, %s, %s, %s)"
    
    cursor.execute(insertar, 
    (nombre, NRC, codigo_materia, promedio))
    bd.commit()

    if cursor.rowcount:
        return True
    else: 
        return False

def get_profesores():
    query = "SELECT id, nombre, NRC, codigo_materia, promedio"
    cursor.execute(query)
    profesores = []
    for row in cursor.fetchall():
        profesor = {
            'id': row[0],
            'nombre': row[1],                           #Obtener informacion de todos los profesores(no usuario) registrados.
            'NRC': row[2],
            'promedio': row[3]
        }
        profesores.append(profesor)

    return profesores

def modificar_profesor(id, columna, valor):
    update = f"UPDATE profesor SET {columna} = %s WHERE id = %s"
    cursor.execute(update, (valor, id))
    bd.commit()

    if cursor.rowcount:                                 #Modificar la informacion del profesor por si hubo algun error
        return True
    else: 
        return False

def eliminar_profesor(id):
    eliminar = "DELETE from profesor WHERE id = %s"
    cursor.execute(eliminar, (id,))
    bd.commit()

    if cursor.rowcount:                                 #Eliminar profesor(no usuario) de la base de datos por si hubo algun error
        return True
    else:
        return False
    