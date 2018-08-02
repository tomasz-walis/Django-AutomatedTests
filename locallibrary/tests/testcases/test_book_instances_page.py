from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.testcases.test_admin_login import TestAdminLogin
from locallibrary.tests.pageobjects.book_instances import BookInstancePage
from locallibrary.tests.helpers import values
from time import sleep
from random import choice


class TestAuthorPage(EnvironmentSetup):

    def test_group_page(self):
        driver = self.driver
        v = values
        login = TestAdminLogin
        login.test_login(self)
        book_instance = BookInstancePage(driver)

        try:
            assert v.welcome_login_page_title in driver.title
            book_instance.go_to_book_instance()
            assert v.book_instance_page in driver.title
            book_instance.go_to_add_book_instance()
            assert v.add_book_instance in driver.title
            book_instance.select_book()
            book_instance.fill_book_imprint(choice(v.imprint))
            book_instance.book_due()
            book_instance.borrower()
            book_instance.save_book_instance()
            sleep(5)
        except Exception as e:
            print(e, "Page Failed to load")
