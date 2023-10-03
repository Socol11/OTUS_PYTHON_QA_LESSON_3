import math
from src.Figure import Figure


class Circle(Figure):
    """Cyrcle class returns cyrcle's name, perimeter and area"""
    def __init__(self, radius):
        super().__init__()
        if radius <= 0:
            raise ValueError("Can't create Circle!")
        self.radius = radius
        self.name = f'Circle R={self.radius}'
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        area = math.pi * self.radius ** 2
        return round(area, 2)

    def get_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return round(perimeter, 2)


if __name__ == "__main__":
    c = Circle(1000)
    print(c.name)
    print(c.perimeter)
    print(c.area)
