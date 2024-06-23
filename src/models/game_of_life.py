import numpy as np
from models.matrix_handler import OldMatrix, NewMatrix

class GameOfLife:
    def __init__(self, seed=None):
        self.old_matrix = OldMatrix(seed)
        self.new_matrix = NewMatrix()

    def live_neighbors(self, x, y):
        '''
        Calcula el número de vecinos vivos de una celda.
        Los vecinos son las 8 celdas adyacentes modulando las coordenadas.
        '''
        neighborhood = self.old_matrix.neighborhood(x, y)
        neighborhood[1, 1] = 0  # Excluye la célula misma
        return np.sum(neighborhood)

    def put_cell(self, x, y):
        '''
        Retorna (valor anterior, valor actual).
        '''
        neighbours = self.live_neighbors(x, y)
        cell_is_alive = self.old_matrix[x, y] == 1
        new_value = self.apply_rules(neighbours, cell_is_alive)
        self.new_matrix[x, y] = new_value
        return self.old_matrix[x, y], self.new_matrix[x, y]

    def next_generation(self):
        '''
        Swapea las matrices de los objetos OldMatrix y NewMatrix.
        '''
        aux = self.old_matrix.get_matrix()
        self.old_matrix.put_matrix(self.new_matrix.get_matrix())
        self.new_matrix.put_matrix(aux)

    def apply_rules(self, neighbors, cell_is_alive):
        if cell_is_alive == 1:
            if neighbors < 2 or neighbors > 3:
                return 0
            else:
                return 1
        else:
            if neighbors == 3:
                return 1
            else:
                return 0

