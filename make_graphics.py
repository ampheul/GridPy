from PIL import Image, ImageDraw
from functools import partial
import sys
import os
import typing
import typing_extensions
import Grid

def make_graphic(n: int, it : typing.Iterable[int], name : str) -> None:
    
    size = 512

    im = Image.new('RGB', (size, size), (0,255,255))
    draw = ImageDraw.Draw(im)

    squareSize = size / n

    def color(i : int):
        colors = [
            (255, 0, 0), 
            #(255, 255, 0),
            #(0,255, 0),
            #(0, 255, 255),
            #(0, 0, 255),
            (0, 0, 255)
        ]
        j = int( (len(colors)-1)* i / (n*n) )
        t = (len(colors) -1)* i / (n*n) - j
        j = int(j)
        return tuple( int( (1-t)*a + t*b ) for a,b in zip(colors[j], colors[j+1]) )


    for i in it:
        x, y = Grid.flat_to_matrix2d(n, i)
        draw.rectangle( 
            (x*squareSize,y*squareSize, (x+1)*squareSize, (y+1)*squareSize), 
            fill = color(i) )
        
    im.save( name + '.png', 'PNG' )

if __name__ == '__main__':
    n = 8
    flat_to_flat_diagonal = lambda i : Grid.matrix2d_to_flat(n,
            *Grid.diagonal_to_matrix2d(n, 
                *Grid.flat_to_diagonal(n, i)))
    make_graphic(n, map(flat_to_flat_diagonal, range(n*n)), 'regular' )
