import time

import allure
from selenium import webdriver
from WEB.Locators.Locators_cart import Locators_Cart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Cart_Page:
    def __init__(self):
        self.driver = webdriver.Chrome
        self.wait = WebDriverWait(self.driver, 30)
        self.url_cart = Locators_Cart.CART_URL
        self.delete = Locators_Cart.DELETE_LINK
        self.place_order_btn = Locators_Cart.PLACE_ORDER_BUTTON
        self.name = Locators_Cart.CART_NAME
        self.country = Locators_Cart.CART_COUNTRY
        self.city = Locators_Cart.CART_CITY
        self.credit_card = Locators_Cart.CREDIT
        self.month = Locators_Cart.CART_MONTH
        self.year = Locators_Cart.CART_YEAR
        self.purchase_btn = Locators_Cart.PURCHASE
        self.close_btn = Locators_Cart.CART_CLOSE_BUTTON
        self.text = Locators_Cart.TEXT
        self.text_2 = Locators_Cart.TEXT_2
        self.thankyou_text = Locators_Cart.THANKYOU_TEXT
        self.ok_btn = Locators_Cart.OK_BUTTON


    @allure.step
    @allure.description('navigate product store')
    def navigate_to_web(self):
        self.driver = webdriver.Chrome()
        url = "https://www.demoblaze.com/index.html#"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description("click on cart link text")
    def click_cart_link_text(self):
        self.driver.find_element(By.LINK_TEXT, self.url_cart).click()
        time.sleep(4)
        text = self.driver.find_element(By.XPATH, self.text).text
        assert "Products" in text
        assert "Pic" in text
        assert "Title" in text
        assert "Price" in text
        assert "Total" in text
        time.sleep(3)

    @allure.step
    @allure.description("click on place order button")
    def click_place_order_btn(self):
        self.driver.find_element(By.XPATH, self.place_order_btn).click()
        self.driver.implicitly_wait(10)
        # text_2 = self.driver.find_element(By.XPATH, self.text_2).text
        # assert "Place order" in text_2
        self.driver.implicitly_wait(10)

    @allure.step
    @allure.description("insert correct name")
    def correct_name(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys("Mesganaw Ayehu")

    @allure.step
    @allure.description("insert incorrect name")
    def incorrect_name(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys("-/")

    @allure.step
    @allure.description("null name")
    def null_name(self):
        name = self.driver.find_element(By.ID, self.name)
        name.clear()
        name.send_keys("")

    @allure.step
    @allure.description("insert correct country")
    def correct_country(self):
        country = self.driver.find_element(By.ID, self.country)
        country.clear()
        country.send_keys("Israel")

    @allure.step
    @allure.description("insert incorrect country")
    def incorrect_country(self):
        country = self.driver.find_element(By.ID, self.country)
        country.clear()
        country.send_keys("bbb")

    @allure.step
    @allure.description("null country")
    def null_country(self):
        country = self.driver.find_element(By.ID, self.country)
        country.clear()
        country.send_keys("")

    @allure.step
    @allure.description("insert correct city")
    def correct_city(self):
        city = self.driver.find_element(By.ID, self.city)
        city.clear()
        city.send_keys("Jerusalem")

    @allure.step
    @allure.description("insert incorrect city")
    def incorrect_city(self):
        city = self.driver.find_element(By.ID, self.city)
        city.clear()
        city.send_keys("123")

    @allure.step
    @allure.description("null city")
    def null_city(self):
        city = self.driver.find_element(By.ID, self.city)
        city.clear()
        city.send_keys("")

    @allure.step
    @allure.description("insert correct credit card")
    def correct_credit_card(self):
        credit_card = self.driver.find_element(By.ID, self.credit_card)
        credit_card.clear()
        credit_card.send_keys("345620324568")
        self.driver.execute_script("window.scrollBy(0, 1000);")

    @allure.step
    @allure.description("insert incorrect credit card")
    def incorrect_credit_card(self):
        credit_card = self.driver.find_element(By.ID, self.credit_card)
        credit_card.clear()
        credit_card.send_keys("abcd")
        self.driver.execute_script("window.scrollBy(0, 1000);")

    @allure.step
    @allure.description("null credit card")
    def null_credit_card(self):
        credit_card = self.driver.find_element(By.ID, self.credit_card)
        credit_card.clear()
        credit_card.send_keys("")
        self.driver.execute_script("window.scrollBy(0, 1000);")

    @allure.step
    @allure.description("insert correct month")
    def correct_month(self):
        month = self.driver.find_element(By.ID, self.month)
        month.clear()
        month.send_keys("10")

    @allure.step
    @allure.description("insert incorrect month")
    def incorrect_month(self):
        month = self.driver.find_element(By.ID, self.month)
        month.clear()
        month.send_keys("AA")

    @allure.step
    @allure.description("null month")
    def null_month(self):
        month = self.driver.find_element(By.ID, self.month)
        month.clear()
        month.send_keys("")

    @allure.step
    @allure.description("insert correct year")
    def correct_year(self):
        year = self.driver.find_element(By.ID, self.year)
        year.clear()
        year.send_keys("2000")

    @allure.step
    @allure.description("insert incorrect year")
    def incorrect_year(self):
        year = self.driver.find_element(By.ID, self.year)
        year.clear()
        year.send_keys("two thousand")

    @allure.step
    @allure.description("null year")
    def null_year(self):
        year = self.driver.find_element(By.ID, self.year)
        year.clear()
        year.send_keys("")

    @allure.step
    @allure.description("click on purchase button")
    def click_purchase_btn(self):
        self.driver.find_element(By.XPATH, self.purchase_btn).click()
        time.sleep(3)

    @allure.step
    @allure.description("click on purchase button")
    def assertion_text(self):
        response = self.driver.find_element(By.XPATH, self.thankyou_text).text
        assert "Thank you for your purchase!" in response
        time.sleep(2)

    @allure.step
    @allure.description("click on close button")
    def click_close_btn(self):
        self.driver.find_element(By.XPATH, self.close_btn).click()
        time.sleep(3)


    @allure.step
    @allure.description("click on OK button")
    def click_ok_btn(self):
        self.driver.find_element(By.XPATH, self.ok_btn).click()

    @allure.step
    @allure.description("click on delete button")
    def click_delete_btn(self):
        self.driver.find_element(By.XPATH, self.delete).click()


    @allure.step
    @allure.description('Click ok/ accept alert message')
    def window_alert_accept(self):
        self.driver.switch_to.alert.accept()


    @property
    @allure.step
    @allure.description('Extracting message from window alert')
    def window_alert_text(self):
        return self.driver.switch_to.alert.text





