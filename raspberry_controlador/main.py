from controlador_usb1208fs import controlador_usb
from bd.creacion_bd import (verificar_existencia, crear_base_datos)
from utilidades.verificar_conexion import verificar_conexion

def main():

    if not verificar_existencia():
        crear_base_datos()  

    print("\n[1] Realizar medición\n[2] Conectar al escritorio\n")
    decision = input("Seleccione la opción: ")

    if (decision == "1"):
        controlador_usb()
    elif (decision == "2"):
        verificar_conexion()        


if __name__ == "__main__":
    main()  