from src.Figure import Figure


class Rectangle(Figure):
    """Rectangle class returns rectangle's name, perimeter and area"""
    def __init__(self, side_a, side_b):
        super().__init__()
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Can't create Rectangle")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f'Rectangle {side_a} and {side_b}'
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()

    def get_area(self):
        """The function calculates the area of a rectangle"""
        return round(self.side_a * self.side_b, 2)

    def get_perimeter(self):
        """The fincion calculates the perimeter of a rectangle"""
        return 2 * (self.side_a + self.side_b)
