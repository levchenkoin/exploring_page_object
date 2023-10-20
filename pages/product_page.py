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
        check_name_in_basket = self.browser.find_element(*BasketCheckLocators.NAME_IN_BASKET).text
        print (check_name_in_basket)
        check_product_name = self.browser.find_element(*BasketCheckLocators.PRODUCT_NAME).text
        print (check_product_name)
        assert check_name_in_basket == check_product_name, "Incorrect product in basket"        


    def price_in_basket(self):
        check_basket_price = self.browser.find_element(*BasketCheckLocators.BASKET_PRICE).text
        print (check_basket_price)
        check_product_price = self.browser.find_element(*BasketCheckLocators.PRODUCT_PRICE).text
        print (check_product_price)
        assert check_basket_price == check_product_price, "Incorrect price in basket"
        
