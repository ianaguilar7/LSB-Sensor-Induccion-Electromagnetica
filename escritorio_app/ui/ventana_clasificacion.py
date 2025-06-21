from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QHBoxLayout,
    QSizePolicy, QHeaderView, QTableWidgetItem, QPushButton
)
from common.dao.medicion_dao import ClasificacionDAO
from PyQt6.QtCore import QSize

class VentanaClasificacion(QWidget):
    def __init__(self):
        super().__init__()

        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels([
            "ID", "Metal", "Voltaje Medio", "Amplitud", "Frecuencia"
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

    def cargar_pagina(self):
                    
        offset = self.__PAG_ACTUAL * self.__MAX_PAGINAS
        clasificaciones = ClasificacionDAO.obtener(self.__MAX_PAGINAS, offset)

        self.tabla.setRowCount(len(clasificaciones))

        for fila, clasificacion in enumerate(clasificaciones):
            self.tabla.setItem(fila, 0, QTableWidgetItem(str(clasificacion.id_metal)))
            self.tabla.setItem(fila, 1, QTableWidgetItem(str(clasificacion.metal)))
            self.tabla.setItem(fila, 2, QTableWidgetItem(str(clasificacion.voltaje_medio)))
            self.tabla.setItem(fila, 3, QTableWidgetItem(str(clasificacion.amplitud)))
            self.tabla.setItem(fila, 4, QTableWidgetItem(str(clasificacion.frecuencia)))

        self.boton_anterior.setEnabled(self.__PAG_ACTUAL > 0)
        self.boton_siguiente.setEnabled(len(clasificaciones) == self.__MAX_PAGINAS)
    
    def siguiente(self):
        self.__PAG_ACTUAL += 1
        self.cargar_pagina()

    def anterior(self):
        if self.__PAG_ACTUAL > 0:
            self.__PAG_ACTUAL -= 1
            self.cargar_pagina()
    