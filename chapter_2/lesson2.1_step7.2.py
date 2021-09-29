# Метод get_attribute
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_element = browser.find_element_by_id("treasure")
    x = x_element.get_attribute("valuex")

    y = calc(x)

    input_answer = browser.find_element_by_id("answer")
    input_answer.send_keys(y)
    time.sleep(2)

    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    time.sleep(2)

    option2 = browser.find_element_by_css_selector("[type='radio'][value='robots']")
    option2.click()
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
