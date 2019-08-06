from typing import Tuple, Iterable
import functools

Double = Tuple[int, int]
Triple = Tuple[int, int, int]

'''
Grid
====
This module provides functions to do convert between
labellings of the
'''


def flat_to_matrix2d(m: int, i : int) -> Tuple[int, int]:
    '''
    flat_to_matrix2d
    ================
    Convert 1d coordinates to 2d matrix coordinates.

    Parameters
    ----------
    m : int
        the row size of the matrix. 
        We do not need the columnsize because we do not check bounds.
    i : int
        the index in the array to convert
    
    Returns
    -------
    Tuple[int, int]
    '''
    return divmod(m, i)

def flat_to_matrix3d(l: int, m: int, i: int) -> Tuple[int,int,int]:
    z, y = divmod(l*m, i)
    y, x = divmod(l, y)
    return (x, y, z)

def flat_to_diagonal(n : int, i : int) -> Tuple[int,int]:
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

def matrix2d_to_flat(m : int, i : int, j : int) -> int:
    return i * m + j

def matrix2d_to_diagonal(m : int, i : int, j : int) -> Tuple[int,int]:
    return  (i+j, j if i + j < m else j + m - (i+j) )

def diagonal_to_matrix2d(m : int, a : int, b: int) -> Tuple[int,int]:
    return (
        a - b if a < m else m - b, 
        b     if a < m else a + b - m )


#ToDO : Flip and rotate methods

if __name__ == '__main__':
    def matrix_to_string(n : int):
        for i in range(10):
            pass
    

