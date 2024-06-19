
# Cosas qu voy aprendiendo de python

## Archivo __init__.py

El archivo \__init\__.py es un componente clave en la estructura de paquetes de Python.Su presencia en un directorio indica a Python que el directorio debe ser tratado como un paquete, lo cual permite importar módulos desde ese directorio.

### Funciones del __init__.py

#### Inicialización de Paquetes

El archivo \__init\__.py puede contener código de inicialización que se ejecuta cuando el paquete o subpaquete es importado. Permite configurar variables, importar submódulos, y realizar configuraciones necesarias para el paquete.

#### Definición de Paquetes

Su presencia convierte un directorio en un paquete Python, permitiendo que los módulos dentro de ese directorio sean importados usando la sintaxis de paquetes.

#### Control de Importaciones

Controla qué submódulos y subpaquetes están disponibles al importar el paquete. Esto se puede hacer definiendo la lista \__all\__ en el \__init\__.py. Facilita la reexportación de ciertos submódulos o variables a nivel del paquete.
