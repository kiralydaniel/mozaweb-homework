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
        self.cart_checkout_button = page.locator("#cart_checkout1")

    def navigate_to_shirts(self):
        self.apparel_menu.hover()
        if self.shirts_submenu.is_visible():
            self.shirts_submenu.click()
        self.page.wait_for_load_state("networkidle")

    def sort_by_price_desc(self):
        # Select the price descending option
        self.price_short.select_option("p.price-DESC")
        
        # Wait for the page to load and stabilize
        self.page.wait_for_load_state("networkidle")
        
        # Wait for the products to be visible after sorting
        self.product_items.first.wait_for(state="visible")

    def add_most_expensive_to_cart(self, num_items=2):
        added_count = 0
        shirts_page_url = self.page.url

        while added_count < num_items:
            # Wait for products to be visible before trying to access them
            self.product_items.first.wait_for(state="visible")
            
            products = self.product_items.all()

            for product in products:
                # Check if product is out of stock
                if product.locator("span.nostock").is_visible():
                    continue

                # Click on the product to open its page
                product.click()
                self.page.wait_for_load_state("networkidle")

                # Wait for add to cart button 
                self.add_to_cart_button.wait_for(state="visible")
                self.add_to_cart_button.click()
                self.page.wait_for_load_state("networkidle")
                added_count += 1

                # Only go back if we need more items
                if added_count < num_items:
                    self.page.goto(shirts_page_url)
                    self.page.wait_for_load_state("networkidle")
                    self.sort_by_price_desc()

                if added_count == num_items:
                    break

            if added_count == num_items:
                break

    def go_to_checkout(self):
        self.cart_checkout_button.click()
        self.page.wait_for_load_state("networkidle")