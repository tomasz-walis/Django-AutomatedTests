from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.testcases.test_admin_login import TestAdminLogin
from locallibrary.tests.pageobjects.user_page import UserPage
from locallibrary.tests.helpers import values
import random
from time import sleep


class TestAuthorPage(EnvironmentSetup):

    def test_group_page(self):
        driver = self.driver
        v = values
        login = TestAdminLogin
        login.test_login(self)
        user = UserPage(driver)

        try:
            assert v.admin_login_page_title in driver.title
            user.go_to_users()
            assert v.select_user_to_change in driver.title
            user.go_to_add_user()
            assert v.add_user in driver.title
            user.fill_username(random.choice(v.users))
            user.fill_password(v.user_password)
            user.fill_confirm_password(v.user_password)
            user.add_new_user_bt()
            user.fill_first_name(v.user_first_name)
            user.fill_last_name(v.user_last_name)
            user.fill_user_email(v.user_email)
            user.add_user_permissions()
            user.add_new_user_bt()
            user.tick_to_delete_user()
            user.select_delete_option()
            user.press_go_button()
            assert v.confirm_delete in driver.title
            user.press_confirm()
            sleep(5)
            assert v.welcome_login_page_title in driver.title
        except Exception as e:
            print(e, "Page Failed to load")


