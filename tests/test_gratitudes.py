from lib.gratitudes import *

def test_gratitudes_no_input():
    grat = Gratitudes()
    actual = grat.format()
    expected = 'Be grateful for: '
    assert actual == expected

def test_gratitudes_1_input():
    grat = Gratitudes()
    grat.add('people')
    actual = grat.format()
    expected = 'Be grateful for: people'
    assert actual == expected

def test_gratitudes_multiple_inputs():
    grat = Gratitudes()
    grat.add('people')
    grat.add('happiness')
    actual = grat.format()
    expected = 'Be grateful for: people, happiness'
    assert actual == expected