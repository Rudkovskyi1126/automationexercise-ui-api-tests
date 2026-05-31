from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage
from pages.products_page import ProductPage
from pages.checkout_page import CheckoutPage
from pages.register_page import RegisterPage


def test_place_order_register_while_checkout(page, user_payload):
    page.locator(ProductPage.ADD_TO_CART).first.click()
    page.locator(ProductPage.CONTINUE_SHOPPING_BTN).click()
    page.locator(MainPage.CART).first.click()
    page.locator(CheckoutPage.PROCEED_TO_CHECKOUT).click()
    page.locator(CheckoutPage.REGISTER_LOGIN).click()
    login_page = LoginPage(page)
    login_page.signup(user_payload["name"], user_payload["email"])
    page.wait_for_url("**/signup")
    register_page = RegisterPage(page)
    register_page.fill_form(user_payload)
    expect(page.locator(RegisterPage.MSG_ACCOUNT_CREATED)).to_be_visible()
    page.locator(RegisterPage.CONTINUE_BTN).click()
    expect(page.locator(MainPage.LOGGED_IN)).to_be_visible()
    page.locator(MainPage.CART).first.click()
    page.locator(CheckoutPage.PROCEED_TO_CHECKOUT).click()
    page.locator(CheckoutPage.TEXT).fill("Test order")
    page.locator(CheckoutPage.PLACE_ORDER).click()
    payment_page = PaymentPage(page)
    payment_page.pay("Test User", "4111111111111111", "123", "12", "2027")
    expect(page.locator(PaymentPage.SUCCESS_MSG)).to_be_visible(timeout=15000)
    page.locator(MainPage.DELETE_ACCOUNT).click()
    expect(page.locator(RegisterPage.MSG_ACCOUNT_DELETED)).to_be_visible()


def test_place_order_register_before_checkout(page, user_payload):
    login_page = LoginPage(page)
    page.locator(MainPage.SIGNUP_LOGIN).click()
    login_page.signup(user_payload["name"], user_payload["email"])
    register_page = RegisterPage(page)
    register_page.fill_form(user_payload)
    expect(page.locator(RegisterPage.MSG_ACCOUNT_CREATED)).to_be_visible()
    page.locator(RegisterPage.CONTINUE_BTN).click()
    expect(page.locator(MainPage.LOGGED_IN)).to_be_visible()
    page.locator(ProductPage.ADD_TO_CART).first.click()
    page.locator(ProductPage.CONTINUE_SHOPPING_BTN).wait_for(state="visible")
    page.locator(ProductPage.CONTINUE_SHOPPING_BTN).click()
    page.locator(MainPage.CART).first.click()
    page.locator(CheckoutPage.PROCEED_TO_CHECKOUT).click()
    page.locator(CheckoutPage.TEXT).fill("Test order")
    page.locator(CheckoutPage.PLACE_ORDER).click()
    payment_page = PaymentPage(page)
    payment_page.pay("Test User", "4111111111111111", "123", "12", "2027")
    expect(page.locator(PaymentPage.SUCCESS_MSG)).to_be_visible(timeout=15000)
    page.locator(MainPage.DELETE_ACCOUNT).click()
    expect(page.locator(RegisterPage.MSG_ACCOUNT_DELETED)).to_be_visible()


def test_place_order_login_before_checkout(page, created_user):
    login_page = LoginPage(page)
    page.locator(MainPage.SIGNUP_LOGIN).click()
    login_page.login(created_user["email"], created_user["password"])
    expect(page.locator(MainPage.LOGGED_IN)).to_be_visible()
    page.locator(ProductPage.ADD_TO_CART).first.click()
    page.locator(ProductPage.CONTINUE_SHOPPING_BTN).wait_for(state="visible")
    page.locator(ProductPage.CONTINUE_SHOPPING_BTN).click()
    page.locator(MainPage.CART).first.click()
    page.locator(CheckoutPage.PROCEED_TO_CHECKOUT).click()
    page.locator(CheckoutPage.TEXT).fill("Test order")
    page.locator(CheckoutPage.PLACE_ORDER).click()
    payment_page = PaymentPage(page)
    payment_page.pay("Test User", "4111111111111111", "123", "12", "2027")
    expect(page.locator(PaymentPage.SUCCESS_MSG)).to_be_visible(timeout=15000)
    page.locator(MainPage.DELETE_ACCOUNT).click()
    expect(page.locator(RegisterPage.MSG_ACCOUNT_DELETED)).to_be_visible()
