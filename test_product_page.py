from selenium.common.exceptions import NoAlertPresentException
import pytest
import math
#from .pages.base_page import BasePage
from .pages.product_page import ProductPage

class TestProductPage():
    
    def test_guest_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)   
        page.open()                     
        page.add_product_to_basket()

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print("это значение answer -", answer)
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    #def get_code(self):
        #page.solve_quiz_and_get_code()

    #def test_guest_can_see_product_in_basket(self, browser):
