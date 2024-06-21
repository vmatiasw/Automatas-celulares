import numpy as np
from configs.settings import MATRIX_X, MATRIX_Y

class GameOfLife:
    def __init__(self):
        self.generation_number = 0
        self.even_gen_matrix = np.zeros((MATRIX_Y, MATRIX_X))
        self.odd_gen_matrix = np.zeros((MATRIX_Y, MATRIX_X))
        self.matrix_x = MATRIX_X
        self.matrix_y = MATRIX_Y
        self.initialize_matrices()

    def initialize_matrices(self):
        for row in range(self.matrix_y):
            for col in range(self.matrix_x):
                self.even_gen_matrix[row][col] = np.random.randint(0, 2)
                self.odd_gen_matrix[row][col] = 0

    def live_neighbors(self, matrix, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if matrix[(y + i) % self.matrix_y][(x + j) % self.matrix_x] == 1:
                    count += 1
        return count

    def put_cell(self, x, y):
        if (self.generation_number % 2) == 1:
            old_matrix = self.even_gen_matrix
            new_matrix = self.odd_gen_matrix
        else:
            old_matrix = self.odd_gen_matrix
            new_matrix = self.even_gen_matrix
        neighbours = self.live_neighbors(old_matrix, x, y)
        cell_is_alive = old_matrix[y][x] == 1
        if cell_is_alive:
            if neighbours < 2 or neighbours > 3:
                new_matrix[y][x] = 0
            else:
                new_matrix[y][x] = 1
        else:
            if neighbours == 3:
                new_matrix[y][x] = 1
            else:
                new_matrix[y][x] = 0
        return new_matrix[y][x]

    def next_generation(self):
        self.generation_number += 1
