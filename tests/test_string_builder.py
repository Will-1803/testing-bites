from lib.string_builder import *

def test_string_builder_add_1_string():
    string = StringBuilder()
    string.add('Hello')
    actual = string.output()
    expected = 'Hello'
    assert actual == expected

def test_string_builder_add_2_string():
    string = StringBuilder()
    string.add('Hello')
    string.add(', my name is John')
    actual = string.output()
    expected = 'Hello, my name is John'
    assert actual == expected

def test_string_builder_add_1_string_return_length():
    string = StringBuilder()
    string.add('Hello')
    actual = string.size()
    expected = 5
    assert actual == expected

def test_string_builder_add_2_string_return_length():
    string = StringBuilder()
    string.add('Hello')
    string.add(', my name is John')
    actual = string.size()
    expected = 22
    assert actual == expected