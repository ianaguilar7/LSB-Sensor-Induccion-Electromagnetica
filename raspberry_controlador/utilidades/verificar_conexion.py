import serial
import json
import time

# Ruta del puerto serial donde está conectado el escritorio (puede variar).
# En Raspberry Pi suele ser /dev/ttyUSB0 o /dev/ttyACM0
PUERTO_SERIAL: str = "/dev/ttyUSB0"
BAUDRATE: int = 9600

def verificar_conexion():
    while True:
        try:
            with serial.Serial(PUERTO_SERIAL, BAUDRATE, timeout=1) as ser:
                print("Conectado a la aplicación de escritorio.")
                return True
        except serial.SerialException:
            print("Esperando reconexión...")
            time.sleep(2)

def recibir_dato():
    if verificar_conexion():
        with serial.Serial(PUERTO_SERIAL, BAUDRATE, timeout=2) as ser:

            linea = ser.readline().decode("utf-8").strip()

            try:
                datos = json.loads(linea)

                #for clave, valor in datos.items():
            
            except json.JSONDecodeError:
                print("ERROR: No se pudo decodificar el JSON.")