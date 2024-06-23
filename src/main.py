# main.py
import pygame
from configs.settings import SPEED
from controllers.event_handler import handle_event
from views.interface import GameInterface
from utils.exepcions import ExitGame

def main():
    game_interface = GameInterface()
    userSpeed = 0
    
    try:
        while True:
            userSpeed = handle_event(userSpeed)
            game_interface.game.next_generation()
            game_interface.update_display(SPEED + userSpeed)
    except (KeyboardInterrupt, ExitGame):
        print("Saliendo del juego...")
        del game_interface
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
