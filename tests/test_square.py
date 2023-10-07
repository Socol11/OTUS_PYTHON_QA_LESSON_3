from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(4, 16, 16),
                          (1.51, 2.28, 6.04),
                          (1000, 1000000, 4000)],
                         ids=["Create the Square with a small integer side",
                              "Create the Square with a small fractional side",
                              "Create the Square wit a large integer side"]
                         )
def test_square(side, area, perimeter):
    """
    The function checks the area and the perimeter of a square with different side length
    :param side:
    :param area:
    :param perimeter:
    :return:
    """
    r = Square(side)
    assert r.name == f"Square {side}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side", "other_figure", "summ"),
                         [(5, Square(10), 125),
                          (10, Rectangle(5, 10), 150),
                          (7, Triangle(5, 5, 5), 59.83),
                          (25, Circle(8), 826.06)],
                         ids=["Square area + other Square area",
                              "Square area + Rectangle area",
                              "Square area + Triangle area",
                              "Square area + Circle area"]
                         )
def test_square_add_area(side, other_figure, summ):
    """
    The function checks the summ of areas of two figures
    :param side:
    :param other_figure:
    :param summ:
    :return:
    """
    s = Square(side)
    assert s.add_area(other_figure) == summ
