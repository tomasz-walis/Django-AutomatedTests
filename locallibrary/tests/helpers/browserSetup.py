import unittest
import datetime
from selenium import webdriver


class EnvironmentSetup(unittest.TestCase):

    # setUP contains the browser setup attributes
    def setUp(self):
        self.driver = webdriver.Chrome()
        print("Run Started at :" + str(datetime.datetime.now()))
        # self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    # tearDown method just to close all the browser instances and then quit
    def tearDown(self):
        if self.driver is not None:
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
