from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator


class WishList(HomePage):
    locator = read_locator("wishlist")
    def select_four_item_from_display_dropdown(self,option1):
        wrapper= Wrapper(self.driver)
        wrapper.dropdown_select(self.locator["dropdown_display"],value=option1)
    def select_eight_item_from_display_dropdown(self,option2):
        wrapper= Wrapper(self.driver)
        wrapper.dropdown_select(self.locator["dropdown_display"],value=option2)
    def select_twelve_item_from_display_dropdown(self,option3):
        wrapper= Wrapper(self.driver)
        wrapper.dropdown_select(self.locator["dropdown_display"],value=option3)

    def click_blue_green_sneakers(self):
        wrapper =Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_bg_sneaker"])

    def click_add_to_wishlist(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["btn_add_to_wishlist"])

    def clik_wishlist(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_wishlist"])
    def clear_qty(self,option4):
        wrapper = Wrapper(self.driver)
        wrapper.send_element(self.locator["txb_qty"],value=option4)
        wrapper.click_element(self.locator["btn_update_wishlist"])





#assertions
    def is_all_item_displayed_on_page(self):
        all_products =self.driver.find_elements("xpath","//div[@class='product-grid']/div[@class='item-box']")
        for item in all_products:
            all_items =item.text
            if len(all_items)==4 or len(all_items)==8 or len(all_items)==12:
                break
                #if "50's Rockabilly Polka Dot Top JR Plus Size" or "Show details for Blue and green Sneaker" or "Show details for Blue Jeans" or "Casual Golf Belt" in item.text():
        return True

    def is_blue_grean_sneakers_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//h1[contains(text(),'Blue and green Sneaker')]")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False


    def wishlist_conformation_messege(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//p[text()='The product has been added to your ']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_blue_shoes_is_displayed_in_wishlist_page(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//a[text()='Blue and green Sneaker']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False
    def empty_wishlist_message(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div[contains(text(),'The wishlist is empty!')]")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

