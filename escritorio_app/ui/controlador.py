from PyQt6.QtWidgets import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QStackedWidget
from ui.ventana_principal import VentanaPrincipal
from ui.ventana_clasificacion import VentanaClasificacion

class Controlador(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema")
        self.setGeometry(100, 100, 1200, 800)

        # Crear pantallas
        self.ventana_principal = VentanaPrincipal()
        self.ventana_clasificacion = VentanaClasificacion()

        # Crear contenedor de vistas (pantallas)
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(self.ventana_principal)      # índice 0
        self.stacked_widget.addWidget(self.ventana_clasificacion)  # índice 1

        # Crear botones de navegación
        self.boton_panel = QPushButton("Panel")
        self.boton_clasificacion = QPushButton("Clasificación")
        self.boton_perfiles = QPushButton("Perfiles")
        self.boton_alertas = QPushButton("Alertas")

        self.boton_panel.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.boton_clasificacion.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.boton_perfiles.clicked.connect(lambda: print("Perfiles aún no implementado"))
        self.boton_alertas.clicked.connect(lambda: print("Alertas aún no implementado"))

        # Layout de los botones (izquierda)
        botones_layout = QVBoxLayout()
        botones_layout.setSpacing(40)          # Espacio entre botones
        botones_layout.setContentsMargins(10, 40, 10, 40)  # márgenes: izquierda, arriba, derecha, abajo

        botones_layout.addWidget(self.boton_panel)
        botones_layout.addWidget(self.boton_clasificacion)
        botones_layout.addWidget(self.boton_perfiles)
        botones_layout.addWidget(self.boton_alertas)
        botones_layout.addStretch()  # Empuja los botones hacia arriba si sobra espacio

        # Contenedor para los botones (opcional, para control extra de estilo o tamaño)
        contenedor_botones = QWidget()
        contenedor_botones.setLayout(botones_layout)

        # Layout principal (horizontal)
        layout_principal = QHBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.addWidget(contenedor_botones)
        layout_principal.addWidget(self.stacked_widget)

        self.setLayout(layout_principal)
