import pygame
import time
from configs.settings import TXTNAME, SAVEINTXT, SCREEN_WIDTH, SCREEN_HEIGHT, LIFE, DEATH, SEED, MATRIX_COLUMNS, MATRIX_ROWS, SPEED
from models.game_of_life import GameOfLife
from controllers.game import GameController

global counter
counter = 0

global sumatoria 
sumatoria = 0
class GameInterface():
    def __init__(self, interface_object):
        self.screen = interface_object.screen
        self.speed = SPEED
        self.clock = pygame.time.Clock()
        self.game = GameOfLife(SEED, TXTNAME, SAVEINTXT)
        self.controller = GameController()
        self.cell_size = SCREEN_WIDTH // MATRIX_COLUMNS
        
    def put_board(self):
        start = time.time()
        for row in range(MATRIX_ROWS):
            for col in range(MATRIX_COLUMNS):
                old_value, new_value = self.game.put_cell(row, col)
                if old_value != new_value:
                    if new_value == 1:
                        color = LIFE
                    else:
                        color = DEATH
                    pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))
        end = time.time()
        global sumatoria
        sumatoria += (end - start) / (MATRIX_COLUMNS * MATRIX_ROWS)
        global counter
        counter += 1

    def update_display(self):
        self.put_board()
        pygame.display.flip() # Actualizar la pantalla
        self.clock.tick(self.speed) # Controlar la velocidad de actualización
        self.game.next_generation()
    
    def handle_events(self):
        self.speed = self.controller.handle_events(self.speed)

    def __del__(self):
        if counter > 0:
            print(f"Tiempo promedio de alctualizacion del board: {sumatoria / counter}")
