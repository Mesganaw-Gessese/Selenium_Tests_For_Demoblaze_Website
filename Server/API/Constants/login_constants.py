class LoginConstants:
    url = "https://api.demoblaze.com/login"

    valid_data = {"username" :"mesganaw",
                  "password" :"12345"}

    invalid_data_username = {"username": "python",
                             "password": "12345"}

    invalid_data_password = {"username": "mesganaw",
                             "password": "wangra"}

    invalid_both_data = {"username": "lalakomte",
                             "password": "bebelaw"}