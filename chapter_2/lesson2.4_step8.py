# Настройка ожиданий
# Ждем нужный текст на странице

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    # Ожидание проверки, присутствует ли данный текст в указанном элементе. В нашем случае это $100
    price = WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

    # Как только дождались нужной цены, нажимае на кнопку "Book"
    button = browser.find_element(By.ID, 'book')
    button.click()

    # решаем математическую задачку
    element_x = browser.find_element(By.ID, "input_value")
    answer = element_x.text
    # считаем значение функции, чтобы ввести его в поле ответа
    input_answer = calc(answer)

    #  находим поле для ввода ответа и вводим ответ
    element_answer = browser.find_element(By.ID, "answer")
    element_answer.send_keys(input_answer)

    button_end = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_end.click()

finally:
    time.sleep(5)
    browser.quit()

