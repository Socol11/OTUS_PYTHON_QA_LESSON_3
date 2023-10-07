from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20),
                          (1.5, 10, 15, 23),
                          (0.01, 0.99, 0.01, 2),
                          (1000, 1000, 1000000, 4000)],
                         ids=["Create Rectangle with integer sides",
                              "Create Rectangle with one fractional side",
                              "Create Rectangle with two small fractional sides",
                              "Create Rectangle with two large sides"]
                         )
def test_rectangle(side_a, side_b, area, perimeter):
    """
    The function checks the area and the perimeter of rectangle for different side length
    Функция проверяет площадь и периметр прямоугольника для разных значений сторон
    :param side_a:
    :param side_b:
    :param area:
    :param perimeter:
    :return:
    """
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "other_figure", "summ"),
                         [(10, 20, Circle(5), 278.54),
                          (1.01, 2.99, Square(5), 28.02),
                          (1, 100, Triangle(5, 5, 5), 110.83),
                          (0.09, 0.01, Rectangle(5, 15), 75)],
                         ids=["Rectangle area + Circle area",
                              "Rectangle area + Square area",
                              "Rectangle area + Triangle area",
                              "Rectangle area + other Rectangle area"]
                         )
def test_rectangle_add_area(side_a, side_b, other_figure, summ):
    """
    The function checks the summ of areas of two figures
    :param side_a:
    :param side_b:
    :param other_figure:
    :param summ:
    :return:
    """
    r = Rectangle(side_a, side_b)
    assert r.add_area(other_figure) == summ
