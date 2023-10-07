from src.Rectangle import Rectangle
from src.Figure import Figure


class Square(Rectangle, Figure):
    """Square class returns square's name, perimeter and area"""
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Can't create Square!!!")
        super().__init__(side, side)
        self.side = side
        self.name = f'Square {self.side}'
