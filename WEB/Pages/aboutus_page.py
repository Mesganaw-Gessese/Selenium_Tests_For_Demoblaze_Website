import time

import allure
from selenium import webdriver
from WEB.Locators.Locators_about_us import Locators_About_Us
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class About_Us_Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)
        self.url_about_us = Locators_About_Us.URL_ABOUT_US
        self.close_btn = Locators_About_Us.ABOUT_US_CLOSE_BUTTON
        self.x_btn = Locators_About_Us.X_EXIT_BUTTON
        self.text = Locators_About_Us.TEXT


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
    def click_about_us_link_text(self):
        self.driver.find_element(By.LINK_TEXT, self.url_about_us).click()
        time.sleep(4)
        text = self.driver.find_element(By.XPATH, self.text).text
        assert "About us" in text

    @allure.step
    @allure.description("click on close button")
    def click_close_button(self):
        self.driver.find_element(By.XPATH, self.close_btn).click()

    @allure.step
    @allure.description("click on X button")
    def click_x_button(self):
        self.driver.find_element(By.XPATH, self.x_btn).click()