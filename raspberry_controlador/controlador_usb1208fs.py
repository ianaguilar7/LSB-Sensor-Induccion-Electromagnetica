import time
import numpy as np
from typing import Final
from modelos.medicion import Medicion
from dao.medicion_dao import MedicionDAO
from uldaq import (get_daq_device_inventory, InterfaceType, DaqDevice, AiInputMode, 
                   ScanOption, ScanStatus)

# Se establece una constante global.
# Define la entrada analógica del USB-1208FS.
CHANNEL: Final = 0

def controlador_usb():

    nombre = input("Ingrese el nombre del metal: ").strip()
    try:
        # Se detectan dispositivos USB-DAQ
        devices = get_daq_device_inventory(InterfaceType.USB)
        if not devices:
            print("No se encontró ningún dispositivo USB-DAQ.")
            return
        
        # Se crea una instancia de DaqDevice con el primer dispositivo que encontro.
        daq_device = DaqDevice(devices[0])

        # Abre la conexión con el dispositivo DAQ para poder leer los datos.
        daq_device.connect()
        
        # Se obtiene el modulo de entrada analógica del dispositivo. 
        ai = daq_device.get_ai()
        
        # Cada canal mide voltaje entre su pin y el pin GND.
        # Modo DIFFERENTIAL, el canal mide la diferencia entre dos pines.
        input_mode = AiInputMode.SINGLE_ENDED
        
        # Obtener rango válido para el canal
        ranges = ai.get_ranges(CHANNEL)
        input_range = ranges[0]  # Elegir primer rango válido, ej: +/-10V
        
        # Configurar tasa de muestreo y cantidad de muestras
        rate = 1000  # muestras por segundo
        count = 1000  # total muestras por adquisición
        
        # Buffer para almacenar las muestras
        # count: Cantidad de muestras que se quieren adquirir.
        # dtype=np.float64: Asegura que los valores sean números de punto flotante de 
        # 64 bits.
        data = np.zeros(count, dtype=np.float64)
        
        # Iniciar escaneo analógico
        # ScanOption.DEFAULT: Opción de escaneo(por defecto = modo bloqueado, sin 
        # trigger).
        ai.scan_start(CHANNEL, input_range, count, rate, ScanOption.DEFAULT)
        
        # Leer datos
        status = ScanStatus.RUNNING
        while status == ScanStatus.RUNNING:
            data_read, status = ai.scan_read(data, count, 10.0)  # Timeout 10s
        
        # Detener escaneo
        ai.scan_stop()
        
        # Procesar datos
        voltaje_medio = np.mean(data)
        amplitud = np.max(data) - np.min(data)
        
        # Estimar frecuencia (simplemente con FFT)
        freqs = np.fft.fftfreq(len(data), 1/rate)
        fft_values = np.abs(np.fft.fft(data))
        
        # Solo tomamos frecuencias positivas
        pos_mask = freqs > 0
        freqs = freqs[pos_mask]
        fft_values = fft_values[pos_mask]
        
        # Frecuencia con mayor magnitud
        frecuencia_principal = freqs[np.argmax(fft_values)]
        
        print(f"Voltaje medio: {voltaje_medio:.3f} V")
        print(f"Amplitud: {amplitud:.3f} V")
        print(f"Frecuencia principal: {frecuencia_principal:.1f} Hz")
        print(f"Muestras por segundo: {rate}")
        
        daq_device.disconnect()

        # Se crea un objeto Medición.
        medicion = Medicion(nombre, 9,voltaje_medio, amplitud, frecuencia_principal, 
                            rate)
        print(medicion.__str__)

        # Se almacena el objeto Medición en la tabla correspondiente.
        MedicionDAO.insertar(medicion)

    except Exception as e:
        print(f"Error: {e}")