from locallibrary.tests.helpers.locators import AdminPageLocators
from locallibrary.tests.helpers import values


class AdminLogin(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = AdminPageLocators
        self.v = values

    def userName(self, username):
        self.driver.find_element_by_id(self.id.admin_signIn_userName).send_keys(username)

    def password(self, passwrd):
        self.driver.find_element_by_id(self.id.admin_signIn_password).send_keys(passwrd)

    def log_in(self):
        self.driver.find_element_by_xpath(self.id.admin_signIn_button).click()
        assert self.driver.title == self.v.welcome_login_page_title
