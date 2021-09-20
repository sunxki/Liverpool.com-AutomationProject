import time

import pytest
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
from testData.HomePageData import HomePageData


class TestBuyingSmartTV(BaseClass):
    def test_shop_flow(self,get_data):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        self.driver.implicitly_wait(10)
        resultpage = homepage.perform_a_search(get_data["Search"])
        log.info(f'The keywords use on the search was {get_data["Search"]}')
        log.info(f'This search result were: {resultpage.search_validation()}')
        # assert (get_data["Search"] in resultpage.search_validation())
        resultpage.select_item(get_data["Brand"],get_data["Size"], get_data["Price"])
        time.sleep(2)
    @pytest.fixture(params=HomePageData.expected_smart)
    def get_data(self,request):
        return request.param