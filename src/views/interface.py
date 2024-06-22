import pygame
from configs.settings import SCREEN_X, SCREEN_Y, LIFE, DEATH, SEED
from models.game_of_life import GameOfLife
class GameInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        self.screen_y = SCREEN_Y
        self.screen_x = SCREEN_X
        pygame.display.set_caption('Juego de la Vida')
        self.clock = pygame.time.Clock()
        self.game = GameOfLife(SEED)
        self.lifeColor = LIFE
        self.deathColor = DEATH
        self.cell_size = SCREEN_X // self.game.matrix_x
        
    def put_board(self):
        for row in range(self.game.matrix_y):
            for col in range(self.game.matrix_x):
                old_value, new_value = self.game.put_cell(col, row)
                if old_value != new_value:
                    if new_value == 1:
                        color = self.lifeColor
                    else:
                        color = self.deathColor
                    pygame.draw.rect(self.screen, color, (col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size))

    def update_display(self, speed):
        self.put_board()
        pygame.display.flip() # Actualizar la pantalla
        self.clock.tick(speed) # Controlar la velocidad de actualización