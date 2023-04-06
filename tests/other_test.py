import time

from pages.other_page import Others

class TestOther:
    def test_catalog_data(self,driver):
        othe=Others(driver,"http://193.124.117.158/#/login")
        othe.open()
        othe.autorization()
        othe.catalog_data()
        time.sleep(3)

    def test_message(self, driver):
        othe = Others(driver, "http://193.124.117.158/#/login")
        othe.open()
        othe.autorization()
        othe.message()
        time.sleep(3)