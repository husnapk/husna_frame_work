

from pytest import mark

from lib.lib import read_headers, read_data

headers=read_headers("smoke","test_newsletter_search")
data=read_data("smoke","test_newsletter_search")
@mark.parametrize(headers,data)
def test_search_scenario(_driver,pages,email,password,name):
    print("hello")
    pages.search.signup_newsletter(email)
    assert pages.search.is_newsletter_message()==True
    pages.loginpage.click_login()
    assert pages.loginpage.is_loginpage_displayed()==True
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_loggedin(email)==True
    pages.search.search_product_in_searchbox(name)
    assert pages.search.is_computer_page()==True



