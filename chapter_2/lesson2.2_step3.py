# Работа с выпадающими списками

import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

link ='http://suninjuly.github.io/selects1.html'

browser = webdriver.Chrome()
browser.get(link)

try:
    # ищем элемент первого слагаемого на странице и определяем его значение
    number1 = browser.find_element_by_id("num1")
    x = int(number1.text)

    # ищем элемент второго слагаемого на странице и определяем его значение
    number2 = browser.find_element_by_id("num2")
    y = int(number2.text)

    # считаем сумму двух слагаемых
    answer = str(x + y)

    # открываем выпадвющий список, используя специальный класс Select из библиотеки WebDriver

    # нициализируем новый объект, передав в него WebElement с тегом select
    select = Select(browser.find_element_by_tag_name("select"))

    # находим нужный вариант из списка по значению value c html страницы
    select.select_by_value(answer)

    # Можно использовать еще два метода: select.select_by_visible_text("text") и select.select_by_index(index).
    # Первый способ ищет элемент по видимому тексту
    # Второй способ ищет элемент по его индексу или порядковому номеру. Индексация начинается с нуля.

    # находим элемент кнопки и нажимаем ее
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

