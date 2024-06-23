# main.py
import pygame
from configs.settings import SPEED
from controllers.event_handler import handle_event
from views.interface import Interface
from utils.exepcions import ExitGame

def main():
    interface = Interface()
    game_interface = interface.game_interface()
    userSpeed = 0
    
    try:
        while True:
            userSpeed = handle_event(userSpeed)
            game_interface.update_display(SPEED + userSpeed)
            game_interface.game.next_generation()
    except (KeyboardInterrupt, ExitGame):
        del interface
        print("Saliendo del juego...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
