import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pageObjects.LoginPage import LoginPage
import pytest
from utilities.read_properties import ReadData
from utilities.logger import LogGen
from utilities import utility_excel


class Test_Login_DDT_001:

    url = ReadData.get_url()
    path = ".//TestData/Sampledata.xlsx"
    sheet_name = "Sheet1"

    logger = LogGen.loggen()

    def test_login_admin_ddt(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.logger.info("*** starting the 1st ddt test case ****")
        self.driver.implicitly_wait(5)
        self.lp = LoginPage(self.driver)
        time.sleep(3)
        self.max_row = utility_excel.get_row_count(self.path, self.sheet_name)
        self.lst = []

        for r in range(2, self.max_row + 1):
            self.username = utility_excel.read_data(self.path, self.sheet_name, r, 1)
            self.pwd = utility_excel.read_data(self.path, self.sheet_name, r, 2)
            self.exp_value = utility_excel.read_data(self.path, self.sheet_name, r, 3)

            if r != 2:
                self.lp.click_signin_link()

            self.lp.set_email_id(self.username)
            self.lp.set_password(self.pwd)
            self.lp.click_login()
            time.sleep(3)
            login_title = self.driver.title
            self.exp_title = "All Products - UltimateQA"
            print(login_title)
            #self.exp_username = "hashan"

            print(self.exp_value)
            if self.exp_title == login_title:
                if self.exp_value == "pass":
                    print("get into if check")
                    self.logger.info(f"{r} iteration")
                    self.lp.click_logout()
                    print("Logged out")
                    self.lst.append("pass")

                elif self.exp_value == "fail":
                    self.logger.info(f"{r} iteration")
                    time.sleep(3)
                    self.lp.click_logout()
                    time.sleep(3)
                    self.lst.append("fail")

            elif self.exp_title != login_title:
                if self.exp_value == "pass":
                    print("get into elif check")
                    self.logger.info(f"{r} iteration")
                    self.lst.append("fail")

                elif self.exp_value == "fail":
                    self.logger.info(f"{r} iteration")
                    self.lst.append("pass")

        if "fail" not in self.lst:
            self.driver.close()
            assert True

        else:
            self.driver.save_screenshot('.\\Screenshots\\' + 'screenshot.png')
            self.driver.close()
            assert False

