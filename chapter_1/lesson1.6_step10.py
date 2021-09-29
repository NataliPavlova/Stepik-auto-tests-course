# Проверка регистрации при заполнении только обязательных полей. Конструкция assert.

from selenium import webdriver
import time

link = 'http://suninjuly.github.io/registration1.html'
# link = 'http://suninjuly.github.io/registration2.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # заполнем форму
    first_name = browser.find_element_by_css_selector('div.first_block input.first')
    first_name.send_keys('Мой ответ')

    last_name = browser.find_element_by_css_selector('div.first_block input.second')
    last_name.send_keys('Мой ответ')

    email = browser.find_element_by_css_selector('div.first_block input.third')
    email.send_keys('Мой ответ')

    time.sleep(5)

    #  отправляем заполенную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

