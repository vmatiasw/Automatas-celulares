# Sobre el juego de la vida

El "Juego de la Vida" es un autómata celular desarrollado por el matemático británico John Conway en 1970. Consiste en un modelo matemático que simula la evolución de  poblaciones en un tablero bidimensional basado en reglas simples.

Aquí están las reglas básicas del Juego de la Vida:

    Tablero: El Juego de la Vida se juega en un tablero bidimensional infinito 
        compuesto por celdas cuadradas.

    Estado inicial: Cada celda puede estar en uno de dos estados posibles: 
        viva (representada por un valor no nulo, a menudo 1) o muerta 
        (representada por un valor nulo, a menudo 0).

    Reglas de evolución:
        Sobrepoblación: Una célula viva muere si tiene más de tres vecinos vivos.
        Estabilidad: Una célula viva con dos o tres vecinos vivos permanece viva en 
        la siguiente generación.
        Reproducción: Una célula muerta con exactamente tres vecinos vivos se 
        convierte en una célula viva.

    Vecindad: Cada célula tiene hasta ocho células vecinas adyacentes, 
        que son las que comparten un lado o una esquina con la célula en cuestión.

    Iteración: El tablero evoluciona en pasos discretos de tiempo (generaciones). 
        En cada paso de tiempo, todas las células del tablero se actualizan 
        simultáneamente según las reglas anteriores. Esto significa que el estado de 
        todas las células en la generación siguiente se calcula en función del estado 
        actual de todas las células en la generación actual.
