import os.path
import sqlite3

NOMBRE_BASE_DATOS: str = "BaseDatosRaspberry"

RUTA_BASE_DATOS = os.path.join("raspberry_controlador", "bd", 
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

    tabla_perfil_configuracion = """
    CREATE TABLE IF NOT EXISTS PerfilConfiguracion (
        ID_Perfil INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        canal INTEGER NOT NULL,
        modo_entrada TEXT NOT NULL CHECK(modo_entrada IN ('SINGLE_ENDED', 
        'DIFFERENTIAL')),
        rango_entrada INTEGER NOT NULL,
        tasa INTEGER NOT NULL,
        conteo INTEGER NOT NULL
    );
    """

    tabla_alerta = """
    CREATE TABLE IF NOT EXISTS Alerta(
        ID_Alerta INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        tipo TEXT NOT NULL CHECK(tipo IN ('visual', 'sonora')),
        ubicacion TEXT NOT NULL
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
    bd_cursor.execute(tabla_perfil_configuracion)
    bd_cursor.execute(tabla_alerta)
    bd_cursor.execute(tabla_medicion_procesada)

    base_datos.commit()
    base_datos.close()