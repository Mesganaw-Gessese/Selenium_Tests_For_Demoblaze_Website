import pytest
import allure
from _pytest import mark
import time
from WEB.Pages.cart_page import *

class Test_Cart:

    @allure.description('Test contact us clickable')
    @pytest.mark.sanity
    def test_cart_clickable(self):
        cart = Cart_Page()
        cart.navigate_to_web()
        cart.click_cart_link_text()

    @allure.description('Test place order correctly')
    @pytest.mark.sanity
    def test_place_order_correctly(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.correct_name()
        place_order.correct_country()
        time.sleep(2)
        place_order.correct_city()
        time.sleep(2)
        place_order.correct_credit_card()
        time.sleep(2)
        place_order.correct_month()
        time.sleep(2)
        place_order.correct_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        place_order.assertion_text()
        place_order.click_ok_btn()

    @allure.description('Test place order incorrectly')
    @pytest.mark.sanity
    def test_place_order_incorrectly(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.incorrect_name()
        place_order.incorrect_country()
        time.sleep(2)
        place_order.incorrect_city()
        time.sleep(2)
        place_order.incorrect_credit_card()
        time.sleep(2)
        place_order.incorrect_month()
        time.sleep(2)
        place_order.incorrect_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        place_order.click_ok_btn()
        alert = place_order.window_alert_text()
        assert "Please fill out the fild correctly" in alert

    @allure.description('Test place order null')
    @pytest.mark.sanity
    def test_place_order_null(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.null_name()
        place_order.null_country()
        time.sleep(2)
        place_order.null_city()
        time.sleep(2)
        place_order.null_credit_card()
        time.sleep(2)
        place_order.null_month()
        time.sleep(2)
        place_order.null_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text()
        assert "Please fill out the fild correctly" in alert

    @allure.description('Test cart place order close button works correctly')
    @pytest.mark.sanity
    def test_place_order_null(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.null_name()
        place_order.null_country()
        time.sleep(2)
        place_order.null_city()
        time.sleep(2)
        place_order.null_credit_card()
        time.sleep(2)
        place_order.null_month()
        time.sleep(2)
        place_order.null_year()
        time.sleep(2)
        place_order.click_close_btn()

    @allure.description('Test place order null name')
    @pytest.mark.sanity
    def test_place_order_null_name(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.null_name()
        place_order.correct_country()
        time.sleep(2)
        place_order.correct_city()
        time.sleep(2)
        place_order.correct_credit_card()
        time.sleep(2)
        place_order.correct_month()
        time.sleep(2)
        place_order.correct_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out name" in alert

    @allure.description('Test place order null credit card')
    @pytest.mark.sanity
    def test_place_order_null_credit_card(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.correct_name()
        place_order.correct_country()
        time.sleep(2)
        place_order.correct_city()
        time.sleep(2)
        place_order.null_credit_card()
        time.sleep(2)
        place_order.correct_month()
        time.sleep(2)
        place_order.correct_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out Creditcard" in alert

    @allure.description('Test place order null name and credit card')
    @pytest.mark.sanity
    def test_place_order_null_name_and_credit(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.null_name()
        place_order.correct_country()
        time.sleep(2)
        place_order.correct_city()
        time.sleep(2)
        place_order.null_credit_card()
        time.sleep(2)
        place_order.correct_month()
        time.sleep(2)
        place_order.correct_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out Name and Creditcard." in alert

    @allure.description('Test place order INCORRECT name and credit card')
    @pytest.mark.sanity
    def test_place_order_incorrect_name_and_credit(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.incorrect_name()
        place_order.correct_country()
        time.sleep(2)
        place_order.correct_city()
        time.sleep(2)
        place_order.incorrect_credit_card()
        time.sleep(2)
        place_order.correct_month()
        time.sleep(2)
        place_order.correct_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out Name and Creditcard." in alert

    @allure.description('Test place order null country and city')
    @pytest.mark.sanity
    def test_place_order_null_country_and_city(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.correct_name()
        place_order.null_country()
        time.sleep(2)
        place_order.null_city()
        time.sleep(2)
        place_order.correct_credit_card()
        time.sleep(2)
        place_order.correct_month()
        time.sleep(2)
        place_order.correct_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out Country and City." in alert

    @allure.description('Test place order incorrect country and city')
    @pytest.mark.sanity
    def test_place_order_incorrect_country_and_city(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.correct_name()
        place_order.incorrect_country()
        time.sleep(2)
        place_order.incorrect_city()
        time.sleep(2)
        place_order.correct_credit_card()
        time.sleep(2)
        place_order.correct_month()
        time.sleep(2)
        place_order.correct_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out Country and City correctly." in alert

    @allure.description('Test place order null Month and Year')
    @pytest.mark.sanity
    def test_place_order_null_month_and_year(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.correct_name()
        place_order.null_country()
        time.sleep(2)
        place_order.null_city()
        time.sleep(2)
        place_order.correct_credit_card()
        time.sleep(2)
        place_order.null_month()
        time.sleep(2)
        place_order.null_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out Month and year." in alert

    @allure.description('Test place order incorrect Month and Year')
    @pytest.mark.sanity
    def test_place_order_incorrect_month_and_year(self):
        place_order = Cart_Page()
        place_order.navigate_to_web()
        place_order.click_cart_link_text()
        place_order.click_place_order_btn()
        place_order.correct_name()
        place_order.null_country()
        time.sleep(2)
        place_order.null_city()
        time.sleep(2)
        place_order.correct_credit_card()
        time.sleep(2)
        place_order.incorrect_month()
        time.sleep(2)
        place_order.incorrect_year()
        time.sleep(2)
        place_order.click_purchase_btn()
        alert = place_order.window_alert_text
        assert "Please fill out Month and Year Correctly." in alert
