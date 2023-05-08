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
            
def insertarHistorial(fecha, herencias, tratamiento, cantidaMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico):
    
    # Sentencia SQL para insertar el historial médico en la base de datos
    sentenciaSQL = """INSERT INTO HistorialMedico (fecha, herencias, tratamiento, cantidaMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (fecha, herencias, tratamiento, cantidaMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico))

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
            
def actualizarHistorial(idHistorial, fecha, herencias, tratamiento, cantidaMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico):
    
    # Sentencia SQL para actualizar el historial médico en la base de datos
    sentenciaSQL = """UPDATE HistorialMedico
                    SET fecha = %s,
                        herencias = %s,
                        tratamiento = %s,
                        cantidaMedicamento = %s,
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
        cur.execute(sentenciaSQL, (fecha, herencias, tratamiento, cantidaMedicamento, estado, comentario, idLugarMedico, idPaciente, idEnfermedad, idMedico, idHistorial))

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

def consultaMedico(idMedico):
    
    # Sentencia SQL para consultar la información del medico en la base de datos
    sentenciaSQL = """SELECT * FROM Medico
                    WHERE idMedico = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando el valor del parámetro como parámetro
        cur.execute(sentenciaSQL, (idMedico,))

        # Obtenemos la información del medico
        medico = cur.fetchone()

        # Cerramos la conexión
        cur.close()

        # Devolvemos la información del medico como una lista
        return list(medico)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
    
    finally:
        if conn is not None:
            conn.close()

def actualizarMedico(idMedico, nombre, direccion, telefono, especialidad, idLugarMedico):
    # Sentencia SQL para actualizar el médico en la base de datos
    sentenciaSQL = """UPDATE Medico
                    SET nombre = %s,
                        direccion = %s,
                        telefono = %s,
                        idEspecialidad = %s,
                        idLugarMedico = %s
                    WHERE idMedico = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (nombre, direccion, telefono, especialidad, idLugarMedico, idMedico))

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

def consultaBodeguero(idBodeguero):
    
    # Sentencia SQL para obtener la información del bodeguero por su idBodeguero
    sentenciaSQL = """SELECT idBodeguero, nombre, idUsuario, idLugarMedico
                    FROM Bodeguero
                    WHERE idBodeguero = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando el valor del parámetro como parámetro
        cur.execute(sentenciaSQL, (idBodeguero,))

        # Obtenemos el resultado de la consulta
        resultado = cur.fetchone()

        # Cerramos la conexión
        cur.close()

        # Retornamos el resultado
        return resultado

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
    
    finally:
        if conn is not None:
            conn.close()

def actualizarBodeguero(idBodeguero, nombre, idLugarMedico):
    
    # Sentencia SQL para actualizar el bodeguero en la base de datos
    sentenciaSQL = """UPDATE Bodeguero
                    SET nombre = %s,
                        idLugarMedico = %s
                    WHERE idBodeguero = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (nombre, idLugarMedico, idBodeguero))

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
            
def consultaHospital(idLugarMedico):
    
    # Sentencia SQL para seleccionar el hospital por su ID de lugar médico
    sentenciaSQL = """SELECT *
                    FROM lugarMedico
                    WHERE idLugarMedico = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando el valor del parámetro como parámetro
        cur.execute(sentenciaSQL, (idLugarMedico,))
        
        # Obtenemos el resultado
        hospital = cur.fetchone()

        # Cerramos la conexión
        cur.close()

        return hospital

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None
    
    finally:
        if conn is not None:
            conn.close()
            
def ingresarHospital(nombre, localizacion):
    # Sentencia SQL para insertar un hospital en la base de datos
    sentenciaSQL = """INSERT INTO LugarMedico (nombre, localizacion)
                    VALUES (%s, %s)
                    RETURNING idLugarMedico"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (nombre, localizacion))

        # Obtenemos el idLugarMedico generado por la base de datos
        idLugarMedico = cur.fetchone()[0]

        # Confirmamos los cambios en la base de datos
        conn.commit()

        # Cerramos la conexión
        cur.close()

        # Devolvemos el idLugarMedico generado por la base de datos
        return idLugarMedico

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

    finally:
        if conn is not None:
            conn.close()
            
