
import psycopg2
from configuracion.config import config


from collections import namedtuple

def consultaPaciente(idPaciente):
    sentenciaSQL = "SELECT * FROM Paciente WHERE idPaciente = %s;"
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando el ID del paciente como parámetro
        cur.execute(sentenciaSQL, (idPaciente,))

        # Obtenemos el resultado de la consulta como un objeto "row"
        row = cur.fetchone()

        # Si la consulta no devuelve resultados, devolvemos None
        if not row:
            return None

        # Creamos un objeto "namedtuple" a partir de los campos de la tabla
        campos = [desc[0] for desc in cur.description]
        Paciente = namedtuple('Paciente', campos)

        # Devolvemos el resultado como un diccionario
        return Paciente(*row)._asdict()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    
def insertarPaciente(nombre, direccion, telefono, masaCorporal, altura, adicciones):
    # Sentencia SQL para insertar un nuevo paciente
    sentenciaSQL = """INSERT INTO Paciente(nombre, direccion, telefono, masaCorporal, altura, adicciones)
                    VALUES (%s, %s, %s, %s, %s, %s) RETURNING idPaciente;"""
    
    # Conectarse a la base de datos
    conn = None
    try:
        # Obtener los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        
        # Ejecutar la sentencia SQL
        cur.execute(sentenciaSQL, (nombre, direccion, telefono, masaCorporal, altura, adicciones))
        
        # Obtener el ID del paciente recién insertado
        id_paciente = cur.fetchone()[0]
        
        # Confirmar la transacción
        conn.commit()
        
        # Devolver el ID del paciente recién insertado
        return id_paciente
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        # Cerrar la conexión a la base de datos
        if conn is not None:
            conn.close()
    
def actualizarPaciente(idPaciente, nombre, direccion, telefono, masaCorporal, altura, adicciones):
    """ Actualiza la información de un paciente existente en la base de datos"""
    
    sentenciaSQL = """UPDATE Paciente
                            SET nombre = %s, 
                            direccion = %s, 
                            telefono = %s, 
                            masaCorporal = %s, 
                            altura = %s, 
                            adicciones = %s
                        WHERE idPaciente = %s;"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como argumentos
        cur.execute(sentenciaSQL, (nombre, direccion, telefono, masaCorporal, altura, adicciones, idPaciente))

        # Realizamos la confirmación de la transacción
        conn.commit()

        # Obtenemos el número de filas afectadas por la consulta
        row_count = cur.rowcount

        # Imprimimos el número de filas afectadas
        print(f"Se actualizaron {row_count} filas.")
        
        # Verificamos si se actualizaron filas
        if row_count > 0:
            return True
        else:
            return False

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            


def consultaHistorial(idHistorial):
    # Sentencia SQL para obtener un historial médico
    sentenciaSQL = """SELECT * FROM HistorialMedico WHERE idHistorial = %s"""
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL, (idHistorial,))

        # Obtenemos los resultados de la consulta
        row = cur.fetchone()

        # Creamos un objeto "namedtuple" a partir de los campos de la tabla
        campos = [desc[0] for desc in cur.description]
        Paciente = namedtuple('Historial', campos)

        # Devolvemos el resultado como un diccionario
        return Paciente(*row)._asdict()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            
def insertarHistorial(fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico):
    
    # Sentencia SQL para insertar el historial médico en la base de datos
    sentenciaSQL = """INSERT INTO HistorialMedico (fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico))

        # Confirmamos los cambios en la base de datos
        conn.commit()

        # Cerramos la conexión
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    
    finally:
        if conn is not None:
            conn.close()
            
def actualizarHistorial(idHistorial, fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico):
    
    # Sentencia SQL para actualizar el historial médico en la base de datos
    sentenciaSQL = """UPDATE HistorialMedico
                    SET fecha = %s,
                        herencias = %s,
                        tratamiento = %s,
                        cantidadMedicamento = %s,
                        estado = %s,
                        comentario = %s,
                        idLugarMedico = %s,
                        idPaciente = %s,
                        idEnfermedad = %s,
                        idMedico = %s
                    WHERE idHistorial = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (fecha, herencias, tratamiento, cantidadMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico, idHistorial))

        # Confirmamos los cambios en la base de datos
        conn.commit()

        # Cerramos la conexión
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    
    finally:
        if conn is not None:
            conn.close()
            

def actualizarMedicina(cantidad,tratamiento, idLugarMedico):
    
    # Sentencia SQL para actualizar la cantidad de un suministro médico en el inventario
    sentenciaSQL = """UPDATE Inventario
                    SET cantidad = cantidad - %s
                    WHERE idSuministro = %s AND idLugarMedico = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (cantidad, tratamiento, idLugarMedico))

        # Confirmamos los cambios en la base de datos
        conn.commit()

        # Cerramos la conexión
        cur.close()
        return True

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return False
    
    finally:
        if conn is not None:
            conn.close()