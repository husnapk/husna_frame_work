from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from xlrd import open_workbook

def wait(func):
    def _wrapper(*args,**kwargs):
        self = args[0]  # 'self' is just a name ican give anything like Wrapper class in constructor self passing
        _locator=args[1]
        w= WebDriverWait(self.driver,20)
        w.until(visibility_of_element_located(_locator))
        return func(*args,**kwargs)
    return _wrapper


class Wrapper:

    def __init__(self,driver):
        self.driver=driver
    @wait
    def click_element(self,locator):
        self.driver.find_element(*locator).click()
    @wait
    def send_element(self,locator,*,value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @wait
    def mouse_action(self,locator):
        action=ActionChains(self.driver)
        element = self.driver.find_element(*locator)
        action.move_to_element(element).perform()

    @wait
    def dropdown_select(self,locator,*,value):
        element = self.driver.find_element(*locator)
        select = Select(element)
        select.select_by_visible_text(value)



    # ======================reading locators from the exel file====================================

def read_locator(sheetname):
    workbook   = open_workbook(r"C:\Users\jasma\Desktop\objects.xls")
    excelsheet = workbook.sheet_by_name(sheetname)
    used_rows = excelsheet.nrows
    data={}
    for i in range(1,used_rows):
        temp_data = excelsheet.row_values(i)
        data[temp_data[0]]=(temp_data[1],temp_data[2]) # adding data to dictionary
    return data

# ====================================reading the data from Excel sheet========================================================

def read_headers(sheetname,scriptname):
    workbook=open_workbook(r"C:\Users\jasma\Desktop\testdata.xls")
    excelsheet = workbook.sheet_by_name(sheetname)
    used_rows=excelsheet.nrows
    for i in range(0,used_rows):
        temp_data = excelsheet.row_values(i)  # this condition not satisfied go below steps
        if temp_data[0]==scriptname:
            header = excelsheet.row_values(i-1)
            header=[item for item in header if item.strip()]  # getting output in the form of list
            return ','.join(header[2:])  # converting list to string jion method using


def read_data(sheetname,scriptname):
    workbook = open_workbook(r"C:\Users\jasma\Desktop\testdata.xls")
    excelsheet = workbook.sheet_by_name(sheetname)
    used_rows = excelsheet.nrows
    final_data=[] #list of tuples
    for i in range(0, used_rows):
        temp_data = excelsheet.row_values(i)
        if temp_data[0] == scriptname:
            data = [item for item in temp_data if item.strip()]  # getting output in the form of list
            if data[1] == "Yes":
                final_data.append(tuple(data[2:])) # converting list to tuple using typecasting
    return final_data

