# Definición de excepciones personalizadas
class ExitGame(Exception):
    """Indica que el usuario mando para salir del juego"""
    def __init__(self, mensaje=''):
        self.mensaje = mensaje
        super().__init__(self.mensaje)