from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(10, 20, 25, 94.99, 55),
                          (20.2, 100, 110, 917.16, 230.2),
                          (1000, 10000, 10900, 2274916.21, 21900)],
                         ids=["Create Triangle with small integer sides",
                              "Create Triangle with a fractional side",
                              "Create Triangle with large integer sides"])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    """
    The function checks the area and the perimeter of a triangle for different side length
    :param side_a:
    :param side_b:
    :param side_c:
    :param area:
    :param perimeter:
    :return:
    """
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle {side_a}, {side_b}, {side_c}"
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "other_figure", "summ"),
                         [(10, 20, 25, Circle(5), 173.53),
                          (1.01, 2.99, 3.49, Square(5.19), 28.34),
                          (20, 25, 30, Triangle(5, 5, 5), 258.87),
                          (0.09, 0.03, 0.07, Rectangle(5, 15), 75)],
                         ids=["Triangle area + Circle area",
                              "Triangle area + Square area",
                              "Triangle area + other Triangle area",
                              "Triangle area + Rectangle area"]
                         )
def test_triangle_add_area(side_a, side_b, side_c, other_figure, summ):
    """
    The function checks the summ of areas of two figures
    :param side_a:
    :param side_b:
    :param other_figure:
    :param summ:
    :return:
    """
    t = Triangle(side_a, side_b, side_c)
    assert t.add_area(other_figure) == summ
