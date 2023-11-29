import pytest
import math
import time
from selenium.common.exceptions import NoAlertPresentException
from .pages.base_page import BasePage
from .pages.product_page import ProductPage

class TestProductPage():
    
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)   
        page.open()                     
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(5)
        page.product_in_basket()
        page.price_in_basket()
        #review passed
