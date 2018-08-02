from locallibrary.tests.pageobjects.admin_login_page import AdminLogin
from time import sleep
from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.helpers import values


class TestAdminLogin(EnvironmentSetup):

    def test_login(self):
        driver = self.driver
        self.driver.get(values.page_url)
        self.driver.set_page_load_timeout(20)
        v = values
        login = AdminLogin(driver)

        try:
            assert v.admin_login_page_title in driver.title
            print("Admin page loaded successfully")
            login.userName(v.admin_userName)
            login.password(v.admin_password)
            login.log_in()
            sleep(2)
            assert v.welcome_login_page_title in driver.title
        except Exception as e:
            print(e, "Page Failed to load")
