from playwright.sync_api import Page


class MainPage:

    HOME = "a[href='/']"
    PRODUCTS = "a[href='/products']"
    CART = "a[href='/view_cart']"
    SIGNUP_LOGIN = "a[href='/login']"
    LOGOUT = "a[href='/logout']"
    DELETE_ACCOUNT = "a[href='/delete_account']"
    LOGGED_IN = "a:has-text('Logged in as')"
    CONTACT_US = "a[href='/contact_US']"
    TEST_CASES = "a[href='/test_cases']"

    SUBSCRIPTION_HEADING = "h2:has-text('SUBSCRIPTION')"
    SUBSCRIPTION_EMAIL = "input[id='susbscribe_email']"
    SUBSCRIPTION_BTN = "button[id='subscribe']"
    SUBSCRIPTION_SUCCESS = "div#success-subscribe"

    def __init__(self, page: Page):
        self.page = page

    def subscribe(self, email: str):
        self.page.locator(self.SUBSCRIPTION_EMAIL).scroll_into_view_if_needed()
        self.page.locator(self.SUBSCRIPTION_EMAIL).fill(email)
        self.page.locator(self.SUBSCRIPTION_BTN).click()