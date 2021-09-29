# Поиск элемента по тексту в ссылке

from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/find_link_text'
try:
    browser = webdriver.Chrome()
    browser.get(link)

#  найдем ссылку с текстом. Текст ссылки, который нужно найти, зашифрован формулой:
    link_txt = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    time.sleep(5)
    link_txt.click()


# перешли на форму регистрации, заполняем форму
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys('Ivan')

    input2 = browser.find_element_by_name('last_name')
    input2.send_keys('Petrov')

    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys('Smolensk')

    input4 = browser.find_element_by_id('country')
    input4.send_keys('Russia')

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

