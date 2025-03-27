from playwright.sync_api import Page
from pages.registration_page import RegistrationPage
from pages.shopping_page import ShoppingPage
from pages.profile_page import ProfilePage
from pages.checkout_page import CheckoutPage
from utils.test_data import generate_test_user



def test_purchase_flow(page: Page):
    # Initialize page objects
    registration_page = RegistrationPage(page)
    shopping_page = ShoppingPage(page)
    profile_page = ProfilePage(page)
    checkout_page = CheckoutPage(page)

    # Register new user
    user_data = generate_test_user()
    registration_page.navigate_to_register()
    registration_page.fill_registration_form(user_data)
    registration_page.submit_registration()

    # Check that user is logged in
    profile_page.user_is_logged_in()

    # Navigate to shirts and add the two most expensive to cart
    shopping_page.navigate_to_shirts()
    shopping_page.sort_by_price_desc()
    shopping_page.add_most_expensive_to_cart()
    shopping_page.go_to_checkout()

    checkout_page.confirm_order()
    checkout_page.is_order_successful()
    order_number = checkout_page.extract_order_number()


