import serial
import json
import time

puerto = "COM3"  # En Windows: algo como COM3. En Linux: /dev/ttyUSB0
baudrate = 9600

datos = {
    "nombre": "Hierro",
    "voltaje": 1.23,
    "amplitud": 0.45,
    "frecuencia": 60.0
}

with serial.Serial(puerto, baudrate, timeout=2) as ser:
    mensaje = json.dumps(datos)
    ser.write((mensaje + "\n").encode('utf-8'))
    print("Datos enviados.")
