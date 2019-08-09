from PIL import Image, ImageDraw, ImageFont
from functools import partial
import sys
import os
from typing import Iterable, Tuple
import typing_extensions
import Grid

def make_graphic(n: int, it : Iterable[Tuple[int,int]], name : str) -> None:
    
    size = 512

    im = Image.new('RGB', (size, size), (0,255,255))
    draw = ImageDraw.Draw(im)

    squareSize = size / n

    def color(i : int):
        colors = [
            (0,255,255),
            (0,255, 0),
            (255, 255, 0),
            (255, 0, 0),
            (255, 0, 255),
            (0,0, 255)
        ]
        j = int( (len(colors)-1)* i / (n*n) )
        t = (len(colors) -1)* i / (n*n) - j
        j = int(j)
        return tuple( int( (1-t)*a + t*b ) for a,b in zip(colors[j], colors[j+1]) )


    i = 0
    for y, x in it:
        draw.rectangle( 
            (x*squareSize,y*squareSize, (x+1)*squareSize, (y+1)*squareSize), 
            fill = color(i) )
        fnt = ImageFont.truetype("FreeMono.ttf", int(squareSize*0.75))

        draw.text((x*squareSize,y*squareSize), str(i), font=fnt, fill=(0,0,0))
        i += 1
    
    # make the lines
    for i in range(n):
        draw.line( (0,i*squareSize, size, i*squareSize), fill=(0,0,0))
        draw.line( (i*squareSize, 0, i*squareSize, size), fill=(0,0,0))
    draw.line( (0, size-1, size-1, size-1), fill=(0,0,0))
    draw.line( (size-1, 0, size-1, size-1), fill=(0,0,0))

        
    im.save( name + '.png', 'PNG' )

if __name__ == '__main__':
    n = 8
    diagonal = lambda i : Grid.diagonal_to_matrix2d(n, *Grid.flat_to_diagonal(n, i))
    diagonal_map = list(map(diagonal, range(n*n)))
    matrix2d = lambda i : Grid.flat_to_matrix2d(n, i)
    matrix2d_map = list(map(matrix2d, range(n*n)))
    make_graphic(n, matrix2d_map, 'matrix' )
    make_graphic(n, diagonal_map, 'diagonal')
