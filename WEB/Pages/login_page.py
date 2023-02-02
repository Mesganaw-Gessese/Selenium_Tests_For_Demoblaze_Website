import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from WEB.Locators.Locators_login import Locators_Login
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Login_Page:
    def __init__(self):
        self.driver = webdriver.Chrome
        self.wait = WebDriverWait(self.driver, 30)
        self.login_url = Locators_Login.LOGIN_URL
        self.user_name = Locators_Login.LOGIN_USER_NAME
        self.password = Locators_Login.LOGIN_PASSWORD
        self.login_btn = Locators_Login.LOGIN_BUTTON
        self.close_btn = Locators_Login.LOGIN_CLOSE_BUTTON
        self.text = Locators_Login.TEXT
        self.name_of_user = Locators_Login.NAME_OF_USER
        self.logout = Locators_Login.LOGOUT

    @allure.description('navigate product store')
    def navigate_to_web(self):
        self.driver = webdriver.Chrome()
        url = "https://www.demoblaze.com/index.html#"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description("click on login link text")
    def click_login_link_text(self):
        self.driver.find_element(By.LINK_TEXT, self.login_url).click()
        time.sleep(4)
        text = self.driver.find_element(By.XPATH, self.text).text
        assert "Log in" in text

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
    @allure.description("click on login button")
    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.login_btn).click()
        time.sleep(4)

    @allure.step
    @allure.description("click on login button")
    def click_logout_link_text(self):
        self.driver.find_element(By.LINK_TEXT, self.logout).click()
        time.sleep(3)


    @allure.step
    @allure.description("click on login close button")
    def click_login_close_btn(self):
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