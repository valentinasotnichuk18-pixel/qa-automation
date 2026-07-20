import pytest
from calculator import add, subtract, multiply, divide

@pytest.mark.parametrize('a, b, expected', [
    (1, 2, 3),
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize('a, b, expected', [
    (5, 3, 2),
    (10, 4, 6),
    (0, 0, 0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