def actualizarHospital(idLugarMedico, nombre, localizacion):
    
    # Sentencia SQL para actualizar el hospital en la base de datos
    sentenciaSQL = """UPDATE LugarMedico
                    SET nombre = %s,
                        localizacion = %s
                    WHERE idLugarMedico = %s"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL, pasando los valores de los parámetros como parámetros
        cur.execute(sentenciaSQL, (nombre, localizacion, idLugarMedico))

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
            
def consultaEnfermedadesMasFrecuentesMuerte():
    # Sentencia SQL para consultar las enfermedades más frecuentes que causan la muerte
    sentenciaSQL = """SELECT Enfermedad.nombre, COUNT(*) as cantidad
                        FROM HistorialMedico
                        INNER JOIN Enfermedad ON HistorialMedico.idEnfermedad = Enfermedad.idEnfermedad
                        WHERE HistorialMedico.estado = 'muerto'
                        GROUP BY Enfermedad.nombre
                        ORDER BY cantidad DESC
                        LIMIT 10;"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL)

        # Obtenemos los resultados y los guardamos en una lista de diccionarios
        resultados = []
        for fila in cur.fetchall():
            resultados.append({'enfermedad': fila[0], 'cantidad': fila[1]})

        # Cerramos la conexión y retornamos los resultados
        cur.close()
        return resultados

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return []

    finally:
        if conn is not None:
            conn.close()
            
def consultarPacientesPorMedico():
    sentenciaSQL = """
        SELECT m.nombre AS Medico, COUNT(*) AS NumeroPacientesAtendidos
        FROM Medico m
        JOIN HistorialMedico hm ON m.idMedico = hm.idMedico
        GROUP BY m.idMedico
        ORDER BY NumeroPacientesAtendidos DESC
        LIMIT 10;
    """
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL)

        # Recuperamos los resultados de la consulta
        resultados = cur.fetchall()

        # Cerramos la conexión
        cur.close()

        return resultados

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return None

    finally:
        if conn is not None:
            conn.close()
            
def consultaTopPacientes():
    # Sentencia SQL para la consulta
    sentenciaSQL = """SELECT p.idPaciente, p.nombre, p.direccion, p.telefono, p.masaCorporal, p.altura, 
                        COUNT(*) AS NumeroAsistencias
                    FROM Paciente p
                    JOIN HistorialMedico hm ON p.idPaciente = hm.idPaciente
                    GROUP BY p.idPaciente
                    ORDER BY NumeroAsistencias DESC
                    LIMIT 5"""

    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Ejecutamos la sentencia SQL
        cur.execute(sentenciaSQL)

        # Obtenemos los resultados
        resultados = cur.fetchall()

        # Cerramos la conexión
        cur.close()

        # Devolvemos los resultados
        return resultados

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    finally:
        if conn is not None:
            conn.close()
            
def consultaInventarioBajo():
    """Realiza una consulta a la base de datos para encontrar los suministros en inventario que tienen una cantidad menor o igual al stock mínimo especificado"""
    # Definir la sentencia SQL
    sentenciaSQL = """SELECT LugarMedico.nombre AS "Unidad de Salud", Suministro.nombre AS "Suministro", Inventario.cantidad AS "Cantidad", Inventario.expiracion AS "Fecha de Expiración"
                    FROM LugarMedico
                    INNER JOIN Inventario ON LugarMedico.idLugarMedico = Inventario.idLugarMedico
                    INNER JOIN Suministro ON Inventario.idSuministro = Suministro.idSuministro
                    WHERE Inventario.cantidad <= 15"""

    # Establecer la conexión a la base de datos
    conn = None
    try:
        # Obtener los parámetros de configuración
        params = config()
        # Conectar a la base de datos
        conn = psycopg2.connect(**params)
        # Crear un cursor para ejecutar las consultas
        cur = conn.cursor()
        # Ejecutar la consulta SQL, pasando el parámetro de stock mínimo como argumento
        cur.execute(sentenciaSQL)
        # Recuperar los resultados
        resultados = cur.fetchall()
        # Cerrar el cursor y confirmar los cambios
        cur.close()
        conn.commit()
        # Devolver los resultados
        return resultados
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # Cerrar la conexión
            conn.close()
def consultaPacientesAtendidos():
    """Realiza una consulta a la base de datos para encontrar las unidades de salud con mayor cantidad de pacientes atendidos"""
    # Definir la sentencia SQL
    sentenciaSQL = """SELECT LugarMedico.nombre, COUNT(DISTINCT HistorialMedico.idPaciente) AS total_pacientes_atendidos
                    FROM LugarMedico
                    JOIN HistorialMedico ON LugarMedico.idLugarMedico = HistorialMedico.idLugarMedico
                    GROUP BY LugarMedico.nombre
                    ORDER BY total_pacientes_atendidos DESC
                    LIMIT 3"""

    # Establecer la conexión a la base de datos
    conn = None
    try:
        # Obtener los parámetros de configuración
        params = config()
        # Conectar a la base de datos
        conn = psycopg2.connect(**params)
        # Crear un cursor para ejecutar las consultas
        cur = conn.cursor()
        # Ejecutar la consulta SQL, pasando el parámetro de cantidad de unidades de salud como argumento
        cur.execute(sentenciaSQL)
        # Recuperar los resultados
        resultados = cur.fetchall()
        # Cerrar el cursor y confirmar los cambios
        cur.close()
        conn.commit()
        # Devolver los resultados
        return resultados
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            # Cerrar la conexión
            conn.close()