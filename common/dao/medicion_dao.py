import sqlite3
from common.modelos.medicion import Medicion
from common.bd.creacion_bd import RUTA_BASE_DATOS

class MedicionDAO():
    
    def __init__(self):
        pass

    @staticmethod
    def insertar(medicion: Medicion):
        
        insertar_medicion = """
        INSERT INTO Medicion (nombre_metal, voltaje_utilizado, voltaje_medio, 
        amplitud, frecuencia, muestras_segundo, fecha)
        VALUES(?, ?, ?, ?, ?, ?, ?)
        """
      
        valores = [medicion.nombre_metal, medicion.voltaje_usado, 
                   medicion.voltaje_medio, medicion.amplitud, medicion.frecuencia, 
                   medicion.muestras_segundo, medicion.fecha]

        try:
            with sqlite3.connect(RUTA_BASE_DATOS) as base_datos:
                cursor = base_datos.cursor()
                cursor.execute(insertar_medicion, valores)
                base_datos.commit()
        except sqlite3.Error:
            raise # Se re-lanza el error para manejarlo fuera de la función.

    @staticmethod
    def actualizar(medicion: Medicion):
        pass

    @staticmethod
    def obtener(limite : int, offset : int) -> list[Medicion]:
        
        leer_medicion = """
        SELECT * FROM Medicion
        ORDER BY ID_Medicion LIMIT ? OFFSET ?;
        """

        try:
            with sqlite3.connect(RUTA_BASE_DATOS) as base_datos:
                cursor = base_datos.cursor()
                cursor.execute(leer_medicion, (limite, offset))
                filas = cursor.fetchall()

                mediciones = [
                    Medicion(id, metal, voltaje_utilizado, voltaje_medio, amplitud, 
                             frecuencia, muestras_segundo, fecha) 
                             for (id, metal, voltaje_utilizado, voltaje_medio, 
                                  amplitud, frecuencia, muestras_segundo, fecha) 
                                  in filas
                ]

        except sqlite3.Error:
            raise 

        return mediciones