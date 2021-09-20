import inspect
import logging
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        """Recycle method to provided log input on the test cases execution"""
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('utilities\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_link_present(self, text):
        """Explicit wait recycle method to wait until the link that matches the text is available"""
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def verify_elements_present(self,locator):
        """Explicit wait recycle method to wait until all the elements are available on the page"""
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_all_elements_located(locator))

    def verify_element_present(self,locator):
        """Explicit wait recycle method to wait until the elements are available on the page"""
        WebDriverWait(self.driver, 5).until(
            expected_conditions.presence_of_element_located(locator))

    def generate_email(self, fullname):
        """Return fullname string into email formatted string"""
        return fullname.replace(" ", ".").lower()+"@fake.com"
