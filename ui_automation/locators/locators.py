from selenium.webdriver.common.by import By

class HomePageLocators:
    SEARCH_BAR = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, ".product-layout")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li > a")
