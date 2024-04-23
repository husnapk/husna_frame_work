from pytest import mark

from lib.lib import read_headers, read_data

headers=read_headers("smoke","test_search_and_compare")
data = read_data("smoke","test_search_and_compare")



@mark.parametrize(headers,data)
def test_serach_and_compare_secenario(_driver,pages,email,password):
    pages.searchandcompare.click_login()
    assert pages.loginpage.is_loginpage_displayed() == True
    pages.loginpage.login(email, password)
    assert pages.loginpage.is_user_loggedin(email) == True
    pages.searchandcompare.mouse_hower_electronics()
    assert pages.searchandcompare.is_camerapage_displayed()==True
    pages.searchandcompare.click_handy_camcorder()
    assert pages.searchandcompare.is_handycam_dispalyed()==True
    pages.searchandcompare.click_add_compare_list()
    assert pages.searchandcompare.is_comparedtext_displayed()==True
    pages.searchandcompare.click_back()
    pages.searchandcompare.click_back()
    assert pages.searchandcompare.is_camerapage_displayed()==True
    pages.searchandcompare.click_camcoder()
    assert pages.searchandcompare.is_camcoder_dispalyed()==True
    pages.searchandcompare.click_add_compare_list()
    assert pages.searchandcompare.is_comparedtext_displayed() == True
    pages.searchandcompare.click_remove()
    pages.searchandcompare.click_remove()
    assert pages.searchandcompare.is_no_item_compare_text_displayed()==True
    pages.loginpage.click_logout()