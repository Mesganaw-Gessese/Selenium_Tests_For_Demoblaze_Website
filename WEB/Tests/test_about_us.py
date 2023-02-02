import pytest
import allure
from _pytest import mark
from WEB.Pages.aboutus_page import About_Us_Page

class Test_AboutUS:

    @allure.description('test About us link text clickable')
    @pytest.mark.sanity
    def test_about_us_clickable(self):
        about_us = About_Us_Page(self)
        about_us.navigate_to_web()
        about_us.click_about_us_link_text()

    @allure.description('test About us close button clickable')
    @pytest.mark.sanity
    def test_close_btn_clickable(self):
        about_us = About_Us_Page(self)
        about_us.navigate_to_web()
        about_us.click_about_us_link_text()
        about_us.click_close_button()

    @allure.description('test about us X button clickable clickable')
    @pytest.mark.sanity
    def test_x_btn_clickable(self):
        about_us = About_Us_Page(self)
        about_us.navigate_to_web()
        about_us.click_about_us_link_text()
        about_us.click_x_button()

