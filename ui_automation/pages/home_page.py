from utils.base_page import BasePage
from locators.locators import HomePageLocators

class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        self.find_element(HomePageLocators.SEARCH_BAR).send_keys(product_name)
        self.click_element(HomePageLocators.SEARCH_BUTTON)

    def is_featured_product_displayed(self):
        return len(self.driver.find_elements(*HomePageLocators.FEATURED_PRODUCTS)) > 0
