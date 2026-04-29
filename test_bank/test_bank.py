from bank import value

def test_value_0():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello, Newman") == 0

def test_value_20():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How you doing?") == 20

def test_value_100():
    assert value("whats up") == 100
    assert value("good morning") == 100
    assert value("Greetings") == 100