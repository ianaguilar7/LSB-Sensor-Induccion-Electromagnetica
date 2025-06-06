import sqlite3
from modelos.medicion import Medicion
from bd.creacion_bd import RUTA_BASE_DATOS

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
    def obtener():
        pass