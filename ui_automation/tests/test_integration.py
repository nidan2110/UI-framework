import pytest
from pages.home_page import HomePage
from pages.cart_page import CartPage

@pytest.mark.usefixtures("setup")
@pytest.mark.skip
class TestIntegration:

    def test_integration_search_and_add_to_cart(self):
        """
        Integration test: Search for a product, add it to the cart, and proceed to checkout.
        """
        # Step 1: Go to the home page
        home_page = HomePage(self.driver)
        self.driver.get("https://naveenautomationlabs.com/opencart/index.php?route=common/home")
        self.driver.maximize_window()

        # Step 2: Search for a product (e.g., iPhone)
        home_page.search_product("iPhone")
        assert "Search - iPhone" in self.driver.title

        # Step 3: Add the first product to the cart
        home_page.add_first_product_to_cart()
        cart_page = CartPage(self.driver)
        assert cart_page.product_added_confirmation_is_displayed()

        # Step 4: Proceed to checkout
        cart_page.proceed_to_checkout()
        assert cart_page.is_checkout_page_displayed()

        # Optional: Refresh or navigate back to home if needed
        self.driver.refresh()
