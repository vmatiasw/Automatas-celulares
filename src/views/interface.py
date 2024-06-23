import pygame
from configs.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR
from views.game import GameInterface
from views.menu import MenuInterface

class Interface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Juego de la Vida')
        self.handler = MenuInterface(self)
    
    def set_game_interface(self):
        del self.handler
        self.screen.fill(BACKGROUND_COLOR)
        self.handler = GameInterface(self)
        return self.handler

    def set_menu_interface(self):
        del self.handler
        self.screen.fill(BACKGROUND_COLOR)
        self.handler = MenuInterface(self)
        return self.handler
    
    def set_config_interface(self):
        pass
        # del self.handler
        # self.screen.fill(BACKGROUND_COLOR)
        # self.handler = ConfigInterface(self.screen)
        # return self.handler
    
    def get_handler(self):
        return self.handler
    
    def __del__(self):
        del self.handler
        pygame.quit()