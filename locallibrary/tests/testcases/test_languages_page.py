from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.testcases.test_admin_login import TestAdminLogin
from locallibrary.tests.pageobjects.laguages_page import LanguagesPage
from locallibrary.tests.helpers import values

from random import choice
from time import sleep


class TestAuthorPage(EnvironmentSetup):

    def test_group_page(self):
        driver = self.driver
        v = values
        login = TestAdminLogin
        login.test_login(self)

        try:
            assert v.admin_login_page_title in driver.title
            language = LanguagesPage(driver)
            language.go_to_languages()
            language.go_to_add_language()
            language.fill_in_language(choice(v.languages))
            language.save_language()
            sleep(2)
        except Exception as e:
            print(e, "Page Failed to load")

