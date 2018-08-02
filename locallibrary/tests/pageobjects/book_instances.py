from selenium.webdriver.support.select import Select
from locallibrary.tests.helpers.locators import BookInstancesLocators
from locallibrary.tests.helpers import values


class BookInstancePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = BookInstancesLocators
        self.v = values

    def go_to_book_instance(self):
        self.driver.find_element_by_link_text(self.id.press_book_instance_link).click()

    def go_to_add_book_instance(self):
        self.driver.find_element_by_link_text(self.id.press_add_book_instance).click()

    def select_book(self):
        self.driver.find_element_by_xpath(self.id.select_book).click()

    def fill_book_imprint(self, imprint):
        self.driver.find_element_by_id(self.id.book_imprint).send_keys(imprint)

    def book_due(self):
        self.driver.find_element_by_id(self.id.book_due).send_keys(self.v.book_due_date)

    def borrower(self):
        select_borrower = Select(self.driver.find_element_by_id(self.id.book_borrower))
        select_borrower.select_by_index('1')

    def save_book_instance(self):
        self.driver.find_element_by_css_selector(self.id.save_instance).click()