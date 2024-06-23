import pygame
from configs.settings import SCREEN_X, SCREEN_Y, LIFE, DEATH, SEED, MATRIX_X, MATRIX_Y
from models.game_of_life import GameOfLife
class GameInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption('Juego de la Vida')
        self.clock = pygame.time.Clock()
        self.game = GameOfLife(SEED)
        self.cell_size = SCREEN_X // MATRIX_X
        
    def put_board(self):
        for row in range(MATRIX_Y):
            for col in range(MATRIX_X):
                old_value, new_value = self.game.put_cell(col, row)
                if old_value != new_value:
                    if new_value == 1:
                        color = LIFE
                    else:
                        color = DEATH
                    pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def update_display(self, speed):
        self.put_board()
        pygame.display.flip() # Actualizar la pantalla
        self.clock.tick(speed) # Controlar la velocidad de actualización