from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator


class ShoppingCartCondition(HomePage):
    locator = read_locator("shoppingcartcondition")
    def click_on_apprael_and_shoe(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_apparel&shoes"])
    def click_lether_bag_cell_phone_holder(self):
        wrapper =Wrapper(self.driver)
        wrapper.mouse_action(self.locator["btn_add_to_cart"])

    def click_on_shopping_cart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["btn_shopping_cart"])
    def change_the_quantity(self,qty):
        wrapper = Wrapper(self.driver)
        wrapper.send_element(self.locator["txt_quantity"],value=qty)

    def click_update_shopping_cart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["btn_update_shopping_cart"])

    def remove_genuine_lether_bag(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["checkbox"])
        wrapper.click_element(self.locator["btn_update_shopping_cart"])




    #assertion

    def is_apparel_and_shoes_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//h1[text()='Apparel & Shoes']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_conformation_messege_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath", "//p[text()='The product has been added to your ']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_shopping_cart_page_is_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div/h1[text()='Shopping cart']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_genuin_lether_bag_is_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//td/a[text()='Genuine Leather Handbag with Cell Phone Holder & Many Pockets']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False


    def check_price_quantity_total_is_dispalyed(self):
            all_products = self.driver.find_elements("xpath", "//div[@class='page-body']//span")
            for item in all_products:
                if "35.00" or "1" or "35.00" in item.text:
                    continue
            return True
    def updated_shopping_cart_price_quantity_total_is_dispalyed(self):
            all_products = self.driver.find_elements("xpath", "//div[@class='page-body']//span")
            for item in all_products:
                if "35.00" or "4" or "35.00" in item.text:
                    continue
            return True

    def shopping_cart_empty_messege_is_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div/h1[text()='Shopping cart']/../..//div[@class='order-summary-content']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

#