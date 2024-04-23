from time import sleep

from lib.lib import read_headers, read_data
from pytest import mark
headers=read_headers("smoke","test_wishlist")
data=read_data("smoke","test_wishlist")
@mark.parametrize(headers,data)
def test_wishlist_scenarios(_driver,pages,email,password,option1,option2,option3,option4):
    pages.loginpage.click_login()
    assert pages.loginpage.is_loginpage_displayed() == True
    pages.loginpage.login(email, password)
    assert pages.loginpage.is_user_loggedin(email) == True
    pages.shoppingcartcondition.click_on_apprael_and_shoe()
    assert pages.shoppingcartcondition.is_apparel_and_shoes_displayed() == True
    pages.wishlist.select_four_item_from_display_dropdown(option1)
    assert pages.wishlist.is_all_item_displayed_on_page()==True
    pages.wishlist.select_eight_item_from_display_dropdown(option2)
    assert pages.wishlist.is_all_item_displayed_on_page() == True
    pages.wishlist.select_twelve_item_from_display_dropdown(option3)
    assert pages.wishlist.is_all_item_displayed_on_page() == True
    pages.wishlist.click_blue_green_sneakers()
    assert pages.wishlist.is_blue_grean_sneakers_displayed()==True
    pages.wishlist.click_add_to_wishlist()
    assert pages.wishlist.wishlist_conformation_messege()==True
    pages.wishlist.clik_wishlist()
    assert pages.wishlist.is_blue_shoes_is_displayed_in_wishlist_page()==True
    pages.wishlist.clear_qty(option4)
    assert pages.wishlist.empty_wishlist_message()==True
    pages.loginpage.click_logout()


