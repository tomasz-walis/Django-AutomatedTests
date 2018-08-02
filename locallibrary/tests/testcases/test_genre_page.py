from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.testcases.test_admin_login import TestAdminLogin
from locallibrary.tests.pageobjects.genre_page import GenrePage
from locallibrary.tests.helpers import values
from time import sleep
from random import choice


class TestAuthorPage(EnvironmentSetup):

    def test_group_page(self):
        driver = self.driver
        v = values
        login = TestAdminLogin
        login.test_login(self)

        try:
            assert v.admin_login_page_title in driver.title
            print("Admin page loaded successfully")
            genre = GenrePage(driver)
            genre.go_to_genre()
            genre.go_to_add_genre()
            genre.fill_book_genre(choice(v.genres))
            genre.save_genre()
            sleep(5)
        except Exception as e:
            print(e, "Page Failed to load")

