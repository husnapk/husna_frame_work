from time import sleep

from pytest import mark

from lib.lib import read_headers, read_data

headers=read_headers("smoke","test_shopping_cart")
data=read_data("smoke","test_shopping_cart")

@mark.parametrize(headers,data)
def test_shopping_cart_scenario(_driver,pages,email,password):
    pages.loginpage.click_login()
    assert pages.loginpage.is_loginpage_displayed()==True
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_loggedin(email)==True
    pages.shoppingcart.user_click_on_book()
    assert pages.shoppingcart.is_book_page_isdisplayed()==True
    pages.shoppingcart.user_click_on_addtocart_below_computing_and_internet_book()
    assert pages.shoppingcart.conformation_message_isdisplayed()==True
    sleep(3)
    pages.shoppingcart.click_on_shopping_cart()
    assert pages.shoppingcart.is_item_displayed_in_addtocart_page()==True
    pages.loginpage.click_logout()

