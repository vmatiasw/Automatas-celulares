"""
El "Juego de la Vida" es un autómata celular desarrollado por el matemático británico 
John Conway en 1970. Consiste en un modelo matemático que simula la evolución de 
poblaciones en un tablero bidimensional basado en reglas simples. 

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
"""

'''
TODO:
    - [] Como hacer para que el usuario cargue la configuración inicial?
'''

# Librerias
import pygame
import numpy as np

# Valiables globales modificables
SCREEN_X = 800
SCREEN_Y = 600
LIFE = (255, 255, 255)
DEATH = (0, 0, 0)
MATRIX_X = 8
MATRIX_Y = 8

# Valiables globales no modificables
GEN_NUMBER = 0
EVEN_GEN_MATRIX = np.zeros((MATRIX_Y, MATRIX_X))
ODD_GEN_MATRIX = np.zeros((MATRIX_Y, MATRIX_X))
CELL_SIZE = SCREEN_X // MATRIX_X

# Funciones
def draw_board():
    for row in range(MATRIX_Y):
        for col in range(MATRIX_X):
            if (row + col) % 2 == 0:
                color = LIFE
            else:
                color = DEATH
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))


# Inicalizamos pygame
pygame.init()

# Creamos la ventana
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption('Juego de la Vida')

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Dibujar el tablero
    screen.fill(LIFE)  # Llenar la pantalla de blanco
    draw_board()  # Dibujar el tablero
    
    # Actualizar la pantalla
    pygame.display.flip()
    
    # Controlar la velocidad de actualización
    clock.tick(60)  # 60 FPS
    
# Salida de Pygame
pygame.quit()
