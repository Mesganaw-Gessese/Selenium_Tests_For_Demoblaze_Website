import time

import allure
from selenium import webdriver
from WEB.Locators.Locators_home import Locators_Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Home_Page:
    def __init__(self):
        self.driver = webdriver.Chrome
        self.wait = WebDriverWait(self.driver, 30)
        self.url_ = Locators_Home.SYSTEM_URL
        self.nav_bar = Locators_Home.NAV_BAR
        self.ui = Locators_Home.NAV_BAR_UI
        self.li_home = Locators_Home.URL_HOME
        self.phone_ = Locators_Home.PHONE_URL
        self.laptop_ = Locators_Home.LAPTOP_URL
        self.monitor_ = Locators_Home.MONITOR_URL
        self.product_sony = Locators_Home.SONY_Z5_PRODUCT_URL
        self.cart_ = Locators_Home.ADD_CART_BTN
        self.products = Locators_Home.NO_OF_PRODUCTS
        self.product_class = Locators_Home.PRODUCT_CLASS
        self.description = Locators_Home.ABOUT_US_DESCRIPTION
        self.get_in_touch = Locators_Home.GET_IN_TOUCH_TXT
        self.text = Locators_Home.TEXT


# test home on categories phone clickable

    @allure.step
    @allure.description("Open product store")
    def login_to_web(self):
        self.driver = webdriver.Chrome()
        url = "https://www.demoblaze.com/index.html#"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description("click on phone link text")
    def click_phone_link_text(self):
        # self.driver = webdriver.Chrome
        self.driver.find_element(By.XPATH, self.phone_).click()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(5)
        self.driver.find_element(By.ID, self.products)
        no_products = self.driver.find_elements(By.CLASS_NAME, self.product_class)
        for x in no_products:
            print(len(no_products))
            assert len(no_products) == 7
            self.driver.implicitly_wait(10)
            break


# test home on categories laptop clickable
    @allure.step
    @allure.description("click on laptop link text")
    def click_laptop_link_text(self):
        self.driver.find_element(By.XPATH, self.laptop_).click()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(5)
        self.driver.find_element(By.ID, self.products)
        no_products = self.driver.find_elements(By.CLASS_NAME, self.product_class)
        for x in no_products:
            print(len(no_products))
            assert len(no_products) == 6
            self.driver.implicitly_wait(10)
            break

# test home on categories monitors clickable
    @allure.step
    @allure.description("click on monitors link text")
    def click_monitor_link_text(self):
        self.driver.find_element(By.XPATH, self.monitor_).click()
        self.driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(5)
        self.driver.find_element(By.ID, self.products)
        no_products = self.driver.find_elements(By.CLASS_NAME, self.product_class)
        for x in no_products:
            print(len(no_products))
            assert len(no_products) == 2
            self.driver.implicitly_wait(10)
            break

# test home link text clickable
    @allure.step
    @allure.description("click home link text")
    def click_monitor_link_text(self):
        self.driver.find_element(By.XPATH, self.li_home).click()
        self.driver.execute_script("window.scrollBy(0, 1000);")

# test home products clickable
    @allure.step
    @allure.description("click sony Z5 product")
    def click_home_link_text(self):
        self.driver.find_element(By.XPATH, self.product_sony).click()
        self.driver.execute_script("window.scrollBy(0, 1000);")

# test the home page footer have about us description
    @allure.step
    @allure.description("check about us description on the footer")
    def check_about_us_description(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.driver.implicitly_wait(10)
        description = self.driver.find_element(By.XPATH, self.description).text
        assert "About Us" in description


    @allure.step
    @allure.description("check get in touch on the footer")
    def check_get_in_touch_txt(self):
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 1000);")
        self.driver.implicitly_wait(10)
        get_in_touch = self.driver.find_element(By.XPATH, self.get_in_touch).text
        assert "Get in Touch" in get_in_touch

    @allure.step
    @allure.description("click on product sonny phone")
    def click_sonny_phone_product(self):
        self.driver.find_element(By.XPATH, self.product_sony).click()
        time.sleep(5)
        text = self.driver.find_element(By.XPATH, self.text).text
        assert "Sony xperia z5" in text

    @allure.step
    @allure.description("click on add to cart button")
    def click_add_to_cart_btn(self):
        # self.driver = webdriver.Chrome
        self.driver.find_element(By.XPATH, self.cart_).click()
        time.sleep(5)

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








