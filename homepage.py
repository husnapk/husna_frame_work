from lib.lib import Wrapper,read_locator
class HomePage:
    locators1 = read_locator("homepage")
    def __init__(self,driver):
        self.driver=driver
    def click_login(self):
        wrapper =Wrapper(self.driver)
        wrapper.click_element(self.locators1["lnk_login"])# acces class variable self has to give locators1 is class variable
    def click_register(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locators1["lnk_register"])

    def click_logout(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locators1["lnk_logout"])













