from .base_page import BasePage
from playwright.sync_api import expect

class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #Locators
        self.profile_menu = page.get_by_role("link", name="Welcome back")

    def user_is_logged_in(self):
        expect(self.profile_menu).to_be_visible()

    def navigate_to_order_history(self):
        self.navigate("/index.php?rt=account/history")

    def verify_order_id(self, order_number):
        expect(self.page.get_by_text(f"Order ID: #{order_number}")).to_be_visible()