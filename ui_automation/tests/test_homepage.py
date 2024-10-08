import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class TestHomePage:
    def test_search_product(self):
        """
        Test to search product from searchbar
        """
        home_page = HomePage(self.driver)
        home_page.search_product("iPhone")
        assert "Search - iPhone" in self.driver.title

        self.driver.refresh()

    def test_featured_products_displayed(self):
        """
        Test to check if the product are displayed
        """
        home_page = HomePage(self.driver)
        assert home_page.is_featured_product_displayed()

    def test_logo_is_displayed(self):
        """
        Test to verify the logo is displayed
        """
        home_page = HomePage(self.driver)
        assert home_page.image_is_displayed()

    def test_cart_btn_is_clicked(self):
        """
        Test to validate the working of cart button
        """
        home_page = HomePage(self.driver)
        assert home_page.cart_btn_working()
    
    @pytest.mark.xfail
    @pytest.mark.usefixtures("setup_fresh_browser")
    def test_carousel_is_displayed(self):
        """
        Test to check whether the carousel is visible"""
        home_page = HomePage(self.driver)
        print(f'carousal:{home_page.get_carousel_items}')
        assert home_page.get_carousel_items() == True, "Carousel is not displayed!"
        print("Current URL:", self.driver.current_url)
        print("Page Source:", self.driver.page_source)


    # def test_carousel_items_visible(self):
    #     home_page = HomePage(self.driver)
    #     items = home_page.get_carousel_items()
    #     assert len(items) > 0, "No carousel items are visible!"
    #     for item in items:
    #         assert item.is_displayed(), "Carousel item is not displayed!"

    @pytest.mark.usefixtures("setup_fresh_browser")
    def test_carousel_navigation(self):
        home_page = HomePage(self.driver)
        assert home_page.slide_carousel(), "Failed to slide the carousel!"

    # @pytest.mark.usefixtures("setup_fresh_browser")
    # def test_brand_logos_displayed(self):
    #     home_page = HomePage(self.driver)
    #     assert home_page.brand_logos_displayed(), "Brand Logos not displayed"
    
