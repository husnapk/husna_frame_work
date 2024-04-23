from time import sleep

from lib.lib import read_data, read_headers
from pytest import mark

headers=read_headers("smoke","test_advanced_search")
data=read_data("smoke","test_advanced_search")

@mark.parametrize(headers,data)
def test_advance_search_scenario(_driver,pages,email,password,name,option1,option2):
    pages.search.signup_newsletter(email)
    assert pages.search.is_newsletter_message()==True
    pages.loginpage.click_login()
    assert pages.loginpage.is_loginpage_displayed()==True
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_loggedin(email)==True
    pages.advancesearch.search_in_customer_service()
    assert pages.advancesearch.is_search_page_displayed()==True
    pages.advancesearch.search_product_in_advanced_search(name)
    assert pages.advancesearch.is_all_field_is_displayed()==True
    pages.advancesearch.dropdown_computer(option1)
    assert pages.advancesearch.no_product_messege_isdisplayed()==True
    pages.advancesearch.dropdown_apparel_and_shoes(option2)
    assert pages.advancesearch.is_runnig_shoe_isdisplayed()==True
    pages.advancesearch.click_logout()