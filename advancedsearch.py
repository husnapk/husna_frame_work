from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator


class AdvancedSearch(HomePage):
    loc=read_locator("search_advanced")
    def search_in_customer_service(self):
        wrapper = Wrapper(self.driver)
        wrapper.mouse_action(self.loc["lnk_in_cust_search"])

    def search_product_in_advanced_search(self,name):
        wrapper = Wrapper(self.driver)
        wrapper.send_element(self.loc["txt_search_keyword"],value=name)
        wrapper.click_element(self.loc["checkbox_ad_search"])
    def dropdown_computer(self,option1):
        wrapper = Wrapper(self.driver)
        wrapper.dropdown_select(self.loc["list_catogory_list"],value=option1)
        wrapper.click_element(self.loc["btn_search"])
    def dropdown_apparel_and_shoes(self,option2):
        wrapper = Wrapper(self.driver)
        wrapper.dropdown_select(self.loc["list_catogory_list"], value=option2)
        wrapper.click_element(self.loc["btn_search"])

    def is_search_page_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div/h1[text()='Search']")
                element.is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
            continue
        return False

    def is_all_field_is_displayed(self):
        element=self.driver.find_elements("xpath","//div[@class='inputs']")
        for item in element:
            if "Manufacturer"or"Category"or"Price range" in item.text:
                continue
        return True

    def no_product_messege_isdisplayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//strong[@class='result']")
                element.is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
            continue
        return False

    def is_runnig_shoe_isdisplayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//h2[@class='product-title']")
                element.is_displayed()
                return True
            except NoSuchElementException:
                sleep(1)
            continue
        return False




