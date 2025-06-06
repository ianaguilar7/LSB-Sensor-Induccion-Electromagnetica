from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QHBoxLayout, QSizePolicy, QHeaderView
from PyQt6.QtCore import QSize

class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()

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

        layout_principal = QVBoxLayout()
        layout_principal.addLayout(contenedor_centrado)
        self.setLayout(layout_principal)

        # Se ajusta el tamaño de la ventana.
        self.setFixedSize(ancho_deseado + 100, alto_deseado + 100)