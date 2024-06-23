import pygame
from configs.settings import SCREEN_X, SCREEN_Y, LIFE, DEATH, SEED, MATRIX_X, MATRIX_Y
from models.game_of_life import GameOfLife
import time

global counter
counter = 0

global sumatoria 
sumatoria = 0
class GameInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption('Juego de la Vida')
        self.clock = pygame.time.Clock()
        self.game = GameOfLife(SEED)
        self.cell_size = SCREEN_X // MATRIX_X
        
    def put_board(self):
        start = time.time()
        for row in range(MATRIX_Y):
            for col in range(MATRIX_X):
                old_value, new_value = self.game.put_cell(row, col)
                if old_value != new_value:
                    if new_value == 1:
                        color = LIFE
                    else:
                        color = DEATH
                    pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
        end = time.time()
        global sumatoria
        sumatoria += (end - start) / (MATRIX_X * MATRIX_Y)
        global counter
        counter += 1

    def update_display(self, speed):
        self.put_board()
        pygame.display.flip() # Actualizar la pantalla
        self.clock.tick(speed) # Controlar la velocidad de actualización

    def __del__(self):
        pygame.quit()
        if counter > 0:
            print(f"Tiempo promedio de ejecución: {sumatoria / counter}")