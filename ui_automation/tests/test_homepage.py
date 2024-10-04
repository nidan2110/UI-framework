import pytest
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup")
class TestHomePage:
    def test_search_product(self):
        home_page = HomePage(self.driver)
        home_page.search_product("iPhone")
        assert "Search - iPhone" in self.driver.title

    def test_featured_products_displayed(self):
        home_page = HomePage(self.driver)
        assert home_page.is_featured_product_displayed()

    # def test_logo_is_displayed(self):
    #     home_page = HomePage(self.driver)
    #     assert home_page.logo_is_displayed()