import pytest
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testData.HomePageData import HomePageData

class TestCaseOne(BaseClass):
    def test_shop_flow(self,get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        self.driver.implicitly_wait(4)
        resultpage = homepage.perform_a_search(get_data["Search"])
        log.info(f'The keywords use on the search was {get_data["Search"]}')
        log.info(f'This search result were: {resultpage.search_validation()}')
    @pytest.fixture(params=HomePageData.expected_data)
    def get_data(self,request):
        return request.param










