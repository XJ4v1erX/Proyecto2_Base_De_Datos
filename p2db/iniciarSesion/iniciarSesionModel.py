
import psycopg2
from configuracion.config import config


def consultarCuenta(usuario, contrasena):
    
    sentenciaSQL = """SELECT tipousuario FROM usuario
    WHERE usuario = %s AND contrasena = %s;""" 
    
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de usuario y contraseña como parámetros
        cur.execute(sentenciaSQL, (usuario, contrasena))

        # Obtenemos el resultado de la consulta
        result = cur.fetchone()

        # Si hay un resultado, devuelve el tipo de usuario. De lo contrario, devuelve None.
        return result[0] if result else None

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
            
def consultarIdCuentaMedico(usuario, contrasena):
    
    sentenciaSQL = """
        SELECT m.idmedico 
        FROM usuario u 
        JOIN medico m ON u.idusuario = m.idusuario 
        WHERE u.usuario = %s AND u.contrasena = %s;
    """
    
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de usuario y contraseña como parámetros
        cur.execute(sentenciaSQL, (usuario, contrasena))

        # Obtenemos el resultado de la consulta
        result = cur.fetchone()

        # Si hay un resultado, devuelve el ID del médico. De lo contrario, devuelve None.
        return result[0] if result else None

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def consultarIdCuenta(usuario, contrasena):
    
    sentenciaSQL = """SELECT idusuario FROM usuario
    WHERE usuario = %s AND contrasena = %s;""" 
    
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de usuario y contraseña como parámetros
        cur.execute(sentenciaSQL, (usuario, contrasena))

        # Obtenemos el resultado de la consulta
        result = cur.fetchone()

        # Si hay un resultado, devuelve el tipo de usuario. De lo contrario, devuelve None.
        return result[0] if result else None

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def consultarIdCuentaBodeguero(usuario, contrasena):
    
    sentenciaSQL = """SELECT Bodeguero.idBodeguero
                        FROM Usuario
                        JOIN Bodeguero ON Usuario.idUsuario = Bodeguero.idUsuario
                        WHERE Usuario.usuario::text = %s AND Usuario.contrasena = %s;""" 
    
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de usuario y contraseña como parámetros
        cur.execute(sentenciaSQL, (str(usuario), contrasena))

        # Obtenemos el resultado de la consulta
        result = cur.fetchone()

        # Si hay un resultado, devuelve el id del bodeguero. De lo contrario, devuelve None.
        return result[0] if result else None

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def consultarIdLugarMedico(idUsuario):
    sentenciaSQL = """SELECT idLugarMedico FROM LugarMedico
                        WHERE idLugarMedico IN 
                        (SELECT idLugarMedico FROM Bodeguero WHERE idUsuario = %s);"""
    
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando el valor de idUsuario como parámetro
        cur.execute(sentenciaSQL, (idUsuario,))

        # Obtenemos el resultado de la consulta
        result = cur.fetchone()

        # Si hay un resultado, devuelve el idLugarMedico. De lo contrario, devuelve None.
        if result is not None:
            return result[0]
        else:
            print(f"No se encontró ningún idLugarMedico para el usuario con idUsuario = {idUsuario}")
            return None

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def set_app_user_session(usuario):
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Seteamos la variable de sesión my.app_user con el valor de idUsuario
        cur.execute(f"SET my.app_user = '{usuario}'")

        # Verificamos si se seteó la variable de sesión
        cur.execute("SELECT current_setting('my.app_user')")
        app_user = cur.fetchone()[0]
        print(f"Se seteó la variable de sesión my.app_user con el valor: {app_user}")

        # Cerramos la comunicación con PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()