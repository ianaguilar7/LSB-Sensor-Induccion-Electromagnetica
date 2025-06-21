from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QHBoxLayout,
    QSizePolicy, QHeaderView, QTableWidgetItem, QPushButton
)
from common.dao.medicion_dao import MedicionDAO
from PyQt6.QtCore import QSize

class VentanaPrincipal(QWidget):

    def __init__(self):
        super().__init__()

        self.__MAX_PAGINAS : int = 25
        self.__PAG_ACTUAL : int = 0

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(8)
        self.tabla.setHorizontalHeaderLabels([
            "ID", "Metal", "Voltaje Utilizado",
            "Voltaje Medio", "Amplitud",
            "Frecuencia", "Muestra/s", "Fecha"
        ])
        self.tabla.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)

        # Tamaño fijo personalizable
        ancho_deseado = 1000
        alto_deseado = 400
        self.tabla.setMinimumSize(QSize(ancho_deseado, alto_deseado))
        self.tabla.setMaximumSize(QSize(ancho_deseado, alto_deseado))
        self.tabla.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        # Se ajusta el tamaño de columnas proporcionalmente
        header = self.tabla.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # Se centrá la tabla horizontalmente
        contenedor_centrado = QHBoxLayout()
        contenedor_centrado.addStretch()
        contenedor_centrado.addWidget(self.tabla)
        contenedor_centrado.addStretch()

        # Botones de navegación
        self.boton_anterior = QPushButton("Anterior")
        self.boton_siguiente = QPushButton("Siguiente")

        self.boton_anterior.clicked.connect(self.anterior)
        self.boton_siguiente.clicked.connect(self.siguiente)

        contenedor_botones = QHBoxLayout()
        contenedor_botones.addStretch()
        contenedor_botones.addWidget(self.boton_anterior)
        contenedor_botones.addWidget(self.boton_siguiente)
        contenedor_botones.addStretch()

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(contenedor_centrado)
        layout_principal.addLayout(contenedor_botones)
        self.setLayout(layout_principal)

        # Se ajusta el tamaño de la ventana.
        self.setFixedSize(ancho_deseado + 100, alto_deseado + 100)

        self.cargar_pagina()

    def cargar_pagina(self):
                    
        offset = self.__PAG_ACTUAL * self.__MAX_PAGINAS
        mediciones = MedicionDAO.obtener(self.__MAX_PAGINAS, offset)

        self.tabla.setRowCount(len(mediciones))

        for fila, medicion in enumerate(mediciones):
            self.tabla.setItem(fila, 0, QTableWidgetItem(str(medicion.id_medicion)))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(medicion.metal)))
            self.tabla.setItem(fila, 2, QTableWidgetItem(str(medicion.voltaje_utilizado)))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(medicion.voltaje_medio)))
            self.tabla.setItem(fila, 4, QTableWidgetItem(str(medicion.amplitud)))
            self.tabla.setItem(fila, 5, QTableWidgetItem(str(medicion.frecuencia)))
            self.tabla.setItem(fila, 6, QTableWidgetItem(str(medicion.muestras_por_segundo)))
            self.tabla.setItem(fila, 7, QTableWidgetItem(str(medicion.fecha)))

        self.boton_anterior.setEnabled(self.__PAG_ACTUAL > 0)
        self.boton_siguiente.setEnabled(len(mediciones) == self.__MAX_PAGINAS)
    
    def siguiente(self):
        self.__PAG_ACTUAL += 1
        self.cargar_pagina()

    def anterior(self):
        if self.__PAG_ACTUAL > 0:
            self.__PAG_ACTUAL -= 1
            self.cargar_pagina()
    