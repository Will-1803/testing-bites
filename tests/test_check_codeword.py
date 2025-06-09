from lib.check_codeword import *

def test_check_codeword_correct():
    actual = check_codeword('horse')
    expected = 'Correct! Come in.'
    assert actual == expected

def test_check_codeword_incorrect():
    actual = check_codeword('dog')
    expected = 'WRONG!'
    assert actual == expected

def test_check_codeword_close():
    actual = check_codeword('house')
    expected = 'Close, but nope.'
    assert actual == expected


