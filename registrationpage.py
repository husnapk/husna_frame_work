from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator


class RegistrationPage(HomePage):
    locator=read_locator("registrationpage")
    def register(self,gender,fname,lname,email,password,confirmpassword):
        wrapper=Wrapper(self.driver)
        if gender == "female":
            wrapper.click_element(self.locator["rdo_female"])
        else:
            wrapper.click_element(self.locator["rdo_male"])
            wrapper.send_element(self.locator["txt_fname"],value=fname)
            wrapper.send_element(self.locator["txt_lname"],value=lname)
            wrapper.send_element(self.locator["txt_email"],value=email)
            wrapper.send_element(self.locator["txt_password"],value=password)
            wrapper.send_element(self.locator["txt_confirmpassword"],value=confirmpassword)
            wrapper.click_element(self.locator["btn_register"])

    def register_continue(self):
        wrapper=Wrapper(self.driver)
        wrapper.click_element(self.locator["btn_continue"])

    def is_user_rigisterd(self):
        for i in range(5):
            try:
                element=self.driver.find_element("xpath","//div[@class='result']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_registrationpage_displayed(self):
        actual_url =("https://demowebshop.tricentis.com/register"
                     "")
        expected_url = self.driver.current_url
        if actual_url==expected_url:
            return  True
        else:
            return False