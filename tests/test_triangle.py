from src.Triangle import Triangle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(10, 20, 25, 94.99, 55),
                          (20.2, 100, 110, 917.16, 230.2),
                          (1000, 10000, 10900, 2274916.21, 21900)])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    t = Triangle(side_a, side_b, side_c)
    assert t.name == f"Triangle {side_a}, {side_b}, {side_c}"
    assert t.get_area() == area
    assert t.get_perimeter() == perimeter

@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(-10, 20, 25, 94.99, 35.01),
                          (20, -100, 110, 915.19, 30),
                          (0, 0, 0, 0, 0),
                          (100100, 10000, 10900, 2274916.21, 21900)])
def test_triangle_negative(side_a, side_b, side_c, area, perimeter):
    with pytest.raises(ValueError):    # Так мы ожидаем, что тест будет с ошибкой, поэтому тесты пройдут.
        t = Triangle(side_a, side_b, side_c)
        assert t.name == f"Triangle {side_a}, {side_b}, {side_c}"
        assert t.get_area() == area
        assert t.get_perimeter() == perimeter


def test_add_area():
    t = Triangle(2, 5, 6)
    s = Square(5)
    assert t.add_area(s) == 29.68
