from locallibrary.tests.helpers.locators import LanguagesPageLocators
from locallibrary.tests.helpers import values


class LanguagesPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = LanguagesPageLocators
        self.v = values

    def go_to_languages(self):
        self.driver.find_element_by_link_text(self.id.press_language_link).click()

    def go_to_add_language(self):
        self.driver.find_element_by_link_text(self.id.press_add_language).click()

    def fill_in_language(self, language):
        self.driver.find_element_by_id(self.id.fill_in_language).send_keys(language)

    def save_language(self):
        self.driver.find_element_by_css_selector(self.id.save_language).click()