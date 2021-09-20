from selenium.webdriver.common.by import By
from pageObjects.ResultPage import ResultPage



class HomePage:

    search_Bar = (By.XPATH, "//input[@label = 'Buscar ...']")
    search_button = (By.CSS_SELECTOR, "button[class='input-group-text']")

    def __init__(self , driver):
        self.driver = driver

    def perform_a_search(self,search):
        """Create the object of the instance from the Resultpage class once the search bar was used"""
        self.driver.find_element(*HomePage.search_Bar).send_keys(search)
        self.driver.find_element(*HomePage.search_button).click()
        resultpage = ResultPage(self.driver)
        return resultpage