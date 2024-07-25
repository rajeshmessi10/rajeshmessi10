import pytest


@pytest.mark.parametrize("n , expected" , [(1,2) , (3,4)])
def test_f(n,expected):
    assert n+1 == expected


