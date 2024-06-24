
# Cosas qu voy aprendiendo de python

## Trabajo con matrices en NumPy

### Slicing en NumPy

En Python estándar, puedes realizar slicing en listas y otros tipos de secuencias, pero no en matrices multidimensionales como en NumPy.
El slicing en NumPy se refiere a la técnica de seleccionar una parte o subconjunto de una matriz mediante especificación de rangos de índices. Esto te permite acceder a porciones específicas de los datos de una matriz sin necesidad de copiar los datos, lo cual es eficiente en términos de memoria y rendimiento.

### Broadcasting en NumPy

El broadcasting en NumPy es una poderosa capacidad que permite a las matrices con diferentes formas interactuar de manera natural y eficiente sin la necesidad de hacer copias explícitas de los datos. Esto hace que las operaciones entre matrices de diferentes tamaños sean posibles y convenientes.

#### Reglas de broadcasting

NumPy sigue un conjunto de reglas para determinar si las dos matrices pueden ser "broadcasteadas" entre sí:

- Regla 1: Si las matrices no tienen el mismo número de dimensiones, NumPy agrega dimensiones adicionales a la izquierda de la forma más pequeña hasta que ambas matrices tengan la misma cantidad de dimensiones.

- Regla 2: Luego, NumPy compara el tamaño de cada dimensión a lo largo de cada eje. Se consideran compatibles si son iguales o si una de ellas es igual a 1. Si ninguna de las dimensiones es igual a 1 en ambos arreglos, NumPy genera un error.

- Regla 3: Después de aplicar las Reglas 1 y 2, NumPy amplía cada dimensión con un tamaño igual al máximo de las longitudes en esa dimensión de los dos arreglos. En otras palabras, NumPy replica los elementos a lo largo de las dimensiones que necesitan ser ampliadas.

#### Ejemplo

[:, None] es una forma de agregar una dimensión adicional a un array en NumPy, convirtiéndolo en una columna. Esto se llama a menudo broadcasting en NumPy y permite que los arrays tengan formas compatibles para operaciones.

## Sobrecarga de operadores

En Python, puedes redefinir el comportamiento de ciertos operadores y funciones especiales mediante métodos especiales (también llamados métodos mágicos o dunder methods, porque comienzan y terminan con dobles guiones bajos __). Estos métodos permiten a los objetos de una clase personalizada comportarse de manera similar a los tipos de datos integrados de Python.

### Métodos especiales relevantes

- \_\_getitem\_\_(self, key):
Se usa para definir el comportamiento al acceder a un elemento de la colección usando la sintaxis de corchetes [].
Permite que los objetos de la clase personalizada se comporten como listas, diccionarios u otras colecciones.

- \_\_setitem\_\_(self, key, value):
Se usa para definir el comportamiento al asignar un valor a un elemento de la colección usando la sintaxis de corchetes [].
Permite la modificación de elementos de la colección.

- \_\_repr\_\_(self):
Define cómo se representa un objeto de la clase cuando se usa la función repr(), o cuando el objeto se imprime en la consola.
Debe devolver una cadena que idealmente podría ser usada para recrear el objeto.

- \_\_next\_\_(): ...

## Archivo \_\_init\_\_.py

El archivo \_\_init\_\_.py es un componente clave en la estructura de paquetes de Python.Su presencia en un directorio indica a Python que el directorio debe ser tratado como un paquete, lo cual permite importar módulos desde ese directorio.

### Funciones del __init__.py

#### Inicialización de Paquetes

El archivo \_\_init\_\_.py puede contener código de inicialización que se ejecuta cuando el paquete o subpaquete es importado. Permite configurar variables, importar submódulos, y realizar configuraciones necesarias para el paquete.

#### Definición de Paquetes

Su presencia convierte un directorio en un paquete Python, permitiendo que los módulos dentro de ese directorio sean importados usando la sintaxis de paquetes.

#### Control de Importaciones

Controla qué submódulos y subpaquetes están disponibles al importar el paquete. Esto se puede hacer definiendo la lista \_\_all\_\_ en el \_\_init\_\_.py. Facilita la reexportación de ciertos submódulos o variables a nivel del paquete.
