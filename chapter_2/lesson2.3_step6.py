# Переход на новую вкладку браузера
# Команда switch_to.window

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)

    # нажимаем на кнопку "I want to go on a magical journey!"
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    time.sleep(2)

    # формируем массив имен всех вкладок
    spisok = browser.window_handles

    # выбираем нудную нам вкладку (вторую, в списке с индексом 1)
    new_window = browser.window_handles[1]
    # переходим на вкладку
    browser.switch_to.window(new_window)

    # считываем значение Х
    element_x = browser.find_element(By.ID, "input_value")
    answer = element_x.text
    # считаем значение функции, чтобы ввести его в поле ответа
    input_answer = calc(answer)

    #  находим поле для ввода ответа и вводим ответ
    element_answer = browser.find_element(By.ID, "answer")
    element_answer.send_keys(input_answer)

    # нажимаем кнопку "Submit"
    button_end = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_end.click()

finally:
    time.sleep(5)
    browser.quit()

