# cliente_raspberry.py
import socket
import json
import time

IP_PC = '192.168.1.100'  # Cambiá esto por la IP real de la PC
PUERTO = 5000

datos = {
    "metal": "cobre",
    "voltaje": 1.78,
    "frecuencia": 345.0
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
    cliente.connect((IP_PC, PUERTO))
    print("Conectado al servidor.")

    while True:
        mensaje = json.dumps(datos)
        cliente.sendall(mensaje.encode('utf-8'))
        print("Dato enviado.")
        time.sleep(2)
