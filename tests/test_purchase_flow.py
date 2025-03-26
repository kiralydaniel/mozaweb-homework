from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from utils.test_data import generate_test_user



def test_purchase_flow(page: Page):
    # Initialize page objects
    registration_page = RegistrationPage(page)

    # Register new user
    user_data = generate_test_user()
    registration_page.navigate_to_register()
    registration_page.fill_registration_form(user_data)
    registration_page.submit_registration()
    