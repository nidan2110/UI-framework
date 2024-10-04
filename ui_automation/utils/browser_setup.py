import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def setup_browser():
    driver = webdriver.Chrome()  # Or any other browser like Firefox, Edge, etc.
    driver.maximize_window()
    yield driver
    driver.quit()
