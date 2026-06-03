from playwright.sync_api import expect
from pages.contact_page import ContactPage


def test_contact_us_form(page, contact_page, user_payload):
    contact_page.go_to_contact_page()
    expect(page.locator(ContactPage.TITLE)).to_be_visible()
    contact_page.fill_and_submit(user_payload)
    expect(page.locator(ContactPage.SUCCESS_MESSAGE)).to_be_visible()
    contact_page.page.locator(contact_page.HOME_BTN).click()
    expect(page).to_have_url("https://automationexercise.com/")
