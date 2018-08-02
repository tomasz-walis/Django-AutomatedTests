from locallibrary.tests.helpers.locators import GroupPageLocators
from locallibrary.tests.helpers import values
import random


class GroupsPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.id = GroupPageLocators
        self.v = values

    def go_to_groups(self):
        self.driver.find_element_by_link_text(self.id.press_groups_link).click()
        assert self.driver.title == self.v.groups_page_title

    def add_group(self):
        self.driver.find_element_by_link_text(self.id.add_group_link).click()

    def fill_in_group_name(self):
        self.driver.find_element_by_id(self.id.group_name).send_keys(random.choice(self.v.groups))

    def fill_in_group_permissions(self):
        self.driver.find_element_by_id(self.id.group_permissions).click()

    def save_new_group(self):
        self.driver.find_element_by_xpath(self.id.save_group).click()

    def search_for_group(self):
        self.driver.find_element_by_id(self.id.search_group).send_keys(self.v.search_group)

    def press_search_button(self):
        self.driver.find_element_by_xpath(self.id.bt_search).click()

    def select_check_box(self):
        self.driver.find_elements_by_class_name(self.id.group_check_box)[0].click()

    def select_action(self):
        self.driver.find_element_by_xpath(self.id.select_action).click()

    def press_bt_go(self):
        self.driver.find_element_by_css_selector(self.id.press_bt_go).click()

    def press_bt_confirm(self):
        self.driver.find_element_by_css_selector(self.id.press_bt_confirm).click()




