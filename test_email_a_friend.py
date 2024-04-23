from pytest import mark
from lib.lib import Wrapper,read_headers,read_data

header=read_headers("smoke","test_email_a_friend")
data=read_data("smoke","test_email_a_friend")
@mark.parametrize(header,data)
def test_email_a_friend_scenarios(_driver,pages,email,password,option1,option2,message):
    pages.homepage.click_login()
    assert pages.loginpage.is_loginpage_displayed()==True
    pages.loginpage.login(email,password)
    assert pages.loginpage.is_user_loggedin(email)==True
    pages.emailafriend.select_cell_phone_from_electronics()
    assert pages.emailafriend.is_cell_phone_page_is_displayed()==True
    pages.emailafriend.click_on_smart_phone()
    assert pages.emailafriend.is_cell_phone_name_displayed()==True
    pages.emailafriend.click_on_email_a_friend()
    assert pages.emailafriend.is_email_a_friend_text_displayed()==True
    pages.emailafriend.formating_the_email(option1)
    assert pages.emailafriend.is_wrong_email_messege_is_palced()==True
    pages.emailafriend.formating_the_correct_email(option2,message)



