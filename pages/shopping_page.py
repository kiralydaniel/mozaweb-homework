from .base_page import BasePage

class ShoppingPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.apparel_menu = page.get_by_role("link", name="Apparel & accessories")
        self.shirts_submenu = page.get_by_role("link", name="T-shirts")
        self.price_short = page.locator("#sort")
        self.product_items = page.locator(".thumbnails.grid .thumbnail")
        self.product_price = page.locator(".oneprice")
        self.out_of_stock_label = page.locator("span.nostock")
        self.add_to_cart_button = page.locator("#product a.cart")

    def navigate_to_shirts(self):
        self.apparel_menu.hover()
        if self.shirts_submenu.is_visible():
            self.shirts_submenu.click()