from typing import Tuple, Iterable
from math import sqrt, floor
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
        The row size of the matrix. 
        We do not need the columnsize because we do not check bounds.
    i : int
        the index in the array to convert
    
    Returns
    -------
    Tuple[int, int]
    '''
    return divmod(i, m)

def flat_to_matrix3d(l: int, m: int, i: int) -> Tuple[int,int,int]:
    z, y = divmod(i, l*m)
    y, x = divmod(i, l)
    return (x, y, z)

def flat_to_diagonal(n : int, i : int) -> Tuple[int,int]:
    '''
    flat_to_diagonal
    ================
    Sequences the squares in diagonal coordinates on a square matrix. 
    
    Parameters
    ----------
    n : int
        The row and column size.
        Diagonal coordinates are only defined for square matrices.
    i : int
        the index in the flat array

    Returns
    -------
    Double
    '''
    a_series = lambda x, y : (x + y) * (x - y + 1) // 2
    if i < n*(n+1)//2:
        # messy equation derived mathematically
        return floor( sqrt( 2*i + 0.25 ) - 0.5 )
    else:
        # messier equation derived mathematically
        return floor( n + 0.5 -sqrt( 2 * ( n * n - i) + 0.25 ) )


def matrix2d_to_flat(m : int, i : int, j : int) -> int:
    '''
    matrix2d_to_flat
    ================
    Convert matrix2d coordinates into 1d flat coordinates.

    Parameters
    ----------
    m : int
        the row size of the matrix
    i : int
        row index
    j : int
        column index
    
    Returns
    -------
    int
        the flat coordinate
    '''
    return i * m + j

def matrix2d_to_diagonal(n : int, i : int, j : int) -> Tuple[int, int]:
    '''
    matrix2d_to_diagonal
    ====================
    Convert matrix coordinates to diagonal coordinates.

    Parameters
    ----------
    n : int
        The row and column size for a square matrix.
        Diagonal coordinates are only defined for square matrices.
    i : int
        the row index.
    j : int
        the column index.

    Returns
    -------
    Tuple[int, int]
        The resultant diagonal coordinate.
    '''
    return  (
        i+j,
        j if i + j < n else n - i )

def diagonal_to_matrix2d(n : int, a : int, b: int) -> Tuple[int, int]:
    '''
    diagonal_to_matrix2d
    ====================
    Convert diagonal coordinate to the corresponding
    position in matrix coordinates.

    Parameters
    ----------
    n : int
        The row and column size for a square matrix.
        Diagonal coordinates are only defined for square matrices.
    a : int
        The index of the diagonal.
    b : int
        The index on the diagonal a.

    Returns
    -------
    Tuple[int, int]
        The resulting matrix coordinate.
    '''
    return (
        a - b if a < n else n - b, 
        b     if a < n else a + b - n )


#ToDO : Flip rotate and transpose. 

if __name__ == '__main__':

    def matrix_to_string(n : int):

        for i in range(10):
            
            pass
    

