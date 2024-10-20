#https://cs50.harvard.edu/python/2022/psets/5/test_bank/

from bank import value

def test_hello():
    assert value("hello") == "$0"

def test_h_not_hello():
    assert value("h") == "$20"

def test_other_greeting():
    assert value("what's happening?") == "$100"

def test_start_with_space():
    assert value(" what's up?") == "$100"