from common.bd.creacion_bd import (verificar_existencia, crear_base_datos)
from PyQt6.QtWidgets import QApplication
from escritorio_app.ui.controlador import Controlador
import sys

def main():
    if not verificar_existencia():
        crear_base_datos()     

    app = QApplication(sys.argv)
    ventana = Controlador()
    ventana.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()  