# LSB-Sensor-Induccion-Electromagnetica

----

### Funcionalidades

## Escritorio

- Visualizar mediciones realizadas(base de datos).
- Cargar datos medidos por los detectores.
- Cargar datos a los detectores.
- Crear perfiles de configuración para cada detector.
- Configurar alertas visuales o de sonido en el detector.

## Rasperry 

- Perfiles de configuración
- Lógica para la medición de los metales.
- Cargar datos de la base de datos (Procesados o sin procesar ?)
- Configurar alertas visuales o de sonido en el detector.

----

#### Construcción de la base de datos

- Voltaje predeterminado 9 volts.
- Voltaje medio (directamente con el ADC).
- Frecuencia (Podrá ser modificada desde la raspberry?).
- Amplitud.
- Forma de onda.
- Mediciones por segundo (Se penso realizar las mediciones en múltiples hilos).
- Fecha de medición.
- Nombre del metal medido.