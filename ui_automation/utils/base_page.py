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

    # def is_displayed(self, locator):
    #     try:
    #         return self.driver.find_element(locator).is_displayed()
    #     except NotImplementedError:
    #         return False