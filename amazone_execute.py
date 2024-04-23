from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get("https://www.amazon.com/")
sleep(10)
driver.maximize_window()
driver.find_element("id",'twotabsearchtextbox').send_keys("iphone")
driver.find_element("xpath","//input[@id='nav-search-submit-button']").click()
all_elements1 =driver.find_elements("xpath","//span[contains (text(),'iPhone')]")
#for item in all_elements:
#    print(item.text)
all_element=driver.find_elements("xpath","//span[contains (text(),'iPhone')]/../../../..//span[@class='a-price-whole']")

for item,price in zip(all_elements1,all_element):
   print(item.text,price.text)








# driver = webdriver.Chrome()
# driver.get("https://www.google.com/")
#
# driver.maximize_window()
#
# driver.switch_to.active_element.send_keys("selenium_rmg")
# #driver.find_element("xpath","//div[@class='YacQv']").send_keys("selenium_rmg")
# sleep(5)
# all_elements = driver.find_elements("xpath","//div[@role='presentation']//li")
# for item in all_elements:
#     print(item.text)