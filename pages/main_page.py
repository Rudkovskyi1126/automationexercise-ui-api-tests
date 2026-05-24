from playwright.sync_api import Page

class MainPage:

    HOME = "a[href='/']"
    PRODUCTS = "a[href='/products']"
    CART = "a[href='/view_cart']"
    SIGNUP_LOGIN = "a[href='/login']"
    LOGOUT = "a[href='/logout']"
    DELETE_ACCOUNT = "a[href='/delete_account']"
    LOGGED_IN = "a:has-text('Logged in as')"


    def __init__(self, page: Page):
        self.page = page


