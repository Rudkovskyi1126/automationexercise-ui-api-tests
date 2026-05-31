from playwright.sync_api import Page
from pages.main_page import MainPage


class CartPage:

    CART_ITEM = "tr[id^='product-']"
    CART_DELETE_BTN = "a.cart_quantity_delete"
    TITLE_EMPTY_CART = "p:has-text('Cart is empty!')"

    def __init__(self, page: Page):
        self.page = page

    def go_to_cart(self):
        self.page.locator(MainPage.CART).first.click()

    def delete_item(self, index: int = 0):
        self.page.locator(self.CART_DELETE_BTN).nth(index).click()