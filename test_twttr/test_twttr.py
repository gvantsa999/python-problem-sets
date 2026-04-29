from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("AEIOU") == ""

def test_shorten_numbers():
    assert shorten("12345") == "12345"

def test_shorten_punctuation():
    assert shorten("!?,.") == "!?,."