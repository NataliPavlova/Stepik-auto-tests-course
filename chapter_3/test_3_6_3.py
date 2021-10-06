# Задание: параметризация тестов

import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()

links = ['https://stepik.org/lesson/236895/step/1',
         'https://stepik.org/lesson/236896/step/1',
         'https://stepik.org/lesson/236897/step/1',
         'https://stepik.org/lesson/236898/step/1',
         'https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1',
         'https://stepik.org/lesson/236904/step/1',
         'https://stepik.org/lesson/236905/step/1']

@pytest.mark.parametrize('link', links)
class TestFeedback:

    message = []

    def test_login_link(self, browser, link):
        browser.get(link)
        input_answer = browser.find_element_by_tag_name('textarea')
        answer = str(math.log(int(time.time())))
        input_answer.send_keys(answer)

        button = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
        button.click()

        feedback = browser.find_element(By.CSS_SELECTOR, "div pre.smart-hints__hint")
        feedback_text = feedback.text

        if feedback_text != "Correct!":
            TestFeedback.message.append(feedback_text)
            TestFeedback.message_new = ' '.join(TestFeedback.message)
            # print(feedback_text)
            print(TestFeedback.message_new)

        assert 'Correct!' == feedback_text, f'Инопланетяне оставили ответ {feedback_text}'














