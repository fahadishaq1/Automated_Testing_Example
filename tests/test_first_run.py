import pytest
from src.first_run.example_code import capitalize_name, uppercase_name, foo


def test_capitalize_name():
    assert capitalize_name('david') == 'David'
    assert capitalize_name('fahad') == 'Fahad'


def test_uppercase_name():
    assert uppercase_name('david') == 'DAVID'
    assert uppercase_name('fahad') == 'FAHAD'


@pytest.mark.parametrize("number", [1, 2, 3, 42])
def test_foo(number):
    assert foo(number) > 0
