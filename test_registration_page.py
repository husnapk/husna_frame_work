from lib.lib import Wrapper, read_headers, read_data

from pytest import mark
headers=read_headers("smoke","test_registration")
data=read_data("smoke","test_registration")

@mark.parametrize(headers,data)

def test_registration(_driver,pages,gender,fname,lname,email,password,confirmpassword):
    pages.registrationpage.click_register()
    assert pages.registrationpage.is_registrationpage_displayed()==True
    pages.registrationpage.register(gender,fname,lname,email,password,confirmpassword)
    assert pages.registrationpage.is_user_rigisterd()==True
    pages.registrationpage.register_continue()
    assert pages.loginpage.is_user_loggedin(email) == True

