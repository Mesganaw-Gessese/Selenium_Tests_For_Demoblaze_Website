import time

import allure
from selenium import webdriver
from WEB.Locators.Locators_contact_us import Locators_ContactUs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Contact_Us_Page:
    def __init__(self):
        self.driver = webdriver.Chrome
        self.wait = WebDriverWait(self.driver, 30)
        self.url_contact = Locators_ContactUs.URL_CONTACT_US
        self.email = Locators_ContactUs.CONTACT_EMAIL
        self.name = Locators_ContactUs.CONTACT_NAME
        self.message = Locators_ContactUs.CONTACT_MESSAGE
        self.send_btn = Locators_ContactUs.SEND_MESSAGE_BUTTON
        self.close_btn = Locators_ContactUs.CLOSE_BUTTON
        self.text = Locators_ContactUs.TEXT

        # test home on categories phone clickable

    @allure.step
    @allure.description("navigate product store")
    def navigate_to_web(self):
            self.driver = webdriver.Chrome()
            url = "https://www.demoblaze.com/index.html#"
            self.driver.get(url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)

    @allure.step
    @allure.description("click on contact us link text")
    def click_contact_us_link_text(self):
        self.driver.find_element(By.LINK_TEXT,self.url_contact).click()
        time.sleep(4)
        text = self.driver.find_element(By.XPATH, self.text).text
        assert "New message" in text

    @allure.step
    @allure.description("insert correct contact email")
    def insert_correct_email(self):
        email = self.driver.find_element(By.ID, self.email)
        email.clear()
        email.send_keys("yehudaayehu@gmail.com")

    @allure.step
    @allure.description("insert correct contact name")
    def insert_correct_name(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys("Mesganaw Ayehu")

    @allure.step
    @allure.description("type Message")
    def type_message(self):
        message = self.driver.find_element(By.ID, self.name)
        message.clear()
        message.send_keys("hellow my name is mesganaw im wondering to talk with you about tests and bugs")

    @allure.step
    @allure.description("click on send message button")
    def click_send_button(self):
        self.driver.find_element(By.XPATH, self.send_btn).click()
        time.sleep(4)
        response_text = self.driver.switch_to.alert.text
        assert "message" in response_text

    @allure.step
    @allure.description("click on close button")
    def click_close_button(self):
        self.driver.find_element(By.XPATH, self.close_btn).click()
        time.sleep(4)

    @allure.step
    @allure.description("insert incorrect contact email")
    def insert_incorrect_email(self):
        email = self.driver.find_element(By.ID, self.email)
        email.clear()
        email.send_keys("yehudaayehu@gm")

    @allure.step
    @allure.description("null contact email")
    def null_contact_email(self):
        email = self.driver.find_element(By.ID, self.email)
        email.clear()
        email.send_keys("")

    @allure.step
    @allure.description("null contact name")
    def null_contact_name(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys("")

    @allure.step
    @allure.description("incorrect contact name")
    def incorrect_contact_name(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys("/-/")

    @allure.step
    @allure.description("null Message")
    def null_message(self):
        message = self.driver.find_element(By.ID, self.name)
        message.clear()
        message.send_keys("")

    @allure.step
    @allure.description('Click ok/ accept alert message')
    def window_alert_accept(self):
        self.driver.switch_to.alert.accept()
    #
    @property
    @allure.step
    @allure.description('Extracting message from window alert')
    def window_alert_text(self):
        return self.driver.switch_to.alert.text