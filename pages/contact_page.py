from playwright.sync_api import Page
from pages.main_page import MainPage

class ContactPage:

    URL_CONTACT = "https://automationexercise.com/contact_us"
    TITLE = "h2:has-text('Get In Touch')"
    NAME_FIELD = "input[data-qa='name']"
    EMAIL_FIELD = "input[data-qa='email']"
    SUBJECT_FIELD = "input[data-qa='subject']"
    YOUR_MESSAGE_FIELD = "textarea[data-qa='message']"
    CHOOSE_FILE_BTN = "input[name='upload_file']"
    SUBMIT_BTN = "input[data-qa='submit-button']"
    SUCCESS_MESSAGE = "div.status.alert-success"
    HOME_BTN = "a.btn.btn-success"


    def __init__(self, page: Page):
        self.page = page

    def go_to_contact_page(self):
        self.page.goto(self.URL_CONTACT)

    def fill_and_submit(self, user_payload):
        self.page.locator(self.NAME_FIELD).fill(user_payload['name'])
        self.page.locator(self.EMAIL_FIELD).fill(user_payload['email'])
        self.page.locator(self.SUBJECT_FIELD).fill('Test Subject')
        self.page.locator(self.YOUR_MESSAGE_FIELD).fill('Test message')
        self.page.locator(self.CHOOSE_FILE_BTN).set_input_files('test_file.txt')
        self.page.on("dialog", lambda dialog:dialog.accept())
        self.page.locator(self.SUBMIT_BTN).click()




