from locallibrary.tests.helpers.locators import GenresPageLocators
from locallibrary.tests.helpers import values


class GenrePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = GenresPageLocators
        self.v = values

    def go_to_genre(self):
        self.driver.find_element_by_link_text(self.id.press_genres_link).click()

    def go_to_add_genre(self):
        self.driver.find_element_by_link_text(self.id.press_add_genre_link).click()

    def fill_book_genre(self, genre):
        self.driver.find_element_by_id(self.id.fill_genre).send_keys(genre)

    def save_genre(self):
        self.driver.find_element_by_css_selector(self.id.save_genre).click()