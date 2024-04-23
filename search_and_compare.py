from time import sleep

from selenium.common import NoSuchElementException

from pom.homepage import HomePage
from lib.lib import Wrapper, read_locator


class SearchAndCompare(HomePage):
    locators = read_locator("searchandcompare")
    def mouse_hower_electronics(self):
        wrapper = Wrapper(self.driver)
        wrapper.mouse_action(self.locators["lnk_electronics"])
        wrapper.click_element(self.locators["lnk_cameraphoto"])
    def click_handy_camcorder(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locators["lnk_1MP 60GB Hard Drive Handycam Camcorder"])
    def click_add_compare_list(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locators["btn_addtocomparelist"])
    def click_back(self):
        self.driver.back()
        #self.driver.back()
    def click_camcoder(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locators["lnk_camcorder"])
        # wrapper.click_element(self.locators["btn_addtocomparelist"])
    def click_remove(self):
        wrapper = Wrapper(self.driver)
        wrapper.click_element(self.locators["btn_remove"])
        #wrapper.click_element(self.locators["btn_remove"])


    def is_camerapage_displayed(self):

        actuall_url="https://demowebshop.tricentis.com/camera-photo"
        expected_url = self.driver.current_url
        if actuall_url==expected_url:
            return True
        else:
            return False

    def is_handycam_dispalyed(self):
        actuall_url = "https://demowebshop.tricentis.com/hard-drive-handycam-camcorder"
        expected_url = self.driver.current_url
        if actuall_url == expected_url:
            return True
        else:
            return False

    def is_comparedtext_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div/h1[text()='Compare products']")
                element.is_displayed()
                return True
            except NoSuchElementException:
                sleep(2)
                continue
        return False

    def is_camcoder_dispalyed(self):
        actuall_url = "https://demowebshop.tricentis.com/camcorder"
        expected_url = self.driver.current_url
        if actuall_url == expected_url:
            return True
        else:
            return False

    def is_no_item_compare_text_displayed(self):
        for i in range(5):
            try:
                element = self.driver.find_element("xpath","//div[contains(text(),'You have no items to compare')]")
                element.is_displayed()
                return True
            except NoSuchElementException:
                sleep(2)
                continue
        return False



