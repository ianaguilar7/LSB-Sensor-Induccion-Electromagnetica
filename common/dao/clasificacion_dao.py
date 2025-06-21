import sqlite3
from common.modelos.clasificacion import Clasificacion
from common.bd.creacion_bd import RUTA_BASE_DATOS

class ClasificacionDAO():

    def __init__(self):
        pass

    @staticmethod
    def insertar(clasificacion: Clasificacion):
        pass

    @staticmethod
    def obtener(limite: int, offset: int) -> list[Clasificacion]:
        
        leer_clasificacion = """
        SELECT * FORM Clasificacion
        ORDER BY ID_Clasificacion LIMIT ? OFFSET ?
        """

        try:
            with sqlite3.connect(RUTA_BASE_DATOS) as base_datos:
                cursor = base_datos.cursor()
                cursor.execute(leer_clasificacion, (limite, offset))
                filas = cursor.fetchall()

                clasificaciones = [
                    Clasificacion(id, metal, voltaje_medio, amplitud, frecuencia)
                    for (id, metal, voltaje_medio, amplitud, frecuencia) in filas
                ]

        except sqlite3.Error:
            raise

        return clasificaciones

