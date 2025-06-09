from lib.greet import *

def test_greet():
    actual = greet('John')
    expected = 'Hello, John!'
    assert actual == expected