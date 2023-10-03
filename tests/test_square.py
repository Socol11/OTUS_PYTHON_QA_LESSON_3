from src.Rectangle import Rectangle
from src.Square import Square
import pytest


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(4, 16, 16),
                          (5, 25, 20),
                          (1000, 1000000, 4000)])
def test_square(side, area, perimeter):
    r = Square(side)
    assert r.name == f"Square {side}"
    assert r.get_area() == area
    assert r.get_perimeter() == perimeter

@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(-4, 16, -16),
                          (-5, 25, -20),
                          (0, 0, 0)])
def test_square_negative(side, area, perimeter):
    with pytest.raises(ValueError):    # Так мы ожидаем, что тест будет с ошибкой, поэтому тесты пройдут.
        r = Square(side)
        assert r.name == f"Square {side}"
        assert r.get_area() == area
        assert r.get_perimeter() == perimeter

def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 35
