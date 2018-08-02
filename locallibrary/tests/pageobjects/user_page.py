from locallibrary.tests.helpers.locators import UserPageLocators
from locallibrary.tests.helpers import values


class UserPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = UserPageLocators
        self.v = values

    def go_to_users(self):
        self.driver.find_element_by_link_text(self.id.press_users_link).click()

    def go_to_add_user(self):
        self.driver.find_element_by_link_text(self.id.press_add_user_link).click()

    def fill_username(self, username):
        self.driver.find_element_by_id(self.id.username).send_keys(username)

    def fill_password(self, password):
        self.driver.find_element_by_id(self.id.user_password).send_keys(password)

    def fill_confirm_password(self, conf_password):
        self.driver.find_element_by_id(self.id.user_confirm_password).send_keys(conf_password)

    def add_new_user_bt(self):
        self.driver.find_element_by_css_selector(self.id.add_new_user_bt).click()

    def fill_first_name(self, first_name):
        self.driver.find_element_by_id(self.id.user_first_name).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element_by_id(self.id.user_last_name).send_keys(last_name)

    def fill_user_email(self, email):
        self.driver.find_element_by_id(self.id.user_email).send_keys(email)

    def add_user_permissions(self):
        self.driver.find_element_by_id(self.id.user_permissions).click()

    def tick_to_delete_user(self):
        self.driver.find_element_by_xpath(self.id.select_check_box).click()

    def select_delete_option(self):
        self.driver.find_element_by_xpath(self.id.select_delete_option).click()

    def press_go_button(self):
        self.driver.find_element_by_css_selector(self.id.bt_go).click()

    def press_confirm(self):
        self.driver.find_element_by_css_selector(self.id.confirm_delete).click()
