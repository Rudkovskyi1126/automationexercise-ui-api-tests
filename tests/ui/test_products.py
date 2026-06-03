from playwright.sync_api import expect
from pages.products_page import ProductPage
from pages.cart_page import CartPage


def test_all_products_page(page, product_page):
    product_page.go_to_products_page()
    expect(page.locator(ProductPage.TITLE_ALL_PRODUCTS)).to_be_visible()
    expect(page.locator(ProductPage.PRODUCT_CARD).first).to_be_visible()
    expect(page.locator(ProductPage.PRICE_PRODUCT_CARD).first).to_be_visible()
    expect(page.locator(ProductPage.NAME_PRODUCT_CARD).first).to_be_visible()
    expect(page.locator(ProductPage.ADD_TO_CART).first).to_be_visible()
    expect(page.locator(ProductPage.VIEW_PRODUCT_CARD).first).to_be_visible()


def test_product_detail_page(page, product_page):
    product_page.go_to_products_page()
    page.locator(ProductPage.VIEW_PRODUCT_CARD).click()
    expect(page.locator(ProductPage.PICTURE_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.NAME_DETAIL_CARD)).to_be_visible()
    expect(page.locator(ProductPage.CATEGORY_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.AVAILABLE_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.CONDITION_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.BRAND_PRODUCT_CARD)).to_be_visible()


def test_search_product(page, product_page):
    product_page.search_product()
    expect(page.locator(ProductPage.TITLE_SEARCH_PAGE)).to_be_visible()
    expect(page.locator(ProductPage.PRODUCT_CARD).first).to_be_visible()


def test_view_category_products(page, product_page):
    expect(page.locator(ProductPage.LEFT_SIDEBAR_CATEGORY)).to_be_visible()
    page.locator(ProductPage.WOMEN_CATEGORY).click()
    page.locator(ProductPage.WOMEN_DRESS).click()
    expect(page.locator(ProductPage.CATEGORY_TITLE)).to_contain_text("Women - Dress Products")
    page.wait_for_load_state("domcontentloaded")
    page.locator(ProductPage.MEN_CATEGORY).click()
    page.locator(ProductPage.MEN_TSHIRTS).click()
    expect(page.locator(ProductPage.CATEGORY_TITLE)).to_contain_text("Men - Tshirts Products")


def test_view_brand_products(page, product_page, cart_page):
    product_page.go_to_products_page()
    page.locator(ProductPage.BRAND_POLO).click()
    expect(page.locator(ProductPage.CATEGORY_TITLE)).to_contain_text("Polo")
    page.locator(ProductPage.BRAND_HM).click()
    expect(page.locator(ProductPage.CATEGORY_TITLE)).to_contain_text("H&M")
    product_page.add_products_to_cart(1)
    cart_page.go_to_cart()
    expect(page.locator(CartPage.CART_ITEM).first).to_be_visible()
