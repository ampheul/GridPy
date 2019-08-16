from typing import Tuple, Iterable
from math import sqrt, floor
import functools

Double = Tuple[int, int]
Triple = Tuple[int, int, int]

'''
Grid
====
:author: Thomas Vandeven

This module provides functions for conversion between
matrix2d, diagonal, and flat coordinates.
'''


def flat_to_matrix2d(n: int, i : int) -> Tuple[int, int]:
    """
    flat_to_matrix2d
    ================
    Convert 1d coordinates to 2d matrix coordinates.

    Parameters
    ----------
    n : int
        The number of columns in the matrix
        We do not need the number of rows because we do not check bounds.
    i : int
        the index in the array to convert
    
    Returns
    -------
    Tuple[int, int]
    """
    return divmod(i, n)


def flat_to_matrix3d(l: int, m: int, i: int) -> Tuple[int,int,int]:
    z, y = divmod(i, l*m)
    y, x = divmod(i, l)
    return (x, y, z)


def flat_to_diagonal(n : int, i : int) -> Tuple[int,int]:
    """
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
    """
    if i < n*(n+1)//2:
        # complex equation derived mathematically
        a = floor( sqrt( 2*i + 0.25 ) - 0.5 )
        b = i - (1+a)*a//2
        return a,b
    else:
        # more complex equation derived mathematically
        a = floor( n + 0.5 - sqrt( 2 * ( n * n - i) + 0.25 ) ) - 1
        b = i - n*(n+1)//2 - (2*n-1-a)*a//2 - 1
        return (n + a, b+1)


def matrix2d_to_flat(n : int, i : int, j : int) -> int:
    """
    matrix2d_to_flat
    ================
    Convert matrix2d coordinates into 1d flat coordinates.

    Parameters
    ----------
    n : int
        the number of columns in the matrix
    i : int
        row index
    j : int
        column index
    
    Returns
    -------
    int
        the flat coordinate
    """
    return i * n + j


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
        i + j,
        j if i + j < n else n - i -1 )


def diagonal_to_matrix2d(n : int, a : int, b: int) -> Tuple[int, int]:
    '''
    diagonal_to_matrix2d
    ====================
    Convert diagonal coordinate to the corresponding
    position in matrix coordinates.

    Parameters
    ----------
    n : int
        The number of rows and columns for a square matrix.
        Diagonal coordinates are only defined for square matrices.
    a : int
        The index *of* the diagonal.
    b : int
        The index *on* the diagonal.

    Returns
    -------
    Tuple[int, int]
        The resulting matrix coordinate.
    '''
    return (
        a - b if a < n else n - b - 1, 
        b     if a < n else a - n + 1 + b )


def diagonal_to_flat(n : int, a : int, b : int) -> int:
    '''
    diagonal_to_flat
    ================
    Convert diagonal coordinates to flat coordinates.

    Parameters
    ----------
    n : int
        The number of rows and columns for a square matrix.
        Diagonal coordinates are only defined for square matrices.
    a : int
        The index *of* the diagonal.
    b : int
        The index *on* the diagonal.
    
    Returns
    -------
    int
        The resulting flat coordinate.
    '''
    return (a+1)*a//2 + b if a < n else n*(n+1)//2 + (3*n-1-a)*(a-n)//2 + b

#ToDO : Flip rotate and transpose. 
