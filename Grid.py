from typing import Tuple, Iterable
import functools

Double = Tuple[int, int]
Triple = Tuple[int, int, int]

def flat_to_matrix2d(rowsize: int, i : int) -> Tuple[int, int]:
    return divmod(rowsize, i)

def matrix2d_to_flat(rowsize : int, i : int, j : int) -> int:
    return i*rowsize + j 

def flat_to_matrix3d(rowsize : int, columnsize: int, i: int) -> Tuple[int, int, int]:
    z, y = divmod(rowsize*columnsize, i)
    y, x = divmod(rowsize, y)
    return (x, y, z)

def flat_to_diagonal(squareSize : int, i : int) -> int:
    '''
    flat_to_diagonal
    ================
    Indexes the 
    Returns
        Tuple[int,int]
    '''

map( range(10*10), functools.partial(flat_to_matrix2d) )
