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

def matrix2d_to_flat(n : int, i : int, j : int) -> int:
    return i * n + j 

def matrix2d_to_diagonal(m : int, i : int, j : int) -> Double:

    return (i*n)

def flat_to_diagonal(n : int, i : int) -> Double:
    '''
    flat_to_diagonal
    ================
    Sequences the squares on the grid using diagonal coordinates. 

    Returns
        Tuple[int,int]
    '''
    return matrix2d_to_diagonal()

flip_matrix2d_horizontal()

if __name__ == '__main__':
    def matrix_to_string(n : int):
        for i in 
    

