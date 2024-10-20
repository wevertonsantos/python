##https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

from twttr import shorten

def test_default():
    assert shorten() == "Output: "

def test_argument():
    assert shorten("Work") == "Output: Wrk"