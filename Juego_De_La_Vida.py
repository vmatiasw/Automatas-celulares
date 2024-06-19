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
    - [] ividir en carpetas por ejemplo los controladores, las vistas y los modelos
    - [] Como hacer para que el usuario cargue la configuración inicial?

IDEAS: 
    - [] Crear clases para los objetos del juego
    - [] Input de usuario para configurar el juego
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
SPEED = 60 / 60 # Velocidad de actualización en FPS

# Valiables globales no modificables
GENERATION_NUMBER = 0
EVEN_GEN_MATRIX = np.zeros((MATRIX_Y, MATRIX_X))
ODD_GEN_MATRIX = np.zeros((MATRIX_Y, MATRIX_X))
CELL_SIZE = SCREEN_X // MATRIX_X

# Inicializamos la matriz con valores aleatorios
def initialize_matrices():
    global EVEN_GEN_MATRIX, ODD_GEN_MATRIX
    for row in range(MATRIX_Y):
        for col in range(MATRIX_X):
            EVEN_GEN_MATRIX[row][col] = np.random.randint(0, 2)
            ODD_GEN_MATRIX[row][col] = 0

initialize_matrices()

def live_neighbors(matrix,x, y):
    '''
    Función que calcula la cantidad de vecinos vivos de una celda
    '''
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if matrix[(y + i) % MATRIX_Y][(x + j) % MATRIX_X] == 1:
                count += 1
    return count

# Funciones
def put_cell(x, y):
    '''
    Sobrepoblación: Una célula viva muere si tiene más de tres vecinos vivos.
    Estabilidad: Una célula viva con dos o tres vecinos vivos permanece viva en 
    la siguiente generación.
    Reproducción: Una célula muerta con exactamente tres vecinos vivos se 
    convierte en una célula viva.
    '''
    if (GENERATION_NUMBER % 2) == 0:
        oldMatrix = EVEN_GEN_MATRIX
        newMatrix = ODD_GEN_MATRIX
    else:
        oldMatrix = ODD_GEN_MATRIX
        newMatrix = EVEN_GEN_MATRIX
    neighbours = live_neighbors(oldMatrix, x, y)
    cell_is_alive = oldMatrix[y][x] == 1
    if cell_is_alive:
        if neighbours < 2 or neighbours > 3:
            newMatrix[y][x] = 0
        else:
            newMatrix[y][x] = 1
    else:
        if neighbours == 3:
            newMatrix[y][x] = 1
        else:
            newMatrix[y][x] = 0
    return newMatrix[y][x]

    

    
def draw_board():
    for row in range(MATRIX_Y):
        for col in range(MATRIX_X):
            if put_cell(row,col) == 1:
                color = LIFE
            else:
                color = DEATH
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Control de simulación
global userSpeed, running
userSpeed = 0  # Inclemento en la velocidad de la simulación
running = True # Control de la simulación

def pause():
    global userSpeed, running
    print("Presiona Enter para continuar")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return
                if event.type == pygame.QUIT:
                    running = False
                    return

def handle_event(event):
    global userSpeed, running
    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            pause()
        if event.key == pygame.K_UP:
            userSpeed += 1
        if event.key == pygame.K_DOWN:
            if userSpeed > 0:
                userSpeed -= 1

# Inicalizamos pygame
pygame.init()

# Creamos la ventana
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption('Juego de la Vida')

# Reloj para controlar la velocidad de actualización
clock = pygame.time.Clock()

# Bucle principal del juego
while running:
    for event in pygame.event.get():
        handle_event(event)
    
    if running == True:
        # Dibujar el tablero
        screen.fill(LIFE)  # Llenar la pantalla de blanco
        draw_board()  # Dibujar el tablero

        # Actualizar el número de generación
        GENERATION_NUMBER += 1
        
        # Actualizar la pantalla
        pygame.display.flip()
        
        # Controlar la velocidad de actualización
        clock.tick(SPEED+userSpeed) 
    
# Salida de Pygame
pygame.quit()
