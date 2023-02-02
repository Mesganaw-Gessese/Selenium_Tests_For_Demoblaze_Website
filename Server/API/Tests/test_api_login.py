from Server.API.Constants.login_constants import *
import requests
import allure


class TestLogin_API:
    @allure.description('Login correctly')
    def test_login_correctly(self):
        url = LoginConstants.url
        data = LoginConstants.valid_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 200
        assert res.elapsed.total_seconds() < 5
 

    @allure.description('Login incorrectly with both invalid')
    def test_login_incorrectly(self):
        url = LoginConstants.url
        data = LoginConstants.invalid_both_data
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('Login incorrectly with invalid username')
    def test_login_incorrectly(self):
        url = LoginConstants.url
        data = LoginConstants.invalid_data_username
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5


    @allure.description('Login incorrectly with invalid password')
    def test_login_incorrectly(self):
        url = LoginConstants.url
        data = LoginConstants.invalid_data_password
        res = requests.post(url, json=data)
        res_data = res.json()
        assert res.status_code == 400
        assert res.elapsed.total_seconds() < 5
