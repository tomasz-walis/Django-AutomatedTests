from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.testcases.test_admin_login import TestAdminLogin
from locallibrary.tests.pageobjects.author_page import AuthorPage
from locallibrary.tests.helpers import values
import random
from time import sleep


class TestAuthorPage(EnvironmentSetup):

    def test_group_page(self):
        driver = self.driver
        v = values
        login = TestAdminLogin
        login.test_login(self)
        author = AuthorPage(driver)

        try:
            assert v.welcome_login_page_title in driver.title
            print("group page loaded successfully")
            author.go_to_authors()
            assert v.select_author_to_change in driver.title
            author.go_to_add_author()
            assert v.add_author in driver.title
            author.fill_authors_name(random.choice(v.authors_name))
            author.fill_authors_last_name(random.choice(v.authors_last_name))
            author.fill_authors_bd(v.authors_bd)
            author.fill_authors_dd(v.authors_db)
            author.fill_book_title(random.choice(v.book_title))
            author.fill_book_summary(random.choice(v.book_summary))
            author.fill_isbn(random.choice(v.isbn))
            author.fill_book_genre()
            author.add_book_language()
            author.save_all()
            assert v.select_author_to_change in driver.title
            author.tick_to_delete_author()
            author.select_delete_option()
            author.press_go_button()
            assert v.confirm_delete in driver.title
            author.press_confirm()
        except Exception as e:
            print(e, "Page Failed to load")






