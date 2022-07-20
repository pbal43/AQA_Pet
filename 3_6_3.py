import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


links = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
        ]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
class TestUFO():
    pieces = []
    def test_messages(self, browser, link):
        browser.get(link)
        WebDriverWait(browser, 15).until(
            EC.visibility_of_any_elements_located((By.TAG_NAME, 'textarea'))
        )
        inputik = browser.find_element(By.TAG_NAME, 'textarea')
        answer = math.log(int(time.time()))
        inputik.send_keys(str(answer))
        buttonchik = browser.find_element(By.CSS_SELECTOR, 'button.submit-submission')
        buttonchik.click()
        WebDriverWait(browser, 10).until(
            EC.visibility_of_any_elements_located((By.CSS_SELECTOR, '.smart-hints__hint'))
        )
        feedback = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint')
        parsed_feedback = feedback.text
        if parsed_feedback != 'Correct!':
            self.pieces.append(parsed_feedback)
        assert parsed_feedback == 'Correct!', f'There is no right message on {link}'
    print(pieces)
