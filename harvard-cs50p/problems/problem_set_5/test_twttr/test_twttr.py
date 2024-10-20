from twttr import shorten

def test_default():
    assert shorten() == "Output: "

def test_argument():
    assert shorten("Work") == "Output: Wrk"