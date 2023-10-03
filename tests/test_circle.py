from src.Circle import Circle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(4, 50.27, 25.13),
                          (1000, 3141592.65, 6283.19)])
def test_circle(radius, area, perimeter):
    c = Circle(radius)
    assert c.name == f"Circle R={radius}"
    assert c.get_area() == area
    assert c.get_perimeter() == perimeter

@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(-4, -50.27, -25.13),
                          (0, 0, 0)])
def test_square_negative(radius, area, perimeter):
    with pytest.raises(ValueError):    # Так мы ожидаем, что тест будет с ошибкой, поэтому тесты пройдут.
        c = Circle(radius)
        assert c.name == f"Circle R={radius}"
        assert c.get_area() == area
        assert c.get_perimeter() == perimeter

def test_add_area():
    c = Circle(5)
    s = Square(5)
    assert c.add_area(s) == 103.54
