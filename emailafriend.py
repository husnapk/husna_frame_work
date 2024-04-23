from pom.homepage import HomePage
from lib.lib import Wrapper,read_locator
class EmailAFriend(HomePage):
    locator =read_locator("emailafriend")

    def select_cell_phone_from_electronics(self):
        wrapper = Wrapper(self.driver)
        wrapper.mouse_action(self.locator["lnk_electronics"])
        wrapper.click_element(self.locator["dropdown_cellphone"])

    def click_on_smart_phone(self):
        wrapper=Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_smartphone"])

    def click_on_email_a_friend(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["btn_email_friend"])

    def formating_the_email(self,option1):
        wrapper=Wrapper(self.driver)
        wrapper.send_element(self.locator["txt_email_friend"],value=option1)
        wrapper.click_element(self.locator["btn_send_email"])

    def formating_the_correct_email(self,option2,message):
        wrapper=Wrapper(self.driver)
        wrapper.send_element(self.locator["txb_email_second"],value=option2)
        wrapper.send_element(self.locator["txf_personal_message"],value=message)
        wrapper.click_element(self.locator["btn_send_email"])


    #assertion

    def is_cell_phone_page_is_displayed(self):
        actual_url="https://demowebshop.tricentis.com/cell-phones"
        expected_url=self.driver.current_url
        if actual_url==expected_url:
            return True
        else:
            return False


    def is_cell_phone_name_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//h1[contains(text(),'Smartphone')]")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(2)
                continue


    def is_email_a_friend_text_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//h1[text()='Email a friend']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(2)
                continue



    def is_wrong_email_messege_is_palced(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath", "//div//span[text()='Wrong email']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(2)
                continue

        #