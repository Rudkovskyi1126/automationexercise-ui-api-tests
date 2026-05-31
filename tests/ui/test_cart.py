from playwright.sync_api import expect
from pages.products_page import ProductPage
from pages.cart_page import CartPage
from pages.main_page import MainPage


def test_add_products_to_cart(page):
    product_page = ProductPage(page)
    product_page.go_to_products_page()
    product_page.add_products_to_cart(3)
    expect(page.locator(CartPage.CART_ITEM)).to_have_count(3)


def test_remove_product_from_cart(page):
    product_page = ProductPage(page)
    cart_page = CartPage(page)
    product_page.go_to_products_page()
    product_page.add_products_to_cart(1)
    cart_page.delete_item(0)
    expect(page.locator(CartPage.CART_ITEM)).to_have_count(0)
    expect(page.locator(CartPage.TITLE_EMPTY_CART)).to_be_visible()


def test_product_quantity_in_cart(page):
    product_page = ProductPage(page)
    product_page.go_to_products_page()
    page.locator(ProductPage.VIEW_PRODUCT_CARD).click()
    page.locator(ProductPage.QUANTITY_INPUT).fill("4")
    page.locator(ProductPage.ADD_TO_CART_DETAIL).click()
    page.locator(ProductPage.MESSAGE_SUCCES_ADD_TO_CART).wait_for()
    page.locator(ProductPage.MODAL_VIEW_CART).click()
    expect(page.locator(ProductPage.CART_QUANTITY)).to_have_text("4")
