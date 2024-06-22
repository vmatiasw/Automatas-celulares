import numpy as np
from configs.settings import MATRIX_X, MATRIX_Y


class GameOfLife:
    def __init__(self, seed=None):
        self.generation_number = 0
        self.even_gen_matrix = np.zeros((MATRIX_Y, MATRIX_X))
        self.odd_gen_matrix = np.zeros((MATRIX_Y, MATRIX_X))
        self.matrix_x = MATRIX_X
        self.matrix_y = MATRIX_Y
        self.seed = np.random.randint(1, 1000) if seed is None else seed
        print(f"Seed: {self.seed}")
        self.initialize_matrices(self.seed)

    def initialize_matrices(self, seed=None):
        '''
        Inicializa las matrices de la generación par e impar.
        La matriz de la generación par se inicializa con ceros.
        La matriz de la generación impar se inicializa con valores aleatorios segun la semilla del parametro o la predefinida.
        '''
        if seed is not None:
            seed = self.seed
        self.odd_gen_matrix = np.zeros(
            (self.matrix_y, self.matrix_x), dtype=int)
        np.random.seed(seed)
        self.even_gen_matrix = np.random.randint(
            0, 2, size=(self.matrix_y, self.matrix_x))

    def live_neighbors(self, matrix, x, y):
        '''
        Calcula el número de vecinos vivos de una celda.
        Los vecinos son las 8 celdas adyacentes modulando las coordenadas.
        '''
        rows, cols = matrix.shape
        neughbors_rows = (np.arange(y-1, y+2) % rows)[:, None]
        neughbors_cols = np.arange(x-1, x+2) % cols
        neighborhood = matrix[neughbors_rows, neughbors_cols]
        neighborhood[1, 1] = 0
        return np.sum(neighborhood)

    def put_cell(self, x, y):
        old_matrix, new_matrix = self.get_matrices()
        neighbours = self.live_neighbors(old_matrix, x, y)
        cell_is_alive = old_matrix[y][x] == 1
        new_matrix[y][x] = self.apply_rules(neighbours, cell_is_alive)
        return new_matrix[y][x]

    def get_matrices(self):
        '''
        Retorna (matriz anterior, matriz actual) segun la generación.
        '''
        if (self.generation_number % 2) == 1:
            return self.even_gen_matrix, self.odd_gen_matrix
        else:
            return self.odd_gen_matrix, self.even_gen_matrix

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

    def next_generation(self):
        self.generation_number += 1

    def get_seed(self):
        return self.seed

    def set_seed(self, seed):
        self.seed = seed

    def restart(self):
        self.initialize_matrices(self.seed)
        self.generation_number = 0
