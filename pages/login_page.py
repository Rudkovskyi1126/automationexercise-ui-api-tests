from playwright.sync_api import Page
from pages.main_page import MainPage
from pages.register_page import RegisterPage


class LoginPage:


    SIGNUP_LOGIN_BTN = "a[href='/login']"
    EMAIL_FIELD = "input[data-qa='login-email']"
    PASSWORD_FIELD = "input[data-qa='login-password']"
    NAME_FIELD = "input[data-qa='signup-name']"
    SIGNUP_EMAIL_FIELD = "input[data-qa='signup-email']"
    LOGIN_BTN = "button[data-qa='login-button']"
    SIGNUP_BTN = "button[data-qa='signup-button']"
    MESSAGE_INCORRECT_PWD = "p:has-text('Your email or password is incorrect!')"


    def __init__(self, page: Page):
        self.page = page


    def go_to_login_page(self):
        self.page.locator(self.SIGNUP_LOGIN_BTN).click()
        try:
            self.page.locator("button:has-text('Consent')").click(timeout=3000)
        except:
            pass


    def login(self, email, password):
        self.page.locator(self.EMAIL_FIELD).fill(email)
        self.page.locator(self.PASSWORD_FIELD).fill(password)
        self.page.locator(self.LOGIN_BTN).click()


    def logout(self):
        self.page.locator(MainPage.LOGOUT).click()


    def signup(self, name, email):
        self.page.locator(self.NAME_FIELD).fill(name)
        self.page.locator(self.SIGNUP_EMAIL_FIELD).fill(email)
        self.page.locator(self.SIGNUP_BTN).click()


    def delete_account(self):
        pass





