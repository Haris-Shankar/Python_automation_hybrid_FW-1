from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginPage:

    text_username_xpath = "//input[@id ='user[email]']"
    text_password_id = "user[password]"
    button_login_xpath = "//button[normalize-space()='Sign in']"
    button_signout_xpath = "//button[normalize-space()='hash s']"
    option_signout_xpath = "//a[normalize-space()='Sign Out']"
    linktext_signin_css = "a[href='/users/sign_in']"
    #label_username_id = "userName-value"

    def __init__(self, driver):
        self.driver = driver


    def set_email_id(self, email):
        self.driver.find_element(By.XPATH, self.text_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_username_xpath).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(By.ID, self.text_password_id).clear()
        self.driver.find_element(By.ID, self.text_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.button_signout_xpath).click()
        self.driver.find_element(By.XPATH, self.option_signout_xpath).click()

        #dropdown = Select(drpdown)
        #dropdown.select_by_index(4)

    def click_signin_link(self):
        self.driver.find_element(By.CSS_SELECTOR,self.linktext_signin_css).click()

    # def get_username(self):
    #
    #     return self.driver.find_element(By.ID, self.label_username_id).text
