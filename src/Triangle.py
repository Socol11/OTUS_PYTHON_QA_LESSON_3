from src.Figure import Figure


class Triangle(Figure):
    """Triangle class returns triangle's name, perimeter and area"""
    def __init__(self, a, b, c):
        super().__init__()
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Can't create Triangle!!!")
        if a >= b + c or b >= a + c or c >= a + b:
            raise ValueError("One side must be less the summ of the others' two!")
        self.a = a
        self.b = b
        self.c = c
        self.name = f'Triangle {self.a}, {self.b}, {self.c}'
        self.perimeter = self.get_perimeter()
        self.area = self.get_area()


    def get_area(self):
        """The function calculates the area of a triangle"""
        sp = self.get_perimeter() / 2
        area = (sp * (sp - self.a) * (sp - self.b) * (sp - self.c)) ** .5
        return round(area, 2)

    def get_perimeter(self):
        """The function calculates the perimeter of a triangle"""
        perimeter = self.a + self.b + self.c
        return perimeter
