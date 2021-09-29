# Прокрутка страницы методом execute_script
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math


try:
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    element1 = browser.find_element(By.ID, "input_value")
    x = int(element1.text)

    answer = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    browser.execute_script("return arguments[0].scrollIntoView(true);", input_answer)
    input_answer.send_keys(answer)

    checkbox_robot = browser.find_element_by_id('robotCheckbox')
    checkbox_robot.click()

    radio_robot = browser.find_element_by_css_selector("[value='robots']")
    radio_robot.click()

    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()

