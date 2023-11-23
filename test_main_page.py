import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    #@pytest.fixture(scope="function", autouse=True)
    #def setup(self):
        #self.product = ProductFactory(title = "Best book created by robot")
        # создаем по апи
        #self.link = self.product.link
        #yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали 
        #self.product.delete()
        
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
        page.open()                      # открываем страницу
        page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
    
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

#def test_should_be_login_url(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #page = LoginPage(browser, link)
    #page.open()
    #page.should_be_login_url()

#def test_should_be_login_form(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #page = LoginPage(browser, link)
    #page.open()
    #page.should_be_login_form()
    
#def test_should_be_register_form(browser):
    #link = "http://selenium1py.pythonanywhere.com/"
    #page = LoginPage(browser, link)
    #page.open()
    #page.should_be_register_form()

#def test_guest_should_see_login_link_on_product_page(browser):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    #page = ProductPage(browser, link)
    #page.open()
    #page.should_be_login_link()
#testops
