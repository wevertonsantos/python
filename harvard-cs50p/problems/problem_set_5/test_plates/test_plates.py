#https://cs50.harvard.edu/python/2022/psets/5/test_plates/

from plates import is_valid

def test_first_number():
    assert is_valid("0SS555") == False

def test_start_two_letters():
    assert is_valid("C5") == False

def test_contain_maximum_six_characters():
    assert is_valid("AAA2222") == False

def test_numbers_not_in_middle():
    assert is_valid("BSD22A") == False

def test_periods():
    assert is_valid("ACA:23") == False

def test_space():
    assert is_valid("CSS 5A") == False

def test_first_punctuation():
    assert is_valid("CSS.5A") == False

def test_second_punctuation():
    assert is_valid("CSS!5A") == False

def test_third_punctuation():
    assert is_valid("CSS,5A") == False