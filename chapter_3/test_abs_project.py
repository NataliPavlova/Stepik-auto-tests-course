# Тесты в стиле unittest
import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):

    @classmethod
    def pepega

    def test_abs1(self):
        browser = webdriver.Chrome()
        browser.get('http://suninjuly.github.io/registration1.html')

        # заполнем форму
        first_name = browser.find_element_by_css_selector('div.first_block input.first')
        first_name.send_keys('Мой ответ')

        last_name = browser.find_element_by_css_selector('div.first_block input.second')
        last_name.send_keys('Мой ответ')

        email = browser.find_element_by_css_selector('div.first_block input.third')
        email.send_keys('Мой ответ')

        #  отправляем заполенную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        welcome_text_test = 'Congratulations! You have successfully registered!'

        # сравниваем результат ожидаемый с фактическим
        self.assertEqual(welcome_text_test, welcome_text)


    def test_abs2(self):
        browser = webdriver.Chrome()
        # в форме по ссылке нет одного поля для обызательного заполнения
        browser.get('http://suninjuly.github.io/registration2.html')

        # заполнем форму
        first_name = browser.find_element_by_css_selector('div.first_block input.first')
        first_name.send_keys('Мой ответ')

        last_name = browser.find_element_by_css_selector('div.first_block input.second')
        last_name.send_keys('Мой ответ')

        email = browser.find_element_by_css_selector('div.first_block input.third')
        email.send_keys('Мой ответ')

        #  отправляем заполенную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        welcome_text_test = 'Congratulations! You have successfully registered!'

        self.assertEqual(welcome_text_test, welcome_text)

if __name__ == "__main__":
    unittest.main()