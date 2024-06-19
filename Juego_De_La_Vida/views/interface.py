import pygame
from configs.settings import SCREEN_X, SCREEN_Y, LIFE, DEATH
from models.game_of_life import GameOfLife

class GameInterface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption('Juego de la Vida')
        self.clock = pygame.time.Clock()
        self.game = GameOfLife()
        self.lifeColor = LIFE
        self.deathColor = DEATH
        
    def put_board(self):
        for row in range(self.game.matrix_y):
            for col in range(self.game.matrix_x):
                if self.game.put_cell(row, col) == 1:
                    color = self.lifeColor
                else:
                    color = self.deathColor
                pygame.draw.rect(self.screen, color, (col * self.game.cell_size, row * self.game.cell_size, self.game.cell_size, self.game.cell_size))

    def update_display(self, speed):
        self.put_board()
        pygame.display.flip() # Actualizar la pantalla
        self.clock.tick(speed) # Controlar la velocidad de actualización