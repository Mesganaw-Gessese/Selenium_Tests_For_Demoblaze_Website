import pytest
import allure
from _pytest import mark
import time
from WEB.Pages.login_page import *

class Test_Login:

    @allure.description("Test login link text clickable")
    @pytest.mark.sanity
    def test_login_link_text(self):
        login = Login_Page()
        login.navigate_to_web()
        login.click_login_link_text()

    @allure.description("Test login close button clickable")
    @pytest.mark.sanity
    def test_login_close_btn(self):
        login = Login_Page()
        login.navigate_to_web()
        login.click_login_link_text()
        login.click_login_close_btn()

    @allure.description("Test login correctly")
    @pytest.mark.sanity
    def test_login_correctly(self):
        login = Login_Page()
        login.navigate_to_web()
        login.click_login_link_text()
        login.user_name_field("mesganaw")
        login.password_field("12345")
        login.click_login_btn()

    @allure.description("Test logout link text works correctly")
    @pytest.mark.sanity
    def test_logout_link_text(self):
        login = Login_Page()
        login.navigate_to_web()
        login.click_login_link_text()
        login.user_name_field("mesganaw")
        login.password_field("12345")
        login.click_login_btn()
        login.click_logout_link_text()

    @allure.description("Test login null")
    @pytest.mark.sanity
    def test_login_null(self):
        sign_up = Login_Page()
        sign_up.navigate_to_web()
        sign_up.click_login_link_text()
        sign_up.user_name_field("")
        sign_up.password_field("")
        sign_up.click_login_btn()
        text = sign_up.window_alert_text
        assert "Please fill out Username and Password." in text
        sign_up.window_alert_accept()
        sign_up.click_login_close_btn()

    @allure.description("Test login user name null")
    @pytest.mark.sanity
    def test_login_null_user_name(self):
        sign_up = Login_Page()
        sign_up.navigate_to_web()
        sign_up.click_login_link_text()
        sign_up.user_name_field("")
        sign_up.password_field("what_about_you")
        sign_up.click_login_btn()
        text = sign_up.window_alert_text
        assert "User does not exist." in text
        sign_up.window_alert_accept()
        sign_up.click_login_close_btn()

    @allure.description("Test login user name incorrect")
    @pytest.mark.sanity
    def test_login_incorrect_user_name(self):
        sign_up = Login_Page()
        sign_up.navigate_to_web()
        sign_up.click_login_link_text()
        sign_up.user_name_field("abebe")
        sign_up.password_field("12345")
        sign_up.click_login_btn()
        text = sign_up.window_alert_text
        assert "User does not exist." in text
        sign_up.window_alert_accept()
        sign_up.click_login_close_btn()

    @allure.description("Test login user password null")
    @pytest.mark.sanity
    def test_sign_up_null_password(self):
        sign_up = Login_Page()
        sign_up.navigate_to_web()
        sign_up.click_login_link_text()
        sign_up.user_name_field("mesganaw")
        sign_up.password_field("")
        sign_up.click_login_btn()
        text = sign_up.window_alert_text
        assert "User does not exist." in text
        sign_up.window_alert_accept()
        sign_up.click_login_close_btn()

    @allure.description("Test login user password incorrect")
    @pytest.mark.sanity
    def test_sign_up_incorrect_password(self):
        sign_up = Login_Page()
        sign_up.navigate_to_web()
        sign_up.click_login_link_text()
        sign_up.user_name_field("mesganaw")
        sign_up.password_field("00000")
        sign_up.click_login_btn()
        text = sign_up.window_alert_text
        assert "User does not exist." in text
        sign_up.window_alert_accept()
        sign_up.click_login_close_btn()

    @allure.description("Test login non existing user")
    @pytest.mark.sanity
    def test_login_incorrect(self):
        sign_up = Login_Page()
        sign_up.navigate_to_web()
        sign_up.click_login_link_text()
        sign_up.user_name_field("mesggnn")
        sign_up.password_field("000")
        sign_up.click_login_btn()
        text = sign_up.window_alert_text
        assert "Please fill out Password." in text
        sign_up.window_alert_accept()
        sign_up.click_login_close_btn()
