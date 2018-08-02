from locallibrary.tests.helpers.locators import AuthorsPageLocators
from locallibrary.tests.helpers import values


class AuthorPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = AuthorsPageLocators
        self.v = values

    def go_to_authors(self):
        self.driver.find_element_by_link_text(self.id.press_authors_link).click()

    def go_to_add_author(self):
        self.driver.find_element_by_link_text(self.id.press_add_author).click()

    def fill_authors_name(self, first_name):
        self.driver.find_element_by_id(self.id.authors_first_name).send_keys(first_name)

    def fill_authors_last_name(self, last_name):
        self.driver.find_element_by_id(self.id.authors_last_name).send_keys(last_name)

    def fill_authors_bd(self, birth_date):
        self.driver.find_element_by_id(self.id.authors_birth_date).send_keys(birth_date)

    def fill_authors_dd(self, death_date):
        self.driver.find_element_by_id(self.id.authors_death_date).send_keys(death_date)

    def fill_book_title(self, title):
        self.driver.find_element_by_id(self.id.add_book_title).send_keys(title)

    def fill_book_summary(self, summary):
        self.driver.find_element_by_id(self.id.add_book_summary).send_keys(summary)

    def fill_isbn(self, isbn):
        self.driver.find_element_by_id(self.id.add_book_isbn).send_keys(isbn)

    def fill_book_genre(self,):
        self.driver.find_element_by_xpath(self.id.add_book_genre).click()

    def add_book_language(self):
        self.driver.find_element_by_xpath(self.id.add_book_language).click()

    def save_all(self):
        self.driver.find_element_by_css_selector(self.id.save_author_and_book).click()

    def tick_to_delete_author(self):
        self.driver.find_element_by_xpath(self.id.select_delete_author).click()

    def select_delete_option(self):
        self.driver.find_element_by_xpath(self.id.select_delete).click()

    def press_go_button(self):
        self.driver.find_element_by_css_selector(self.id.bt_go).click()

    def press_confirm(self):
        self.driver.find_element_by_xpath(self.id.confirm_delete).click()





