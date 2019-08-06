from typing import Tuple, Iterable
import functools

Double = Tuple[int, int]
Triple = Tuple[int, int, int]

def flat_to_matrix2d(m: int, i : int) -> Double:
    return divmod(m, i)

def flat_to_matrix3d(l: int, m: int, i: int) -> Triple:
    z, y = divmod(l*m, i)
    y, x = divmod(l, y)
    return (x, y, z)

def matrix2d_to_flat(m : int, i : int, j : int) -> int:
    return i * m + j

def matrix2d_to_diagonal(m : int, i : int, j : int) -> Double:
    return  (i+j, j if i + j < m else j + m - (i+j) )

def diagonal_to_matrix2d(m : int, a : int, b: int) -> Double:
    return (
        a - b if a < m else m - b, 
        b     if a < m else a + b - m )

def flat_to_diagonal(n : int, i : int) -> Double:
    '''
    flat_to_diagonal
    ================
    Sequences the squares in diagonal coordinates on a square matrix. 
    
    Parameters
    ----------
    n : int
        the size of the square matrix
    i : int
        the index in the flat array

    Returns
    -------
    Double
    '''
    return matrix2d_to_diagonal(n, i // n, i % n)

flip_matrix2d_horizontal()

if __name__ == '__main__':
    def matrix_to_string(n : int):
        for i in 
    

