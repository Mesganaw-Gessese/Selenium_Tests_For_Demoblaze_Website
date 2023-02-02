import pytest
import allure
from _pytest import mark

from WEB.Pages.home_page import *
class Test:
    @allure.description('test home categories phone clickable')
    @pytest.mark.sanity
    def test_phone_clickable(self):
        phone = Home_Page()
        phone.login_to_web()
        phone.click_phone_link_text()

    @allure.description('test home categories laptops clickable')
    @pytest.mark.sanity
    def test_laptop_clickable(self):
        laptop = Home_Page()
        laptop.login_to_web()
        laptop.click_laptop_link_text()

    @allure.description('test home categories monitors clickable')
    @pytest.mark.sanity
    def test_monitor_clickable(self):
        monitor = Home_Page()
        monitor.login_to_web()
        monitor.click_monitor_link_text()

    @allure.description('test home link text clickable')
    @pytest.mark.sanity
    def test_home_link_text_clickable(self):
        home = Home_Page()
        home.login_to_web()
        home.click_home_link_text()

    @allure.description('test the home page footer have about us description')
    @pytest.mark.sanity
    def test_about_us_description(self):
        description = Home_Page()
        description.login_to_web()
        description.check_about_us_description()

    @allure.description('test the home page footer have get in touch')
    @pytest.mark.sanity
    def test_get_in_touch(self):
        get_in_touch = Home_Page()
        get_in_touch.login_to_web()
        get_in_touch.check_about_us_description()

    @allure.description('test home products clickable')
    @pytest.mark.sanity
    def test_phone_products_clickable(self):
        phone = Home_Page()
        phone.login_to_web()
        phone.click_phone_link_text()
        phone.click_sonny_phone_product()

    @allure.description('test home cart button works correctly')
    @pytest.mark.sanity
    def test_phone_products_clickable(self):
        add_cart = Home_Page()
        add_cart.login_to_web()
        add_cart.click_phone_link_text()
        add_cart.click_sonny_phone_product()
        add_cart.click_add_to_cart_btn()
        alert_message = add_cart.window_alert_text
        assert "Product added" in alert_message
        add_cart.window_alert_accept()









