import os.path
import sqlite3

NOMBRE_BASE_DATOS: str = "BaseDatosEscritorio"

RUTA_BASE_DATOS = os.path.join("escritorio_app", "bd", 
                               NOMBRE_BASE_DATOS + ".sqlite3")

def verificar_existencia():
    return os.path.exists(RUTA_BASE_DATOS)

def crear_base_datos():
    
    os.makedirs(os.path.dirname(RUTA_BASE_DATOS), exist_ok=True)

    base_datos = sqlite3.connect(RUTA_BASE_DATOS)

    tabla_medicion = """
    CREATE TABLE IF NOT EXISTS Medicion (
        ID_Medicion INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nombre_metal TEXT NOT NULL,
        voltaje_utilizado REAL NOT NULL,
        voltaje_medio REAL NOT NULL,
        amplitud REAL NOT NULL,
        frecuencia REAL NOT NULL,
        muestras_segundo INTEGER NOT NULL,
        fecha NUMERIC NOT NULL
    );
    """

    tabla_medicion_procesada = """
    CREATE TABLE IF NOT EXISTS MedicionProcesada(
        ID_Procesada INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nombre_metal TEXT NOT NULL UNIQUE,
        voltaje_medio REAL NOT NULL,
        frecuencia REAL NOT NULL,
        ubicacion_metal TEXT NOT NULL
    );
    """
    
    bd_cursor = base_datos.cursor()

    bd_cursor.execute(tabla_medicion)
    bd_cursor.execute(tabla_medicion_procesada)

    base_datos.commit()
    base_datos.close()