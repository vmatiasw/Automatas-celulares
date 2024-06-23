import numpy as np
from configs.settings import MATRIX_X, MATRIX_Y

'''
IDEA:
Separar la lógica de las matrices de la lógica del juego de la vida.
'''

class NewMatrix:
    def __init__(self, seed=None):
        self.seed = np.random.randint(1, 1000) if seed is None else seed
        self.new_matrix = None
        self.initialize()

    def __getitem__(self, indices):
        x, y = indices
        x = x % MATRIX_X
        y = y % MATRIX_Y
        return self.new_matrix[y, x]

    def __setitem__(self, indices, value):
        x, y = indices
        x = x % MATRIX_X
        y = y % MATRIX_Y
        self.new_matrix[y, x] = value
    
    def initialize(self):
        np.random.seed(self.seed)
        self.new_matrix = np.random.randint(0, 2, size=(MATRIX_Y, MATRIX_X))
    
    def put_matrix(self, new_matrix):
        self.new_matrix = new_matrix
    
    def get_matrix(self):
        return self.new_matrix

class OldMatrix:
    def __init__(self):
        self.old_matrix = np.zeros((MATRIX_Y, MATRIX_X))

    def __getitem__(self, indices):
        x, y = indices
        x = x % MATRIX_X
        y = y % MATRIX_Y
        return self.old_matrix[y, x]

    def __setitem__(self, indices, value):
        raise ValueError('No se puede modificar old_matrix!')

    def put_matrix(self, old_matrix):
        self.old_matrix = old_matrix
    
    def get_matrix(self):
        return self.old_matrix

    def neighborhood(self, x, y):
        '''
        Devuelve el vecindario de la celda (x, y) con sus respectivos valores.
        Los vecinos son las 8 celdas adyacentes modulando las coordenadas.
        '''
        rows, cols = self.old_matrix.shape
        neighbors_rows = (np.arange(y-1, y+2) % rows)[:, None]
        neighbors_cols = np.arange(x-1, x+2) % cols
        neighborhood = self.old_matrix[neighbors_rows, neighbors_cols]
        return neighborhood
