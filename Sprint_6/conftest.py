import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    browser = webdriver.Firefox()
    yield browser
    browser.quit()
