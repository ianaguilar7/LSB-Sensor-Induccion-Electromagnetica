from datetime import date

class Medicion():

    def __init__(self, nombre: str, voltaje_usado: float, voltaje_medio: float, 
                 amplitud: float, frecuencia: float, muestras_segundo: int):
        self.__nombre_metal: str = nombre.strip().lower() # Se transforma a minúsuclas
        self.__voltaje_usado: float = voltaje_usado
        self.__voltaje_medio: float = voltaje_medio
        self.__amplitud: float = amplitud
        self.__frecuencia: float = frecuencia
        self.__muestras_segundo: int = muestras_segundo
        self.__fecha: date = date.today()

    # Convierte el contenido de la clase en un str. Sirve para debuggear.
    def __str__(self):
        return (f"Metal: {self._nombre_metal}, Voltaje: {self._voltaje_usado} V, "
                f"Amplitud: {self._amplitud} V, Frecuencia: {self._frecuencia} Hz, "
                f"Muestras/s: {self._muestras_segundo}")

    @property
    def nombre_metal(self):
        return self.__nombre_metal
    
    @property
    def voltaje_usado(self):
        return self.__voltaje_usado
    
    @property
    def voltaje_medio(self):
        return self.__voltaje_medio

    @property
    def amplitud(self):
        return self.__amplitud

    @property
    def frecuencia(self):
        return self.__frecuencia

    @property
    def muestras_segundo(self):
        return self.__muestras_segundo
    
    @property
    def fecha(self):
        return self.__fecha