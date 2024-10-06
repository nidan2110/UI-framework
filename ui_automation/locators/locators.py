from selenium.webdriver.common.by import By

class HomePageLocators:
    SEARCH_BAR = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-default.btn-lg")
    FEATURED_PRODUCTS = (By.CSS_SELECTOR, ".product-layout")
    NAVIGATION_MENU = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li > a")
    LOGO = (By.CSS_SELECTOR, "img.img-responsive")
    CART_BTN = (By.ID, "cart")
    CAROUSEL = (By.ID,"div.slideshow swiper-viewport")
    CAROUSEL_ITEMS = (By.ID, "slideshow0")
    