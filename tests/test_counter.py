from lib.counter import *

def test_counter_0():
    counter = Counter()
    counter.add(0)
    actual = counter.report()
    expected = "Counted to 0 so far."
    assert actual == expected

def test_counter_add_1_number():
    counter = Counter()
    counter.add(25)
    actual = counter.report()
    expected = "Counted to 25 so far."
    assert actual == expected

def test_counter_add_2_numbers():
    counter = Counter()
    counter.add(5)
    counter.add(12)
    actual = counter.report()
    expected = "Counted to 17 so far."
    assert actual == expected