# servidor_pc.py
import socket
import json

HOST = '0.0.0.0'  # Escucha en todas las interfaces de red
PUERTO = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
    servidor.bind((HOST, PUERTO))
    servidor.listen(1)
    print(f"Esperando conexión en el puerto {PUERTO}...")

    conn, addr = servidor.accept()
    with conn:
        print(f"Conectado con: {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                print("Cliente desconectado.")
                break
            try:
                mensaje = data.decode('utf-8')
                datos = json.loads(mensaje)
                print(f"JSON recibido: {datos}")
            except json.JSONDecodeError:
                print(f"Texto recibido: {data.decode('utf-8')}")
