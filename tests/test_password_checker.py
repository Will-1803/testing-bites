from lib.password_checker import *
import pytest


def test_password_valid():
    password = PasswordChecker()
    assert password.check('123456789')

def test_password_invalid():
    password = PasswordChecker()
    with pytest.raises(Exception) as e:
        password.check('123')
    error = str(e.value)
    assert error == "Invalid password, must be 8+ characters."