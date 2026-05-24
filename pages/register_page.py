from playwright.sync_api import Page


class RegisterPage:

    MR_RADIO_BTN = "input[id='id_gender1']"
    MRS_RADIO_BTN = "input[id='id_gender2']"
    NAME_FIELD = "input[data-qa='name']"
    EMAIL_FIELD = "input[data-qa='email']"
    PASSWORD_FIELD = "input[data-qa='password']"
    DAY_DROPDOWN = "select[data-qa='days']"
    MONTH_DROPDOWN = "select[data-qa='months']"
    YEAR_DROPDOWN = "select[data-qa='years']"
    NEWSLETTER_CHECKBOX = "input[id='newsletter']"
    SPECIAL_OFFERS_CHECKBOX = "input[id='optin']"
    FIRST_NAME_FIELD = "input[id='first_name']"
    LAST_NAME_FIELD = "input[id='last_name']"
    COMPANY_FIELD = "input[id='company']"
    ADDRESS_FIELD = "input[id='address1']"
    COUNTRY_DROPDOWN = "select[id='country']"
    STATE_FIELD = "input[id='state']"
    CITY_FIELD = "input[id='city']"
    ZIPCODE_FIELD = "input[id='zipcode']"
    MOBILE_NUMBER_FIELD = "input[id='mobile_number']"
    CREATE_ACCOUNT_BTN = "button[data-qa='create-account']"
    MSG_ACCOUNT_CREATED = "h2:has-text('Account Created!')"
    MSG_ACCOUNT_EXIST = "p:has-text('Email Address already exist!')"



    def __init__(self, page: Page):
        self.page = page

    def fill_form(self, user):
        self.page.locator(self.MR_RADIO_BTN).click()
        # self.page.locator(self.NAME_FIELD).fill(user['name'])
        # self.page.locator(self.EMAIL_FIELD).fill(user['email'])
        self.page.locator(self.PASSWORD_FIELD).fill(user['password'])
        self.page.evaluate("window.scrollBy(0, 400)")

        self.page.locator(self.DAY_DROPDOWN).scroll_into_view_if_needed()
        self.page.locator(self.DAY_DROPDOWN).select_option(value="1")
        self.page.locator(self.MONTH_DROPDOWN).select_option(value="5")
        self.page.locator(self.YEAR_DROPDOWN).select_option(value="1999")
        self.page.locator(self.NEWSLETTER_CHECKBOX).click()
        self.page.locator(self.SPECIAL_OFFERS_CHECKBOX).click()
        self.page.locator(self.FIRST_NAME_FIELD).fill(user['firstname'])
        self.page.locator(self.LAST_NAME_FIELD).fill(user['lastname'])
        self.page.locator(self.COMPANY_FIELD).fill(user['company'])
        self.page.locator(self.ADDRESS_FIELD).fill(user['address1'])
        self.page.locator(self.COUNTRY_DROPDOWN).select_option(value="Canada")
        self.page.locator(self.STATE_FIELD).fill(user['state'])
        self.page.locator(self.CITY_FIELD).fill(user['city'])
        self.page.locator(self.ZIPCODE_FIELD).fill(user['zipcode'])
        self.page.locator(self.MOBILE_NUMBER_FIELD).fill(user['mobile_number'])
        self.page.locator(self.CREATE_ACCOUNT_BTN).click()


