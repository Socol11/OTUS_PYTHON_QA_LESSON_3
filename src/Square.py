from src.Rectangle import Rectangle
from src.Figure import Figure


class Square(Rectangle, Figure):    # Наследуем класс квадрата от класса прямоугольника, т.к. квадрат - частный случай пр-ка.
    """Square class returns square's name, perimeter and area"""
    def __init__(self, side):
        if side <= 0:
            raise ValueError("Can't create Square!!!")
        super().__init__(side, side)
        self.side = side
        self.name = f'Square {self.side}'


if __name__ == "__main__":
    s = Square(6)
    print(s.name)
    print(s.perimeter)
    print(s.area)
    print(s.get_perimeter())
    print(s.get_area())
