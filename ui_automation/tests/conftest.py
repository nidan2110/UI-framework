import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()  # You can replace this with your preferred browser
    request.cls.driver = driver
    driver.get("https://naveenautomationlabs.com/opencart/index.php?route=common/home")
    driver.maximize_window()
    yield driver
    driver.quit()
