from playwright.sync_api import expect
from pages.main_page import MainPage


def test_navigate_to_test_cases_page(page):
    page.locator(MainPage.TEST_CASES).first.click()
    expect(page).to_have_url("https://automationexercise.com/test_cases")


def test_test_cases_content_visible(page):
    page.locator(MainPage.TEST_CASES).first.click()
    expect(page.locator("b:has-text('Test Cases')")).to_be_visible()
    expect(page.locator("div.panel-group").first).to_be_visible()
