# Загрузка файла
from selenium import webdriver
import os
import time

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # заполняем обязательные поля формы регистрации
    first_name = browser.find_element_by_name('firstname')
    first_name.send_keys('Natalya')

    last_name = browser.find_element_by_name('lastname')
    last_name.send_keys('Romashova')

    email = browser.find_element_by_name('email')
    email.send_keys('906@mail.ru')

    # получаем путь к директории текущего исполняемого скрипта lesson2.2_step8.py
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # имя файла, который будем загружать на сайт
    file_name = "zagruzka.txt"

    # получаем путь к file_example.txt
    file_path = os.path.join(current_dir, file_name)

    # находим элемент (поле выбора файла)
    file = browser.find_element_by_css_selector('[type="file"]')

    # отправляем файл
    file.send_keys(file_path)

    # нажимаем на кнопку Submit.
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    # не забываем оставить пустую строку в конце файла

