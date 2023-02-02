import pytest
import allure
from _pytest import mark
import time

from WEB.Pages.contact_us_page import *

class Test_Contact_Us:

    @allure.description('Test contact us clickable')
    @pytest.mark.sanity
    def test_contact_us_clickable(self):
        contact = Contact_Us_Page()
        contact.navigate_to_web()
        contact.click_contact_us_link_text()

    @allure.description('Test new message correctly')
    @pytest.mark.sanity
    def test_new_message_correctly(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.insert_correct_email()
        new_message.insert_correct_name()
        new_message.type_message()
        new_message.click_send_button()

    @allure.description('Test new message null')
    @pytest.mark.sanity
    def test_new_message_null(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.null_contact_email()
        new_message.null_contact_name()
        new_message.null_message()
        new_message.click_send_button()

    @allure.description('Test new message incorrectly')
    @pytest.mark.sanity
    def test_new_message_null(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.insert_incorrect_email()
        new_message.incorrect_contact_name()
        new_message.null_message()
        new_message.click_send_button()

    @allure.description('Test new message contact email incorrectly')
    @pytest.mark.sanity
    def test_new_message_email_incorrectly(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.insert_incorrect_email()
        new_message.insert_correct_name()
        new_message.type_message()
        new_message.click_send_button()

    @allure.description('Test new message contact name null')
    @pytest.mark.sanity
    def test_null_name(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.insert_correct_email()
        new_message.null_contact_name()
        new_message.type_message()
        new_message.click_send_button()

    @allure.description('Test new message close button works')
    @pytest.mark.sanity
    def test_close_button(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.insert_correct_email()
        new_message.null_contact_name()
        new_message.type_message()
        new_message.click_close_button()

    @allure.description('Test new message contact name $ message null')
    @pytest.mark.sanity
    def test_name_and_message_null(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.insert_correct_email()
        new_message.null_contact_name()
        new_message.null_message()
        new_message.click_send_button()

    @allure.description('Test new message contact name $ email null')
    @pytest.mark.sanity
    def test_name_and_email_null(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.null_contact_email()
        new_message.null_contact_name()
        new_message.type_message()
        new_message.click_send_button()

    @allure.description('Test new message contact name $ email incorrect')
    @pytest.mark.sanity
    def test_name_and_email_null(self):
        new_message = Contact_Us_Page()
        new_message.navigate_to_web()
        new_message.click_contact_us_link_text()
        new_message.insert_incorrect_email()
        new_message.incorrect_contact_name()
        new_message.type_message()
        new_message.click_send_button()

