from configparser import ConfigParser


import psycopg2

def config(filename='data.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Sección {0} no encontrada en el {1} fichero'.format(section, filename))

    return db


def connect():
    conn = None
    try:
        # Leemos los parámetros de conexión
        params = config()

        # Conectamos con el servidor PostgreSQL
        print('Conectando con PostgreSQL...')
        conn = psycopg2.connect(**params)

        # creamos un cursor
        cur = conn.cursor()

        # Ejecutamos una sentencia SQL
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # Mostramos la versión de PostgreSQL que hemos solicitado con la sentencia anterior
        db_version = cur.fetchone()
        print(db_version)

        # Cerramos la comunicación con PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')