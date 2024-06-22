import numpy as np
from configs.settings import MATRIX_X, MATRIX_Y

class NewMatrix:
    def __init__(self, matrix_x, matrix_y, seed=None):
        self.seed = np.random.randint(1, 1000) if seed is None else seed
        self.new_matrix = None
        self.matrix_x = MATRIX_X
        self.matrix_y = MATRIX_Y
        self.initialize()

    def __getitem__(self, indices):
        x, y = indices
        # Envolver los índices
        x = x % self.matrix_x
        y = y % self.matrix_y
        return self.new_matrix[x, y]

    def __setitem__(self, indices, value):
        x, y = indices
        # Envolver los índices
        x = x % self.matrix_x
        y = y % self.matrix_y
        self.new_matrix[x, y] = value
    
    def initialize(self):
        np.random.seed(self.seed)
        self.new_matrix = np.random.randint(0, 2, size=(self.matrix_y, self.matrix_x))
    
    def put_matrix(self, new_matrix):
        self.new_matrix = new_matrix

class OldMatrix:
    def __init__(self, matrix_x, matrix_y):
        self.old_matrix = np.zeros((matrix_x, matrix_y))
        self.matrix_x = matrix_x
        self.matrix_y = matrix_y

    def __getitem__(self, indices):
        x, y = indices
        # Envolver los índices
        x = x % self.matrix_x
        y = y % self.matrix_y
        return self.old_matrix[x, y]

    def __setitem__(self, indices, value):
        raise ValueError('No se puede modificar old_matrix!')

    def sum_matrix(self):
        return np.sum(self.old_matrix)

    def put_matrix(self, old_matrix):
        self.old_matrix = old_matrix
    
    