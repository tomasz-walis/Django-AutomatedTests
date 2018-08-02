from locallibrary.tests.helpers.locators import BookPageLocators
from locallibrary.tests.helpers import values
from selenium.webdriver.support.select import Select
import random


class BookPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = BookPageLocators
        self.v = values

    def go_to_books(self):
        self.driver.find_element_by_link_text(self.id.press_books_link).click()

    def go_to_add_book(self):
        self.driver.find_element_by_link_text(self.id.press_add_book).click()

    def fill_book_title(self, title):
        self.driver.find_element_by_id(self.id.book_title).send_keys(title)

    def select_author(self):
        index = [1, 2, 3]
        select_author = Select(self.driver.find_element_by_id(self.id.book_author))
        select_author.select_by_index(random.choice(index))

    def fill_book_summary(self, summary):
        self.driver.find_element_by_id(self.id.book_summary).send_keys(summary)

    def fill_book_isbn(self, isbn):
        self.driver.find_element_by_id(self.id.book_isbn).send_keys(isbn)

    def select_book_genre(self):
        select_genere = Select(self.driver.find_element_by_id(self.id.book_genre))
        select_genere.select_by_index('0')

    def select_book_language(self):
        language = Select(self.driver.find_element_by_id(self.id.book_language))
        language.select_by_index('1')

    def save_book(self):
        self.driver.find_element_by_css_selector(self.id.save_book).click()