import pytest
import allure
from _pytest import mark
import time
from WEB.Pages.sign_up_page import *

class Test_sign_up:

    @allure.description("Test sign up link text clickable")
    @pytest.mark.sanity
    def test_sign_up_link_text(self):
        sign_up = Sign_Up_Page()
        sign_up.navigate_to_web()
        sign_up.click_sign_up_link_text()

    @allure.description("Test sign up close button clickable")
    @pytest.mark.sanity
    def test_sign_up_close_btn(self):
        sign_up = Sign_Up_Page()
        sign_up.navigate_to_web()
        sign_up.click_sign_up_link_text()
        sign_up.click_sign_up_close_btn()

    @allure.description("Test sign up correctly")
    @pytest.mark.sanity
    def test_sign_up_correctly(self):
        sign_up = Sign_Up_Page()
        sign_up.navigate_to_web()
        sign_up.click_sign_up_link_text()
        sign_up.user_name_field("Gessese")
        sign_up.password_field("Mesge12")
        sign_up.click_sign_up_btn()
        text = sign_up.window_alert_text
        assert "Sign up successful." in text
        sign_up.window_alert_accept()
        sign_up.click_sign_up_close_btn()


    @allure.description("Test sign up existing user")
    @pytest.mark.sanity
    def test_sign_up_existing(self):
        sign_up = Sign_Up_Page()
        sign_up.navigate_to_web()
        sign_up.click_sign_up_link_text()
        sign_up.user_name_field("Gessese")
        sign_up.password_field("Mesge12")
        sign_up.click_sign_up_btn()
        text = sign_up.window_alert_text
        assert "This user already exist." in text
        sign_up.window_alert_accept()
        sign_up.click_sign_up_close_btn()

    @allure.description("Test sign up null")
    @pytest.mark.sanity
    def test_sign_up_null(self):
        sign_up = Sign_Up_Page()
        sign_up.navigate_to_web()
        sign_up.click_sign_up_link_text()
        sign_up.user_name_field("")
        sign_up.password_field("")
        sign_up.click_sign_up_btn()
        text = sign_up.window_alert_text
        assert "Please fill out Username and Password." in text
        sign_up.window_alert_accept()
        sign_up.click_sign_up_close_btn()

    @allure.description("Test sign up user name null")
    @pytest.mark.sanity
    def test_sign_up_null_user_name(self):
        sign_up = Sign_Up_Page()
        sign_up.navigate_to_web()
        sign_up.click_sign_up_link_text()
        sign_up.user_name_field("")
        sign_up.password_field("what_about_you")
        sign_up.click_sign_up_btn()
        text = sign_up.window_alert_text
        assert "Please fill out Username." in text
        sign_up.window_alert_accept()
        sign_up.click_sign_up_close_btn()

    @allure.description("Test sign up user password null")
    @pytest.mark.sanity
    def test_sign_up_null_user_password(self):
        sign_up = Sign_Up_Page()
        sign_up.navigate_to_web()
        sign_up.click_sign_up_link_text()
        sign_up.user_name_field("what_about_you")
        sign_up.password_field("")
        sign_up.click_sign_up_btn()
        text = sign_up.window_alert_text
        assert "Please fill out Password." in text
        sign_up.window_alert_accept()
        sign_up.click_sign_up_close_btn()
