
class Clasificacion():

    def __init__(self, nombre: str, voltaje_medio: float, amplitud: float, 
                 frecuencia: float):
        self.__nombre = nombre
        self.__voltaje_medio = voltaje_medio
        self.__amplitud = amplitud
        self.__frecuencia = frecuencia
    
    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def voltaje_medio(self):
        return self.__voltaje_medio
    
    @property
    def amplitud(self):
        return self.__amplitud
    
    @property
    def frecuencia(self):
        return self.__frecuencia
    
    