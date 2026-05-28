from playwright.sync_api import expect
from pages.products_page import ProductPage


def test_all_products_page(page):
    product_page = ProductPage(page)
    product_page.go_to_products_page()
    expect(page.locator(ProductPage.TITLE_ALL_PRODUCTS)).to_be_visible()
    expect(page.locator(ProductPage.PRODUCT_CARD).first).to_be_visible()
    expect(page.locator(ProductPage.PRICE_PRODUCT_CARD).first).to_be_visible()
    expect(page.locator(ProductPage.NAME_PRODUCT_CARD).first).to_be_visible()
    expect(page.locator(ProductPage.ADD_TO_CART).first).to_be_visible()
    expect(page.locator(ProductPage.VIEW_PRODUCT_CARD).first).to_be_visible()

def test_product_detail_page(page):
    product_page = ProductPage(page)
    product_page.go_to_products_page()
    page.locator(ProductPage.VIEW_PRODUCT_CARD).click()
    expect(page.locator(ProductPage.PICTURE_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.NAME_DETAIL_CARD)).to_be_visible()
    expect(page.locator(ProductPage.CATEGORY_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.AVAILABLE_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.CONDITION_PRODUCT_CARD)).to_be_visible()
    expect(page.locator(ProductPage.BRAND_PRODUCT_CARD)).to_be_visible()

def test_search_product(page):
    product_page = ProductPage(page)
    product_page.search_product()
    expect(page.locator(ProductPage.TITLE_SEARCH_PAGE)).to_be_visible()
    expect(page.locator(ProductPage.PRODUCT_CARD).first).to_be_visible()

