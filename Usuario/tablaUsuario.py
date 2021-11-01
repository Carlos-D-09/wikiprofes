from conexionbaseDatos import cursor, bd
import hashlib

def existeUsuario(correo):
    query = "SELECT COUNT(*) FROM usuario WHERE correo = %s"
    cursor.execute(query, (correo,))

    if cursor.fetchone()[0] == 1:
        return True

    return False

def crearUsuario(nombres, apellidos, correo, contra):
    if existeUsuario(correo) == True:
        return False
    else:
        h = hashlib.new("sha256", bytes(contra, "utf-8"))
        h = h.hexdigest()
        insertar = "INSERT INTO usuario \
                    (Nombre(s), Apellido(s), correo, key) \
                    VALUES(%s, %s, %s, %s,)"
        cursor.execute(insertar, (correo,h))

        return True

def iniciarSesion(correo, contra):
    h = hashlib.new("sha256", bytes(contra, "utf-8"))
    h = h.hexdigest()
    query = "SELECT id FROM usuario WHERE correo = %s AND user_key = %s"
    cursor.execute(query, (correo, h))
    consulta = cursor.fetchone()
    if consulta:
        usuario = {
            'Id' : consulta[0],
            'Nombre(s)' : consulta[1],
            'Apellido(s)' : consulta[2],
            'Correo' : consulta[3],
        }
        return usuario
    
    else:
        return False