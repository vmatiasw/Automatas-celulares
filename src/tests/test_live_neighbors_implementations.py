import unittest
import numpy as np
import itertools

class TestLiveNeighbors(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestLiveNeighbors, self).__init__(*args, **kwargs)
        self.MATRIX_COLUMNS = 3
        self.MATRIX_ROWS = 3

    def live_neighbors_1(self, matrix, x, y):
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if matrix[(y + i) % self.MATRIX_ROWS][(x + j) % self.MATRIX_COLUMNS] == 1:
                    count += 1
        return count

    def live_neighbors_2(self, matrix, x, y):
        '''
        Calcula el número de vecinos vivos de una celda.
        Los vecinos son las 8 celdas adyacentes modulando las coordenadas.
        '''
        rows, cols = matrix.shape
        neughbors_rows = (np.arange(y-1, y+2) % rows)[:, None]
        neughbors_cols = np.arange(x-1, x+2) % cols
        vecindario = matrix[neughbors_rows, neughbors_cols]
        vecindario[1, 1] = 0
        return np.sum(vecindario)

    def setUp(self):
        xy_size = 3
        self.matrices = []
        
        # Generar todas las combinaciones posibles de matrices binarias
        for combination in itertools.product([0, 1], repeat=xy_size**2):
            matrix = np.array(combination).reshape((xy_size, xy_size))
            self.matrices.append(matrix)

    def test_live_neighbors_implementations(self):
        for matrix in self.matrices:
            for x in range(matrix.shape[1]):
                for y in range(matrix.shape[0]):
                    result_1 = self.live_neighbors_1(matrix, x, y)
                    result_2 = self.live_neighbors_2(matrix, x, y)
                    # Aquí deberías ajustar el resultado esperado según tu implementación
                    self.assertEqual(result_1, result_2)

if __name__ == '__main__':
    unittest.main()
