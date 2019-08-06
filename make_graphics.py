from PIL import Image, ImageDraw
import typing
import typing_extensions
import Grid

def make_graphic(n: int, it : typing.Iterable[int], name : str) -> None:
    
    size = 512
    im = Image.new('RGB', (size, size))
    squareSize = size / n
    colorFraction = 256 / (n*n)
    draw = ImageDraw.Draw(im)
    for i in it:
        x, y = Grid.flat_to_matrix2d(n, i)
        draw.rectangle( 
            (x*squareSize,y*squareSize, (x+1)*squareSize, (y+1)*squareSize), 
            fill= i*colorFraction )
        
    im.save(name, 'PNG')
    