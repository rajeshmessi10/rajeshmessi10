import pytest


def add(a,b):
    return a+b

@pytest.mark.parametrize("a,b,exp" , [(1,2,3) , (1,23,24) , (1,34,35),(2,34,37)])
def test_check(a,b,exp):
    assert add(a,b) == exp


import pytest

@pytest.fixture()
def fixture_add():
    return 57



def test_fixture(fixture_add):
    assert fixture_add == 57




