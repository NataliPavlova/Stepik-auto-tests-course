# Метод get_attribute

from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link ="http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # считываем значение для переменной х: находим элемент на странице с переменной х
    # aтрибут text возвращает текст, который находится между открывающим и закрывающим тегами элемента
    # (это и есть наш х)
    x_element = browser.find_element_by_id('treasure')
    # x = x_element.text

    x = x_element.get_attribute("valuex")
    print(x)

    # считаем математическую функцию от x (def (calc(x)))
    y = calc(x)

    # вводим ответ в текстовое поле
    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    # отмечаем checkbox "I'm the robot".
    checkbox_robot = browser.find_element_by_id('robotCheckbox')
    checkbox_robot.click()

    # выбираем radiobutton "Robots rule!".
    radio_robot = browser.find_element_by_css_selector("[value='robots']")
    radio_robot.click()

    # нажимаем на кнопку Submit.
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
    # не забываем оставить пустую строку в конце файла


