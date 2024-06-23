import pygame
from utils.exepcions import ExitGame

class GameController:
    def handle_events(self, userSpeed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise ExitGame
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pause()
                if event.key == pygame.K_UP:
                    userSpeed += 1
                if event.key == pygame.K_DOWN and userSpeed > 1:
                    userSpeed -= 1
        return userSpeed

    def pause(self):
        print("Presiona Enter para continuar")
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        print("Continuando...")
                        return
                    if event.type == pygame.QUIT:
                        raise ExitGame