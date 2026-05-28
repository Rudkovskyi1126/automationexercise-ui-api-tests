from playwright.sync_api import Page
from pages.main_page import MainPage


class ProductPage:

    PICTURE_PRODUCT_CARD = "div img[src='/get_product_picture/1']"
    PRICE_PRODUCT_CARD = "div.productinfo.text-center h2"
    NAME_PRODUCT_CARD = "div.productinfo.text-center p"
    ADD_TO_CART = "div.productinfo a[data-product-id]"
    VIEW_PRODUCT_CARD = "a[href='/product_details/1']"

    TITLE_ALL_PRODUCTS = "h2:has-text('All Products')"
    PRODUCT_CARD = "div.col-sm-4"
    NAME_DETAIL_CARD = ".product-information h2"
    PRODUCT_DETAIL_PRICE = "div.product-information span span"
    ADD_TO_CART_DETAIL = "button:has-text('Add to cart')"
    CATEGORY_PRODUCT_CARD = "p:has-text('Category:')"
    AVAILABLE_PRODUCT_CARD = "p:has-text('Availability:')"
    CONDITION_PRODUCT_CARD = "p:has-text('Condition:')"
    BRAND_PRODUCT_CARD = "p:has-text('Brand:')"

    SEARCH_FIELD = "input[id='search_product']"
    SEARCH_BTN = "button[id='submit_search']"
    TITLE_SEARCH_PAGE = "h2:has-text('Searched Products')"

    MESSAGE_SUCCES_ADD_TO_CART = "h4:has-text('Added!')"
    CONTINUE_SHOPPING_BTN = "button.close-modal"
    MODAL_VIEW_CART = "a:has-text('View Cart')"
    QUANTITY_INPUT = "input#quantity"
    CART_QUANTITY = "td.cart_quantity button"

    def __init__(self, page: Page):
        self.page = page

    def go_to_products_page(self):
        self.page.locator(MainPage.PRODUCTS).click()

    def search_product(self):
        self.page.locator(MainPage.PRODUCTS).click()
        self.page.locator(self.SEARCH_FIELD).fill('Tshirts')
        self.page.locator(self.SEARCH_BTN).click()

    def add_products_to_cart(self, count: int):
        for i in range(count):
            self.page.locator(self.ADD_TO_CART).nth(i).scroll_into_view_if_needed()
            self.page.locator(self.ADD_TO_CART).nth(i).click()
            self.page.locator(self.MESSAGE_SUCCES_ADD_TO_CART).wait_for()
            if i < count - 1:
                self.page.locator(self.CONTINUE_SHOPPING_BTN).click()
            else:
                self.page.locator(self.MODAL_VIEW_CART).click()

