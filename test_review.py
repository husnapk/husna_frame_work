from pytest import mark
from lib.lib import Wrapper,read_headers,read_data




header=read_headers("smoke","test_review")
data =read_data("smoke","test_review")

@mark.parametrize(header,data)
def test_review_positive_scenarios(_driver,pages,email,password,option1,option2):
    pages.loginpage.click_login()
    assert pages.loginpage.is_loginpage_displayed() == True
    pages.loginpage.login(email, password)
    assert pages.loginpage.is_user_loggedin(email) == True
    pages.review.click_jewelry()
    assert pages.review.is_jewelry_page_displayed()==True
    pages.review.click_filter_by_price()
    assert pages.review.is_product_displayed_within_the_range()==True
    pages.review.click_black_white_diamond_heart()
    assert pages.review.is_black_white_diamond_heart_displayed()==True
    pages.review.click_rieview()
    assert pages.review.is_Product_review_page_displayed()==True
    pages.review.adding_details_in_review(option1,option2)
    assert pages.review.is_Product_review_messege_displayed()==True
    pages.homepage.click_logout()

