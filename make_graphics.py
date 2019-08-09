from PIL import Image, ImageDraw, ImageFont
from typing import Iterable, Tuple, Callable
import typing_extensions
import Grid

def matrix_graphic(
    im : Image
    n: int, 
    coordinate : Callable[int, Tuple[int,int]],
    name : str,
    size : int = 512,
    colors : List[Tuple[int,int,int]] = [(255,0,0),(0,255,0)]) -> None:
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
    
    name : str
        the name for the resulting file. .png extension added automatically
    
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

    squareSize = size / n

    def color(colors : Tuple[int,int,int], gradient : float):
        
        if len(colors) <= 1:
            return (0,0,0)

        i = math.ceil( (len(colors) - 2) * gradient - 1 )
        t = ( len(colors) - 1 ) * gradient - i
        
        c1, c2 = colors[i:i+2]

        return ( int( (1-t)*a + t*b ) for a,b in zip(c1, c2) )


    for i in range(n*n):
        
        y, x = coordinate(i)

        draw.rectangle( 
            (x*size/n, y*size/n, (x+1)*size/n, (y+1)*size/n), 
            fill = color( i / (n*n) )
        fnt = ImageFont.truetype("FreeMonoBold.ttf", int(squareSize*0.75))

        draw.text((x*squareSize,y*squareSize), str(i), font=fnt, fill=(0,0,0))
    
    # make the lines
    for i in range(n):

        draw.line( (0,i*squareSize, size, i*squareSize), fill=(0,0,0))
        draw.line( (i*squareSize, 0, i*squareSize, size), fill=(0,0,0))

    draw.line( (0, size-1, size-1, size-1), fill=(0,0,0))
    draw.line( (size-1, 0, size-1, size-1), fill=(0,0,0))

    

if __name__ == '__main__':
    import sys

    n = int(sys.argv[1])

    diagonal = lambda i : Grid.diagonal_to_matrix2d(n, *Grid.flat_to_diagonal(n, i))
    matrix2d = lambda i : Grid.flat_to_matrix2d(n, i)

    im1 = Image.new('RGB', (size, size), (0,0,0))
    im2 = Image.new('RGB', (size, size), (0,0,0))
    
    matrix_graphic(im, n, matrix2d, 'matrix' )
    matrix_graphic(im2, n, diagonal)

    im1.save( 'matrix.png', 'PNG' )
    im2.save( 'diagonal.png', 'PNG' )
