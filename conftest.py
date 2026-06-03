import os
import uuid
import pytest
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright
from api.client import ApiClient
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.contact_page import ContactPage
from pages.products_page import ProductPage
from pages.cart_page import CartPage
from pages.main_page import MainPage
from pages.checkout_page import CheckoutPage
from pages.payment_page import PaymentPage

load_dotenv()
BASE_URL = "https://automationexercise.com/"


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def api_url():
    return os.getenv("API_URL")


@pytest.fixture(scope="session")
def api_client(api_url):
    client = ApiClient(api_url)
    yield client
    client.close()


@pytest.fixture
def user_payload():
    unique = uuid.uuid4().hex[:8]
    return {
        "name": f"Test User {unique}",
        "email": f"test_{unique}@example.com",
        "password": "Password123!",
        "firstname": "Test",
        "lastname": "User",
        "company": "Test Company",
        "address1": "123 Test Street",
        "address2": "",
        "country": "Finland",
        "zipcode": "00100",
        "state": "Uusimaa",
        "city": "Helsinki",
        "mobile_number": "0401234567",
    }


@pytest.fixture
def created_user(api_client, user_payload):
    api_client.post("/createAccount", data=user_payload)
    yield user_payload
    api_client.delete("/deleteAccount", data={"email": user_payload["email"], "password": user_payload["password"]})


@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def register_page(page):
    return RegisterPage(page)


@pytest.fixture
def contact_page(page):
    return ContactPage(page)


@pytest.fixture
def product_page(page):
    return ProductPage(page)


@pytest.fixture
def cart_page(page):
    return CartPage(page)


@pytest.fixture
def main_page(page):
    return MainPage(page)


@pytest.fixture
def checkout_page(page):
    return CheckoutPage(page)


@pytest.fixture
def payment_page(page):
    return PaymentPage(page)


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false").lower() == "true"
        browser = p.chromium.launch(headless=headless, args=["--disable-features=Translate", "--disable-translate", "--lang=en-US"])
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            locale="en-US",
        )
        yield context
        context.close()
        browser.close()


@pytest.fixture
def page(browser_context, base_url):
    page = browser_context.new_page()
    page.route("**/*doubleclick.net*", lambda route: route.abort())
    page.route("**/*googlesyndication.com*", lambda route: route.abort())
    page.route("**/*adsbygoogle*", lambda route: route.abort())
    page.route("**/*ads.google.com*", lambda route: route.abort())
    page.route("**/*pagead2.googlesyndication.com*", lambda route: route.abort())
    page.goto(base_url)
    try:
        page.locator("button:has-text('Consent')").click(timeout=3000)
    except:
        pass
    yield page
    page.context.clear_cookies()
    page.close()