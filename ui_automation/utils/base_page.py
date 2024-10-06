from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        self.find_element(locator).click()

    def is_displayed(self, by,locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element.is_displayed()
        except:
            return False

    def is_clickable(self, by, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((by, locator))
            )
            return element.is_clickable()
        except:
            False

    def is_carousel_displayed(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception as e:
            print(f"Error checking carousel visibility: {e}")
            return False