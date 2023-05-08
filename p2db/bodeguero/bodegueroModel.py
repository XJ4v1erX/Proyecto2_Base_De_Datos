

import psycopg2
from configuracion.config import config

def consultaInventario(idLugarMedico, idBodeguero):    
    # Define la consulta SQL que deseas ejecutar
    sentenciaSQL = """
        SELECT Suministro.nombre, Inventario.cantidad, Inventario.expiracion
        FROM Inventario
        INNER JOIN Suministro ON Inventario.idSuministro = Suministro.idSuministro
        INNER JOIN LugarMedico ON Inventario.idLugarMedico = LugarMedico.idLugarMedico
        INNER JOIN Bodeguero ON LugarMedico.idLugarMedico = Bodeguero.idLugarMedico
        INNER JOIN Usuario ON Bodeguero.idUsuario = Usuario.idUsuario
        WHERE LugarMedico.idLugarMedico = %s AND Bodeguero.idLugarMedico = %s
        ORDER BY Inventario.cantidad;
    """

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL, (idLugarMedico, idBodeguero))
        rows = cur.fetchall()

        # Mostramos la cantidad de resultados obtenidos
        print("Cantidad de elementos en inventario: ", cur.rowcount)

        # Retornamos los resultados
        return rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



def consultaAlertas(idLugarMedico, IdBodeguero):
    # Define la consulta SQL que deseas ejecutar
    sentenciaSQL = """
        SELECT Suministro.nombre, Inventario.cantidad, Inventario.expiracion
        FROM Inventario
        INNER JOIN Suministro ON Inventario.idSuministro = Suministro.idSuministro
        INNER JOIN LugarMedico ON Inventario.idLugarMedico = LugarMedico.idLugarMedico
        INNER JOIN Bodeguero ON LugarMedico.idLugarMedico = Bodeguero.idLugarMedico
        INNER JOIN Usuario ON Bodeguero.idUsuario = Usuario.idUsuario
        WHERE LugarMedico.idLugarMedico = %s AND Bodeguero.idLugarMedico = %s AND Inventario.cantidad <= 15 OR Inventario.expiracion <= CURRENT_DATE + INTERVAL '30 days'
        ORDER BY Inventario.cantidad;"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL, (idLugarMedico, IdBodeguero))
        rows = cur.fetchall()

        # Devolvemos los resultados
        return rows

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

            
def insertarSuministro(idSuministro, idLugarMedico, cantidad, expiracion):
    # Define la consulta SQL que deseas ejecutar
    sentenciaSQL = """
        INSERT INTO Inventario (idSuministro, idLugarMedico, cantidad, expiracion)
        VALUES (%s, %s, %s, %s);
    """

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL, (idSuministro, idLugarMedico, cantidad, expiracion))
        
        # Mostramos la cantidad de resultados obtenidos
        print("Cantidad de elementos en inventario: ", cur.rowcount)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def actualizarCantida(idSuministro, idLugarMedico, cantidad):
    # Define la consulta SQL que deseas ejecutar
    sentenciaSQL = """
        UPDATE Inventario
        SET cantidad = %s
        WHERE idSuministro = %s AND idLugarMedico = %s
    """

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL, (cantidad, idSuministro, idLugarMedico))
        conn.commit()

        # Verificamos si se actualizó alguna fila
        if cur.rowcount == 0:
            print("No se encontró el suministro en el lugar médico especificado.")
            return False
        else:
            print("Se actualizó la cantidad del suministro en el lugar médico especificado.")
            return True

        # Cerramos la comunicación con PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()