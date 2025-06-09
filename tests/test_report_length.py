from lib.report_length import *

def test_report_length_pass_1():
    actual = report_length('hello')
    expected = 'This string was 5 characters long.'
    assert actual == expected

def test_report_length_pass_2():
    actual = report_length('goodbye')
    expected = 'This string was 7 characters long.'
    assert actual == expected