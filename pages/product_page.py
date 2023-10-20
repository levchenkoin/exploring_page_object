from .locators import ProductPageLocators
from .locators import BasketCheckLocators
from .base_page import BasePage
from .main_page import MainPage

class ProductPage(BasePage):
        
    def guest_can_add_product_to_basket(self):
        self.add_product_to_basket()
        self.product_in_basket()
        self.price_in_basket()

    def add_product_to_basket(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_product_button.click()

    def product_in_basket(self):
        check_name_in_basket = self.browser.find_element(*BasketCheckLocators.NAME_IN_BASKET)
        print (check_name_in_basket)
        assert self.is_element_present(*BasketCheckLocators.PRODUCT_NAME), "Incorrect product in basket"
        #check_product_name = self.browser.find_element(*BasketCheckLocators.PRODUCT_NAME)


    def price_in_basket(self):
        check_basket_price = self.browser.find_element(*BasketCheckLocators.BASKET_PRICE)
        print (check_basket_price)
        assert self.is_element_present(*BasketCheckLocators.PRODUCT_PRICE), "Incorrect price in basket"
        #check_product_price = self.browser.find_element(*BasketCheckLocators.PRODUCT_PRICE)
