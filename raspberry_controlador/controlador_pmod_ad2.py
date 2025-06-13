import time
import numpy as np
from smbus2 import SMBus
from modelos.medicion import Medicion
from dao.medicion_dao import MedicionDAO

# Dirección I2C del AD7991
I2C_ADDR = 0x21
CONFIG_CH0 = 0b10010000  # Habilitar CH0, modo single-ended

# Parámetros de muestreo
rate = 1000     # muestras por segundo
count = 1000    # total de muestras a leer

def leer_adc(bus):
    # Configurar canal y hacer pequeña pausa
    bus.write_byte(I2C_ADDR, CONFIG_CH0)
    time.sleep(0.001)

    # Leer dos bytes desde el ADC
    data = bus.read_i2c_block_data(I2C_ADDR, 0x00, 2)
    raw_val = ((data[0] & 0x0F) << 8) | data[1]
    voltaje = (raw_val / 4095.0) * 3.3
    return voltaje

def controlador_pmod():
    nombre = input("Ingrese el nombre del metal: ").strip()

    try:
        with SMBus(1) as bus:
            data = []

            print("Leyendo datos del sensor...")
            for _ in range(count):
                voltaje = leer_adc(bus)
                data.append(voltaje)
                time.sleep(1.0 / rate)

            data = np.array(data)

            voltaje_medio = np.mean(data)
            amplitud = np.max(data) - np.min(data)

            # Análisis de frecuencia
            freqs = np.fft.fftfreq(len(data), 1 / rate)
            fft_vals = np.abs(np.fft.fft(data))

            # Tomamos solo frecuencias positivas
            pos_mask = freqs > 0
            freqs = freqs[pos_mask]
            fft_vals = fft_vals[pos_mask]

            frecuencia_principal = freqs[np.argmax(fft_vals)]

            # Mostrar resultados
            print(f"Voltaje medio: {voltaje_medio:.3f} V")
            print(f"Amplitud: {amplitud:.3f} V")
            print(f"Frecuencia principal: {frecuencia_principal:.1f} Hz")
            print(f"Muestras por segundo: {rate}")

            # Crear objeto Medicion
            medicion = Medicion(nombre, 9, voltaje_medio, amplitud, frecuencia_principal, rate)
            print(medicion.__str__)

            # Guardar en la base de datos
            MedicionDAO.insertar(medicion)

    except Exception as e:
        print(f"Error: {e}")
