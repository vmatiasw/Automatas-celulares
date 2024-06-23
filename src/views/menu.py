import pygame

class MenuInterface:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
    
    def update_display(self, speed):
        self.clock.tick(speed)
        pygame.display.flip()