from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator


class Search(HomePage):
    locator=read_locator("search")

    def signup_newsletter(self,email):
        wrapper =Wrapper(self.driver)
        wrapper.send_element(self.locator["txt_newsletter"],value=email)
        wrapper.click_element(self.locator["btn_subscribe"])


    def search_product_in_searchbox(self,name):
        wrapper = Wrapper(self.driver)
        wrapper.send_element(self.locator["txt_search"], value=name)
        wrapper.click_element(self.locator["btn_search"])


    def is_computer_page(self):
        all_Computer_Products = self.driver.find_elements("xpath","//div//h2[@class='product-title']")
        for item in all_Computer_Products:
            if "computer" in item.text:
                return  True
            else:
                return False

    def is_newsletter_message(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div[contains(text(),'Thank you for signing up! ')]")
                element.is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
            continue
        return False
