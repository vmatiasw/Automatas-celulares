import pygame
from configs.settings import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, TEXT_COLOR
from controllers.menu import MenuController
class MenuInterface:
    def __init__(self, interface_object):
        self.screen = interface_object.screen
        self.controller = MenuController(interface_object)
        self.draw_menu()
    
    def draw_menu(self):
        self.screen.fill(BACKGROUND_COLOR)
    
        # Dibujar opciones del menú
        fuente = pygame.font.Font(None, 36)
        
        texto_jugar = fuente.render('1. Iniciar', True, TEXT_COLOR)
        texto_configurar = fuente.render('2. Configurar', True, TEXT_COLOR)
        texto_salir = fuente.render('3. Salir', True, TEXT_COLOR)
        
        self.screen.blit(texto_jugar, (SCREEN_WIDTH // 2 - texto_jugar.get_width() // 2, 200))
        self.screen.blit(texto_configurar, (SCREEN_WIDTH // 2 - texto_configurar.get_width() // 2, 250))
        self.screen.blit(texto_salir, (SCREEN_WIDTH // 2 - texto_salir.get_width() // 2, 300))
        
        pygame.display.flip()
    
    def update_display(self, speed=None):
        pass

    def handle_events(self):
        self.controller.handle_events()