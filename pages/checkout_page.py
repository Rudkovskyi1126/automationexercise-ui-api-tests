from playwright.sync_api import Page


class CheckoutPage():

    PROCEED_TO_CHECKOUT = "a:has-text('Proceed To Checkout')"
    REGISTER_LOGIN = ".modal-body a[href='/login']"
    TEXT = "textarea[name='message']"
    PLACE_ORDER = "a:has-text('Place Order')"


    def __init__(self, page:Page):
        self.page = page


    def proceed_to_checkout(self):
        self.page.locator(self.PROCEED_TO_CHECKOUT).click()

