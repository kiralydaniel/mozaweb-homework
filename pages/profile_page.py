from .base_page import BasePage
from playwright.sync_api import expect

class ProfilePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #Locators
        self.profile_menu = page.get_by_role("link", name="Welcome back")


    def user_is_logged_in(self):
        expect(self.profile_menu).to_be_visible()