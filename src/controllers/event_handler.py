import pygame
from utils.exepcions import ExitGame

def handle_event(userSpeed):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise ExitGame
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()
            if event.key == pygame.K_UP:
                userSpeed += 1
            if event.key == pygame.K_DOWN and userSpeed > 0:
                userSpeed -= 1
    return userSpeed

def pause():
    print("Presiona Enter para continuar")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    print("Continuando...")
                    return
                if event.type == pygame.QUIT:
                    raise ExitGame