import psycopg2
from configuracion.config import config

def insertarMedico(nombre, direccion, telefono, numColegiado, idUsuario,idEspecialidad,idLugarMedico):
    # Ejecutamos una sentencia SQL que inserta una persona nueva en la tabla persona
    sentenciaSQL = """INSERT INTO Medico 
    (nombre, direccion, telefono, numColegiado, idUsuario, idEspecialidad, idLugarMedico)
    VALUES (%s,%s,%s,%s,%s,%s,%s); """

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL,(nombre, direccion, telefono, numColegiado, idUsuario, idEspecialidad, idLugarMedico))
        conn.commit()

        # Cerramos la comunicación con PostgreSQL
        cur.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()

def insertarUsuario(usuario, contrasena, tipousuario):
    # Ejecutamos una sentencia SQL que inserta una persona nueva en la tabla persona
    sentenciaSQL = """INSERT INTO usuario 
    (usuario, contrasena, tipousuario)
    VALUES (%s,%s,%s); """

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL,(usuario, contrasena, tipousuario))
        conn.commit()

        # Cerramos la comunicación con PostgreSQL
        cur.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    finally:
        if conn is not None:
            conn.close()
            
def insertarBodeguero(nombre, idUsuario, idLugarMedico):
    # Ejecutamos una sentencia SQL que inserta una persona nueva en la tabla persona
    sentenciaSQL = """INSERT INTO bodeguero 
    (nombre,idusuario,idlugarMedico)
    VALUES (%s,%s,%s); """

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL,(nombre, idUsuario, idLugarMedico))
        conn.commit()

        # Cerramos la comunicación con PostgreSQL
        cur.close()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
        
    finally:
        if conn is not None:
            conn.close()
            
