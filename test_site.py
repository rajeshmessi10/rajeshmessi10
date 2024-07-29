import pytest
@pytest.mark.reg
def test_too(test_launch):
    driver = test_launch
    assert driver == driver
@pytest.mark.reg
def test_title(test_launch):
    driver = test_launch
    assert driver.title == driver.title


def test_title1(test_launch):
    driver = test_launch
    assert driver.title == driver.title
    assert 1 == 1


class Test():
    def test_title4(self, test_launch):
        driver = test_launch
        self.driver = driver.title
        assert self.driver == self.driver

@pytest.mark.parametrize("num,expected",((1,9) , (1,10) , (1,11) , (1,12)))
def test_mul(num , expected):
    assert 1 * expected == expected




