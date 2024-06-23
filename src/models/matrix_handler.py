import numpy as np
from configs.settings import MATRIX_ROWS, MATRIX_COLUMNS


class NewMatrix:
    def __init__(self):
        self.new_matrix = np.zeros((MATRIX_ROWS, MATRIX_COLUMNS))

    def __getitem__(self, indices):
        i, j = indices
        i = i % MATRIX_COLUMNS
        j = j % MATRIX_ROWS
        return self.new_matrix[i, j]

    def __setitem__(self, indices, value):
        i, j = indices
        i = i % MATRIX_COLUMNS
        j = j % MATRIX_ROWS
        self.new_matrix[i, j] = value

    def put_matrix(self, new_matrix):
        if new_matrix.shape != (MATRIX_ROWS, MATRIX_COLUMNS):
            raise ValueError(
                "La matriz proporcionada no tiene las dimensiones correctas")
        self.new_matrix = new_matrix

    def get_matrix(self):
        return self.new_matrix


class OldMatrix:
    def __init__(self, seed=None):
        self.seed = np.random.randint(1, 1000) if seed is None else seed
        self.old_matrix = None
        self.initialize()

    def initialize(self):
        np.random.seed(self.seed)
        self.old_matrix = np.random.randint(0, 2, size=(MATRIX_ROWS, MATRIX_COLUMNS))

    def __getitem__(self, indices):
        i, j = indices
        i = i % MATRIX_COLUMNS
        j = j % MATRIX_ROWS
        return self.old_matrix[i, j]

    def __setitem__(self, indices, value):
        raise ValueError('No se puede modificar old_matrix!')

    def put_matrix(self, old_matrix):
        if old_matrix.shape != (MATRIX_ROWS, MATRIX_COLUMNS):
            raise ValueError(
                "La matriz proporcionada no tiene las dimensiones correctas")
        self.old_matrix = old_matrix

    def get_matrix(self):
        return self.old_matrix

    def neighborhood(self, i, j):
        '''
        Devuelve el vecindario de la celda (i, j) con sus respectivos valores.
        Los vecinos son las 8 celdas adyacentes modulando las coordenadas.
        '''
        rows, cols = self.old_matrix.shape
        neighbors_rows = (np.arange(i-1, i+2) % rows)[:, None]
        neighbors_cols = np.arange(j-1, j+2) % cols
        neighborhood = self.old_matrix[neighbors_rows, neighbors_cols]
        return neighborhood
