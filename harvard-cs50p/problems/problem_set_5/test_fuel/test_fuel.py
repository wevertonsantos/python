#https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

from fuel import convert,gauge

def test_one_divided_four():
    assert convert('1/4') == 25

def test_one_divided_two():
    assert convert('1/2') == 50

def test_x_y_integer():
    assert convert('y/x') == ValueError

def test_x_y_float():
    assert convert('0.1/2') == ValueError

def test_x_greater_than_y():
    assert convert('100/2') == ValueError

def test_y_is_zero():
    assert convert('1/0') == ZeroDivisionError

def test_return_e():
    assert convert('0/1') == "E"

def test_return_f():
    assert convert('1/1') == "F"