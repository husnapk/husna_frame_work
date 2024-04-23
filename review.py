from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator
from time import sleep


class Review(HomePage):

    locator = read_locator("review")

    def click_jewelry(self):
        wrapper =Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_jewelry"])
    def click_filter_by_price(self):
        wrapper =Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_0.0-0.5_filter"])

    def click_black_white_diamond_heart(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_b_w_diamond_heart"])

    def click_rieview(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locator["lnk_add_review"])

    def adding_details_in_review(self,option1,option2):
        wrapper = Wrapper(self.driver)
        wrapper.send_element(self.locator["txf_review_title"],value=option1)
        wrapper.send_element(self.locator["txf_review_text"], value=option2)
        wrapper.click_element(self.locator["btn_rating"])
        wrapper.click_element(self.locator["btn_submit"])



    #assertions

    def is_jewelry_page_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div/h1[text()='Jewelry']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_product_displayed_within_the_range(self):
        all_elements = self.driver.find_elements("xpath","//div[@class='product-grid']")
        for  element in all_elements:
            x=element.text
            print(x)
            if "100.00" and "130.00" and "360.00" in  element.text:
                return True

    def is_black_white_diamond_heart_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//h1[@itemprop='name']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False

    def is_Product_review_page_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div[@class='page-title']")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False


    def is_Product_review_messege_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div[contains(text(),'Product review is successfully added')]")
                return element.is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False