import numpy as np


def calcReverse(matrix):
    """
    Возвращает обратную матрицу.
    """
    try:
        inverse_matrix = np.linalg.inv(np.array(matrix, dtype=np.int32))
        return inverse_matrix.tolist()
    except np.linalg.LinAlgError:
        return "Матрица вырожденная, обратной не существует."


def calcRank(matrix):
    """
    Возвращает ранг матрицы.
    """
    return [[np.linalg.matrix_rank(np.array(matrix))]]


def calcSquare(matrix):
    """
    Возвращает квадрат матрицы.
    """
    return np.dot(np.array(matrix), np.array(matrix)).tolist()
