from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from .locators import BasePageLocators

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=2):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    #def go_to_login_page(self):
        #link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        #link.click()

    #def should_be_login_link(self):
        #assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        print(x)
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        # Switch to the alert
        alert.send_keys(answer)
        # Accept the alert
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
