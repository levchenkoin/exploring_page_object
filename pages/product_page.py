from .locators import ProductPageLocators
from .base_page import BasePage
from .main_page import MainPage
from selenium.webdriver.common.by import By
import time

class ProductPage(BasePage):
        
    def guest_can_add_product_to_basket(self):
        self.add_product_to_basket()
        self.product_in_basket()
        self.price_in_basket()

    def add_product_to_basket(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_product_button.click()
        time.sleep(10)

    #def product_in_basket(self):



    #def price_in_basket(self):
