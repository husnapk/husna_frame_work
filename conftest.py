from selenium import webdriver
from pytest import fixture

from pom.advancedsearch import AdvancedSearch
from pom.homepage import HomePage
from pom.loginpage import LoginPage
from pom.registrationpage import RegistrationPage
from pom.search import Search
from pom.search_and_compare import SearchAndCompare
from pom.shoppingcart import ShoppingCart
from pom.shoppingcartcondition import ShoppingCartCondition
from pom.wishlist import WishList
from pom.review import Review
from pom.emailafriend import EmailAFriend

@fixture
def _driver():
    driver = webdriver.Chrome()
    driver.get("https://demowebshop.tricentis.com/")
    driver.maximize_window()
    yield driver



@fixture
def pages(_driver):
    class Pages:
        homepage=HomePage(_driver)
        loginpage=LoginPage(_driver)
        registrationpage = RegistrationPage(_driver)
        search = Search(_driver)
        searchandcompare =SearchAndCompare(_driver)
        advancesearch = AdvancedSearch(_driver)
        shoppingcart= ShoppingCart(_driver)
        shoppingcartcondition = ShoppingCartCondition(_driver)
        wishlist = WishList(_driver)
        review = Review(_driver)
        emailafriend=EmailAFriend(_driver)
    return Pages()


