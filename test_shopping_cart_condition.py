from time import sleep

from pytest import mark

from lib.lib import read_headers, read_data

headers = read_headers("smoke","test_shopping_cart_condition")
data =read_data("smoke","test_shopping_cart_condition")

@mark.parametrize(headers,data)
def test_shopping_cart_condition(_driver,pages,email,password,qty):
    pages.loginpage.click_login()
    assert pages.loginpage.is_loginpage_displayed()==True
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_loggedin(email)==True
    pages.shoppingcartcondition.click_on_apprael_and_shoe()
    assert pages.shoppingcartcondition.is_apparel_and_shoes_displayed()==True
    pages.shoppingcartcondition.click_lether_bag_cell_phone_holder()
    assert pages.shoppingcartcondition.is_conformation_messege_displayed()==True
    sleep(3)
    pages.shoppingcartcondition.click_on_shopping_cart()
    assert pages.shoppingcartcondition.is_shopping_cart_page_is_displayed()==True
    assert pages.shoppingcartcondition.is_genuin_lether_bag_is_displayed()==True
    assert pages.shoppingcartcondition.check_price_quantity_total_is_dispalyed()==True
    # pages.shoppingcartcondition.change_the_quantity(qty)
    # pages.shoppingcartcondition.click_update_shopping_cart()
    assert pages.shoppingcartcondition.updated_shopping_cart_price_quantity_total_is_dispalyed()==True
    pages.shoppingcartcondition.remove_genuine_lether_bag()
    assert pages.shoppingcartcondition.shopping_cart_empty_messege_is_displayed()==True
    pages.shoppingcartcondition.click_logout()
