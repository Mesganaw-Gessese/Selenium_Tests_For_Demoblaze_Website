import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from WEB.Locators.Locators_sign_up import Locators_Sign_UP
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Sign_Up_Page:
    def __init__(self):
        self.driver = webdriver.Chrome
        self.wait = WebDriverWait(self.driver, 30)
        self.sign_url = Locators_Sign_UP.SIGN_URL
        self.user_name = Locators_Sign_UP.SIGN_USER_NAME
        self.password = Locators_Sign_UP.SIGN_PASSWORD
        self.sign_up_btn = Locators_Sign_UP.SIGN_UP_BUTTON
        self.close_btn = Locators_Sign_UP.SIGN_CLOSE_BUTTON
        self.text = Locators_Sign_UP.Text

    @allure.description('navigate product store')
    def navigate_to_web(self):
        self.driver = webdriver.Chrome()
        url = "https://www.demoblaze.com/index.html#"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description("click on sign up link text")
    def click_sign_up_link_text(self):
        self.driver.find_element(By.LINK_TEXT, self.sign_url).click()
        time.sleep(4)
        text = self.driver.find_element(By.XPATH, self.text).text
        assert "Sign up" in text

    @allure.step
    @allure.description("insert user name")
    def user_name_field(self, user_names):
        user_name = self.driver.find_element(By.ID, self.user_name)
        user_name.clear()
        user_name.send_keys(user_names)

    @allure.step
    @allure.description("insert password")
    def password_field(self, passwords):
        password = self.driver.find_element(By.ID, self.password)
        password.clear()
        password.send_keys(passwords)

    @allure.step
    @allure.description("click on sign up button")
    def click_sign_up_btn(self):
        self.driver.find_element(By.XPATH, self.sign_up_btn).click()
        time.sleep(4)

    @allure.step
    @allure.description("click on sign up close button")
    def click_sign_up_close_btn(self):
        self.driver.find_element(By.XPATH, self.close_btn).click()
        time.sleep(2)

    @allure.step
    @allure.description('Click ok on alert message')
    def window_alert_accept(self):
        self.driver.switch_to.alert.accept()

    #
    @property
    @allure.step
    @allure.description('Extracting message from window alert')
    def window_alert_text(self):
        return self.driver.switch_to.alert.text