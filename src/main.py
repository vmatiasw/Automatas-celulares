# main.py
import pygame
from views.interface import Interface
from utils.exepcions import ExitGame

def main():
    interface = Interface()
    try:
        while True:
            interface_handler = interface.get_handler()
            interface_handler.handle_events()
            interface_handler.update_display()
    except (KeyboardInterrupt, ExitGame):
        del interface
        print("Saliendo del juego...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
