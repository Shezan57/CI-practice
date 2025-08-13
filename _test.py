import pytest

# squeare
def square(n):
    return n ** 2


# cube
def cube(n):
    return n ** 3

# fifth
def fifth_power(n):
    return n ** 5

# test square
def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(4) == 16

# test cube
def test_cube():
    assert cube(2) == 8
    assert cube(-3) == -27
    assert cube(0) == 0
    assert cube(4) == 64

# test fifth power
def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(-3) == -243
    assert fifth_power(0) == 0
    assert fifth_power(4) == 1024
    
# test for invalid inputs
def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")
        cube("string")
        fifth_power("string")