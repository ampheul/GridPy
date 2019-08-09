#!/usr/bin/python3

from PIL import Image, ImageDraw, ImageFont
from typing import Iterable, Tuple, Callable, List
import math
import typing_extensions
import Grid

def matrix_graphic(
    im : Image,
    n: int, 
    coordinate : Callable[[int], Tuple[int,int]],
    size : int,
    colors : List[Tuple[int,int,int]] = [(255,0,0),(0,255,0)] ) -> None:
    '''
    matrix_graphic
    ==============

    draw a matrix graphic using user input coordinates and colors.

    Parameters
    ----------
    n : int
        the number of rows and column of the square
    
    coordinate: Callable[int, Tuple[int,int]]
        Get the matrix coordinate of the current flat index.
        You could for example
    
    size : int = 512
        the length and width of the image. defaults to 512.
    
    colors : List[Tuple[int,int,int]]
        The colors which the squares will be colored with. 
        Colors occur as a gradient in the order they are given.
    
    Returns
    -------
    None
        generates a file with filename name + '.png' in the current directory.
    '''
    draw = ImageDraw.Draw(im)

    def color(gradient : float) -> Tuple[int,int,int]:
        
        i = math.floor( (len(colors) - 1) * gradient )
        t = ( len(colors) - 1 ) * gradient - i
        
        combine_colors = lambda c1, c2 : tuple( 
            int( (1-t)*a + t*b ) for a,b in zip(c1, c2) )

        return combine_colors(*colors[i:i+2])

    for i in range(n*n):
        
        y, x = coordinate(i)
        square = size/n
        draw.rectangle( 
            (x*square, y*square, (x+1)*square, (y+1)*square), 
            fill = color( i / (n*n) ) 
        )

        fnt = ImageFont.truetype("NotoMono-Regular", int(square*0.6))
        def center_text(x, y, text):
            width, height = fnt.getsize(text)
            return (x - width/2, y - height/2)
        
        draw.text( 
            center_text( (x+0.5)*square, (y+0.5)*square, str(i)), 
            str(i), font=fnt, fill=(0,0,0))
    
    # make the lines
    for i in range(n):

        draw.line( (0,i*square, size, i*square), fill=(0,0,0))
        draw.line( (i*square, 0, i*square, size), fill=(0,0,0))

    draw.line( (0, size-1, size-1, size-1), fill=(0,0,0))
    draw.line( (size-1, 0, size-1, size-1), fill=(0,0,0))

    

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:

        print("Must call make_graphics with arguments:")
        print("\n\tmake_graphics n size")
        print("\n\tn : int")
        print("\t\tthe number of rows and columns")
        print("\n\tsize : int")
        print("\t\tthe width and height of the output.")
        
        sys.exit()

    n = int(sys.argv[1])
    size = int(sys.argv[2])
    diagonal = lambda i : Grid.diagonal_to_matrix2d(n, *Grid.flat_to_diagonal(n, i))
    matrix2d = lambda i : Grid.flat_to_matrix2d(n, i)

    im1 = Image.new('RGB', (size, size), (0,0,0))
    im2 = Image.new('RGB', (size, size), (0,0,0))
    
    colors = [(255,0,0), (0,255,255)]

    matrix_graphic(im1, n, matrix2d, size, colors)
    matrix_graphic(im2, n, diagonal, size, colors)

    im1.save( 'matrix.png', 'PNG' )
    im2.save( 'diagonal.png', 'PNG' )
