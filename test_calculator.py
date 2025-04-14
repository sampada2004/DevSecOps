import pytest
from calculator import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert sub(5, 2) == 3
    assert sub(1, 5) == -4

def test_multiply():
    assert mul(2, 3) == 6
    assert mul(-1, 1) == -1

def test_divide():
    assert div(10, 2) == 5
    with pytest.raises(ValueError):
        div(10,0)