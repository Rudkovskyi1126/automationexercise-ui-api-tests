from playwright.sync_api import Page


class PaymentPage:

    NAME_ON_CARD = "input[name='name_on_card']"
    CARD_NUMBER = "input[name='card_number']"
    CVC = "input[name='cvc']"
    EXPIRY_MONTH = "input[name='expiry_month']"
    EXPIRY_YEAR = "input[name='expiry_year']"
    SUBMIT_BTN = "#submit"
    SUCCESS_MSG = "p:has-text('Congratulations! Your order has been confirmed!')"

    def __init__(self, page: Page):
        self.page = page

    def pay(self, name: str, card: str, cvc: str, month: str, year: str):
        self.page.locator(self.NAME_ON_CARD).fill(name)
        self.page.locator(self.CARD_NUMBER).fill(card)
        self.page.locator(self.CVC).fill(cvc)
        self.page.locator(self.EXPIRY_MONTH).fill(month)
        self.page.locator(self.EXPIRY_YEAR).fill(year)
        self.page.locator(self.SUBMIT_BTN).click()