import numpy as np
from configs.settings import MATRIX_ROWS, MATRIX_COLUMNS
import os

class WrapMatrix:
    def __init__(self):
        self.matrix = np.zeros((MATRIX_ROWS, MATRIX_COLUMNS))

    def __getitem__(self, indices):
        i, j = indices
        i = i % MATRIX_COLUMNS
        j = j % MATRIX_ROWS
        return self.matrix[i, j]

    def __setitem__(self, indices, value):
        i, j = indices
        i = i % MATRIX_COLUMNS
        j = j % MATRIX_ROWS
        self.matrix[i, j] = value

    def validate_matrix(self, matrix):
        if matrix.shape != (MATRIX_ROWS, MATRIX_COLUMNS):
            raise ValueError("La matriz proporcionada no tiene las dimensiones correctas")
        if not np.all(np.isin(matrix, [0, 1])):
            raise ValueError("La matriz proporcionada no tiene solo 0s y 1s")

    def put_matrix(self, matrix):
        self.validate_matrix(matrix)
        self.matrix = matrix

    def get_matrix(self):
        return self.matrix

class NewMatrix(WrapMatrix):
    def __init__(self):
        super().__init__()

class OldMatrix(WrapMatrix):
    def __init__(self, seed=None, txtname=False, saveInTxt=False):
        self.matrix = None
        self.seed = np.random.randint(1, 1000) if seed is None else seed
        
        if txtname:
            self.matrix = np.loadtxt('./data/' + txtname, dtype=int)
            self.validate_matrix(self.matrix)
        else:
            np.random.seed(self.seed)
            self.matrix = np.random.randint(0, 2, size=(MATRIX_ROWS, MATRIX_COLUMNS))
            if saveInTxt:
                self.save_matrix_to_file(self.matrix)

    def save_matrix_to_file(self, matrix):
        directory = './models/data/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        filename = os.path.join(directory, f"{self.seed}.txt")
        np.savetxt(filename, matrix, fmt='%d')
        print(f"Matriz guardada en {filename}")

    def __setitem__(self, indices, value):
        raise ValueError('No se puede modificar old_matrix!')

    def neighborhood(self, i, j):
        '''
        Devuelve el vecindario de la celda (i, j) con sus respectivos valores.
        Los vecinos son las 8 celdas adyacentes modulando las coordenadas.
        '''
        rows, cols = self.matrix.shape
        neighbors_rows = (np.arange(i-1, i+2) % rows)[:, None]
        neighbors_cols = np.arange(j-1, j+2) % cols
        neighborhood = self.matrix[neighbors_rows, neighbors_cols]
        return neighborhood
