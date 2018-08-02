from locallibrary.tests.helpers.browserSetup import EnvironmentSetup
from locallibrary.tests.testcases.test_admin_login import TestAdminLogin
from locallibrary.tests.pageobjects.groups_page import GroupsPage
from locallibrary.tests.helpers import values
import unittest
from time import sleep

class TestGroupPage(EnvironmentSetup):

    def test_group_page(self):
        driver = self.driver
        v = values
        login = TestAdminLogin
        login.test_login(self)
        group = GroupsPage(driver)
        group.go_to_groups()

        try:
            if driver.title == v.groups_page_title:
                print("WebPage loaded successfully")
                group.add_group()
                self.assertEqual(driver.title, v.add_group_title)
                sleep(2)

            if driver.title == v.add_group_title:
                group.fill_in_group_name()
                group.fill_in_group_permissions()
                group.save_new_group()
                self.assertEqual(driver.title, v.group_to_change)

            if driver.title == v.group_to_change:
                group.search_for_group()
                group.press_search_button()
                group.select_check_box()
                group.select_action()
                group.press_bt_go()
                group.press_bt_confirm()
                self.assertEqual(driver.title, v.confirm_delete)
                sleep(2)

        except Exception as e:
            print(e, "WebPage Failed to load")








