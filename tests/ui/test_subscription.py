from playwright.sync_api import expect
from pages.main_page import MainPage
from pages.cart_page import CartPage


def test_subscription_on_home_page(page):
    main_page = MainPage(page)
    expect(page.locator(MainPage.SUBSCRIPTION_HEADING)).to_be_visible()
    main_page.subscribe("subscriber@test.com")
    expect(page.locator(MainPage.SUBSCRIPTION_SUCCESS)).to_be_visible()


def test_subscription_on_cart_page(page):
    cart_page = CartPage(page)
    cart_page.go_to_cart()
    expect(page.locator(MainPage.SUBSCRIPTION_HEADING)).to_be_visible()
    main_page = MainPage(page)
    main_page.subscribe("subscriber@test.com")
    expect(page.locator(MainPage.SUBSCRIPTION_SUCCESS)).to_be_visible()