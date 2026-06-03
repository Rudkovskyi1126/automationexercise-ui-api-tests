from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.register_page import RegisterPage


def test_login_valid_credentials(login_page, page, created_user):
    login_page.go_to_login_page()
    login_page.login(email=created_user['email'], password=created_user['password'])
    assert page.locator(MainPage.LOGGED_IN).is_visible()


def test_login_invalid_credentials(login_page, page):
    login_page.go_to_login_page()
    login_page.login(email='test1@gmail.com', password='123456789')
    assert page.locator(LoginPage.MESSAGE_INCORRECT_PWD).is_visible()


def test_logout_valid_credentials(login_page, page, created_user):
    login_page.go_to_login_page()
    login_page.login(email=created_user['email'], password=created_user['password'])
    login_page.logout()
    assert not page.locator(MainPage.LOGGED_IN).is_visible()


def test_register_new_user(login_page, register_page, page, user_payload):
    login_page.go_to_login_page()
    login_page.signup(email=user_payload['email'], name=user_payload['name'])
    page.wait_for_timeout(5000)
    register_page.fill_form(user_payload)
    assert page.locator(RegisterPage.MSG_ACCOUNT_CREATED).is_visible()


def test_register_existing_email(login_page, page, created_user):
    login_page.go_to_login_page()
    login_page.signup(email=created_user['email'], name=created_user['name'])
    assert page.locator(RegisterPage.MSG_ACCOUNT_EXIST).is_visible()
