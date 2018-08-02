from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.testcases.test_admin_login import TestAdminLogin
from locallibrary.tests.pageobjects.book_page import BookPage
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
            book = BookPage(driver)
            book.go_to_books()
            book.go_to_add_book()
            book.fill_book_title(choice(v.book_title))
            book.select_author()
            book.fill_book_summary(choice(v.book_summary))
            book.fill_book_isbn(choice(v.isbn))
            book.select_book_genre()
            book.select_book_language()
            book.save_book()
            sleep(4)
        except Exception as e:
            print(e, "Page Failed to load")

