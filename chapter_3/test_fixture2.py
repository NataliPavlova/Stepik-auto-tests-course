# Фикстуры, возвращающие значение: @pytest.fixture
# Открытие браузера перед выполнением каждого теста. Вызываем фикстуру, ередав ее как параметр (в тест)
# Запуск тестов: pytest -s -v test_fixture2.py (- v, в отчёт со списком тестов и статусом их прохождения)

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

# создадим фикстуру browser, которая будет создавать объект WebDriver
@pytest.fixture
def int_browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, int_browser):
        int_browser.get(link)
        int_browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, int_browser):
        int_browser.get(link)
        int_browser.find_element_by_css_selector(".basket-mini .btn-group > a")

