# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from pageObjects.LoginPage import LoginPage
# import pytest
# from utilities.read_properties import ReadData
# from utilities.logger import LogGen
#
# class Test_Login_001:
#     url = ReadData.get_url()
#     #url = "https://demoqa.com/login"
#     #url = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
#     username = ReadData.get_username()
#     #username = "hashan"
#     #username = "admin@yourstore.com"
#     pwd = ReadData.get_pwd()
#     #pwd = "Demo@123"
#
#     #pwd = "admin"
#
#     logger = LogGen.loggen()
#
#     def test_home_page_title(self, setup):
#         self.driver = setup
#         self.driver.maximize_window()
#         self.driver.get(self.url)
#         self.logger.info("*** starting the first test case ****")
#         actual_title = self.driver.title
#         self.driver.close()
#
#         if actual_title == "DEMOQA":
#             assert True
#         else:
#             assert False
#         self.logger.info("*** Ending the first test case ****")
#
#     def etest_login_admin(self, setup):
#         self.driver = setup
#         self.driver.maximize_window()
#         self.driver.get(self.url)
#         self.logger.info("*** starting the Second test case ****")
#         self.driver.implicitly_wait(5)
#         self.lp = LoginPage(self.driver)
#         time.sleep(3)
#         self.lp.set_email_id(self.username)
#         self.lp.set_password(self.pwd)
#         self.lp.click_login()
#         login_title = self.driver.title
#         print(login_title)
#
#         if self.lp.get_username() == "hashan":
#             assert True
#
#         else:
#             self.driver.save_screenshot('.\\Screenshots\\' + 'screenshot.png')
#             assert False
#         self.logger.info("*** Ending the second test case ****")
