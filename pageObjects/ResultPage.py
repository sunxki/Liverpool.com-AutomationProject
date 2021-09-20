import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.common.exceptions import *


class ResultPage(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    result_info_text = (By.XPATH, "//h1[contains(@class,'searcherTitle-result')]")
    no_result_info_text = (By.XPATH,"//h1[contains(@class,'d-none')]")
    products_displayed = (By.XPATH,"//h5[@class='card-title a-card-description']")
    price_tag = (By.CSS_SELECTOR,"*[class='a-card-discount']")
    search_Bar = (By.XPATH, "//input[@label = 'Buscar ...']")

    def search_validation(self):
        """Return the info text with search information displayed on the Result page """
        try:
            element = self.driver.find_element(*ResultPage.result_info_text)
            if element.is_displayed():
                self.clear_field()
                return element.text
        except NoSuchElementException:
            element = self.driver.find_element(*ResultPage.no_result_info_text)
            return element.text

    def clear_field(self):
        return self.driver.find_element(*ResultPage.search_Bar).clear()

    def select_item(self,brand,size,price):
        products = self.driver.find_elements(*ResultPage.products_displayed)
        products_description= self.get_description_with_price()
        for index, element in enumerate(products_description,1):
            if brand in element and size in element and element[-1]<=price:
                products[index-1].click()

    def get_description_with_price(self):
        products_description = []
        products = self.driver.find_elements(*ResultPage.products_displayed)
        products_prices = self.get_prices()
        for item in products:
            products_description.append(item.text.split(" "))
        for index,item in enumerate(products_description):
            item.append(products_prices[index])
        return products_description

    def get_prices(self):
        products_prices = []
        prices = self.driver.find_elements(*ResultPage.price_tag)
        for items in prices:
            products_prices.append(float((items.text.replace(("$"),"")).replace(",",""))/100)
        return products_prices