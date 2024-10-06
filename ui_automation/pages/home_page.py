import sys
sys.path.append(r'D:\UI_framework\ui_automation')
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
    

    def image_is_displayed(self):
        return self.is_displayed(*HomePageLocators.LOGO)
    
    def cart_btn_working(self):
        try:
            cart_btn = self.driver.find_element(*HomePageLocators.CART_BTN)
            cart_btn.click()
            return True
        except Exception as e:
            print(f"Error clicking cart buton {e}")
            return False
        

    def carousel_displayed(self):
        return self.is_displayed(*HomePageLocators.CAROUSEL)
    
    def get_carousel_items(self):
        return self.driver.find_elements(*HomePageLocators.CAROUSEL_ITEMS)
    
    # def slide_carousel(self):
    #     try:
    #         next_btn = self.driver.find_element(By.CSS_SELECTOR, "div.swiper-slide text-center swiper-slide-duplicate-active")
    #         next_btn.click()
    #         return True
    #     except Exception as e:
    #         print(f"Error sliding carousel: {e}")
    #         return False
        
