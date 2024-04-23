from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator


class ShoppingCart(HomePage):
    locator =read_locator("shoppingcart")
    def user_click_on_book(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_book"])

    def user_click_on_addtocart_below_computing_and_internet_book(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["btn_add_to_cart"])

    def click_on_shopping_cart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_shopping_cart"])







    #assertion==============================================================================

    def is_book_page_isdisplayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div/h1[text()='Books']")
                return element.is_displayed()

            except NoSuchElementException:
                sleep(1)
                continue
        return False


    def conformation_message_isdisplayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//p[@class='content']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_item_displayed_in_addtocart_page(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//td[@class='product']/a[text()='Computing and Internet']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False
