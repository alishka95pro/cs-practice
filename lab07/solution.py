
import numpy as np

def reshape_rows(values: list[float], width: int) -> list[list[float]]:
    if width <= 0 or len(values) % width != 0:
        return []
    array = np.asarray(values, dtype=float)
    matrix = array.reshape(-1, width)
    return matrix.tolist()
    
def block(matrix: list[list[float]], rows: list[int], columns: list[int]) -> list[list[float]]:
    if not matrix:
        return []
    array = np.asarray(matrix, dtype=float)
    result = array[np.ix_(rows, columns)]
    return result.tolist()


def column_means(matrix: list[list[float]]) -> list[float]:
    if not matrix:
        return []
    array = np.asarray(matrix, dtype=float)
    result = np.mean(array, axis=0)
    return np.round(result, 6).tolist()


def column_range(matrix: list[list[float]], column: int) -> float:
    if not matrix:
        return 0.0
    array = np.asarray(matrix, dtype=float)
    result = np.max(array[:, column]) - np.min(array[:, column])
    return round(float(result), 6)
