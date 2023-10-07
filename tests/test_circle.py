from src.Circle import Circle
from src.Rectangle import Rectangle
from src.Square import Square
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(4, 50.27, 25.13),
                          (1000, 3141592.65, 6283.19),
                          (1.5, 7.07, 9.42)],
                         ids=["Create Circle with small integer radius",
                              "Create Circle with large integer radius",
                              "Create Circle with fractional radius"]
                         )
def test_circle(radius, area, perimeter):
    """
    The function checks the area and the perimeter for different radius length
    :param radius:
    :param area:
    :param perimeter:
    :return:
    """
    c = Circle(radius)
    assert c.name == f"Circle R={radius}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter


@pytest.mark.parametrize(("radius", "other_figure", "summ"),
                         [(1, Circle(5), 81.68),
                          (5, Square(5), 103.54),
                          (10, Triangle(5, 5, 5), 324.99),
                          (2, Rectangle(5, 15), 87.57)],
                         ids=["Circle area + other Circle area",
                              "Circle area + Square area",
                              "Circle area + Triangle area",
                              "Circle area + Rectangle area"]
                         )
def test_circle_add_area(radius, other_figure, summ):
    """
    The function checks the summ of areas of two figures
    :param radius:
    :param other_figure:
    :param summ:
    :return:
    """
    c = Circle(radius)
    assert c.add_area(other_figure) == summ
