# filename: test_math.py

def add(a, b):
    return a + b

def test_add_function():
    result = add(1, 2)
    # Simple, standard Python assert!
    assert result == 3

def test_add_failure():
    # If this fails, pytest will clearly show the values of result and 5
    result = add(2, 3)
    assert result == 5