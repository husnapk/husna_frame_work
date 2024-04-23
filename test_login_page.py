from lib.lib import read_headers, read_data
from pytest import mark


# 1)============creating instance of login page and calling


# def test_positive_scenario(_driver,pages,email,password):
#      login=LoginPage(_driver)
#      login.click_login()
#      login.login(_driver)


#2=====================


headers=read_headers("smoke","test_login_positive")
data=read_data("smoke","test_login_positive")

@mark.parametrize(headers,data)
def test_positive_scenario(_driver,pages,email,password):
    pages.loginpage.click_login()
    assert pages.loginpage.is_loginpage_displayed()==True
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_loggedin(email)==True