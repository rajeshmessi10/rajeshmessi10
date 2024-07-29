from selenium import webdriver
import pytest
@pytest.fixture(autouse = True , scope="session")
def test_launch():
    driver = webdriver.Chrome()
    driver.get("https://en.wikipedia.org/wiki/Lionel_Messi")
    yield driver
    print("closing connection quit")
    driver.quit()