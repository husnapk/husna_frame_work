from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper,read_locator

#2)===============reading locator value from excelsheet=================================
class LoginPage(HomePage):
    locator=read_locator("loginpage")
    def login(self,email,password):
        wrapper = Wrapper(self.driver)
        wrapper.send_element(self.locator["txt_email"], value=email)
        wrapper.send_element(self.locator["txt_password"], value=password)
        wrapper.click_element(self.locator["btn_login"])


# assertiopn=======

    def is_loginpage_displayed(self):
        actual_url =("https://demowebshop.tricentis.com/login")
        expected_url = self.driver.current_url
        if actual_url==expected_url:
            return  True
        else:
            return False

    def is_user_loggedin(self,email):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath",f"//a[text()='{email}']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False





# 1) ============================== passing locator value in script itself========================================================
#class LoginPage(HomePage):
#   def login(self,email,password):
#         wrapper = Wrapper(driver)
#         wrapper.send_element(("id", "Email"), value="demoweb842@gmail.com")
#         wrapper.send_element(("id", "Password"), value="demoweb12")
#         wrapper.click_element(("xpath", "//input[@value='Log in']"))