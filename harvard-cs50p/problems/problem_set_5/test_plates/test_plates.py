#https://cs50.harvard.edu/python/2022/psets/5/test_plates/

from plates import is_valid

def test_start_two_letters():
    assert is_valid("C5") == False

def test_contain_maximum_six_characters():
    assert is_valid("AAA222") == True