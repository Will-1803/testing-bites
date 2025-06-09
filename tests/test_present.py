import pytest
from lib.present import *

def test_present_wrap_unwrap():
    present = Present()
    present.wrap('Toy')
    actual = present.unwrap()
    expected = 'Toy'
    assert actual == expected

def test_present_wrap_twice():
    present = Present()
    present.wrap('Toy')
    with pytest.raises(Exception) as e:
        present.wrap('Car')
    actual = str(e.value)
    expected = "A contents has already been wrapped."
    assert actual == expected

def test_present_unwrap_nothing():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    actual = str(e.value)
    expected = "No contents have been wrapped."
    assert actual == expected

def test_present_contents_doesnt_change():
    present = Present()
    present.wrap('Toy')
    with pytest.raises(Exception) as e:
        present.wrap('Car')
    actual = present.unwrap()
    expected = "Toy"
    assert actual == expected
