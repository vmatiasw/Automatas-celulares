import pygame
from utils.exepcions import ExitGame

class MenuController():

    def __init__(self,interface_object):
        self.interface_object = interface_object

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise ExitGame
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    self.start_game()
                elif event.key == pygame.K_2:
                    self.configure_game()
                elif event.key == pygame.K_3:
                    raise ExitGame

    def start_game(self):
        print("Iniciando juego...")
        self.interface_object.set_game_interface()


    def configure_game(self):
        print("Configurando juego...")
        self.interface_object.set_config_interface()