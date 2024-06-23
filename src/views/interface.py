import pygame
from configs.settings import SCREEN_X, SCREEN_Y
from views.game import GameInterface
from views.menu import MenuInterface

class Interface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
        pygame.display.set_caption('Juego de la Vida')
        self.handler = None
    
    def game_interface(self):
        del self.handler
        self.handler = GameInterface(self.screen)
        return self.handler

    def menu_interface(self):
        del self.handler
        self.handler = MenuInterface(self.screen)
        return self.handler
    
    def __del__(self):
        del self.handler
        pygame.quit()