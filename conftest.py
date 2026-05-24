import os
import uuid
import pytest
import requests
from dotenv import load_dotenv
from playwright.sync_api import sync_playwright

load_dotenv()
BASE_URL = "https://automationexercise.com/"


@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")


@pytest.fixture(scope="session")
def api_url():
    return os.getenv("API_URL")


@pytest.fixture(scope="session")
def api_client():
    session = requests.Session()
    session.headers.update(
    {
        "Content-Type": "application/x-www-form-urlencoded",
    })
    yield session
    session.close()


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
def created_user(api_client, api_url, user_payload):
    api_client.post(f"{api_url}/createAccount", data=user_payload)
    yield user_payload
    api_client.delete(
        f"{api_url}/deleteAccount",
        data=
        {
            "email": user_payload["email"],
            "password": user_payload["password"],
        }
    )


@pytest.fixture(scope="session")
def browser_context():
    with sync_playwright() as p:
        headless = os.getenv("CI", "false").lower() == "true"
        browser = p.chromium.launch(headless=headless)
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
    page.goto(base_url)
    try:
        page.locator("button:has-text('Consent')").click(timeout=3000)
    except:
        pass
    yield page
    page.context.clear_cookies()
    page.close()
