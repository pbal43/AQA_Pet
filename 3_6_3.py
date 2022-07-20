import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

answer = math.log(int(time.time()))
links = ['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
        ]
pieces = []


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('link', links)
class TestUFO():
    def test_messages(self, browser, link):
        browser.get(link)
        WebDriverWait(browser, 15).until(
            EC.visibility_of((By.ID, "ember92"))
        )
        inputik = browser.find_element(By.ID, 'ember92')
        inputik.send_keys(answer)
        buttonchik = browser.find_element(By.CSS_SELECTOR, 'button.btn')
        buttonchik.click()
        WebDriverWait(browser, 10).until(
            EC.visibility_of((By.CSS_SELECTOR, "#ember209 .smart-hints__hint"))
        )
        feedback = browser.find_element(By.CSS_SELECTOR, '#ember209 .smart-hints__hint')
        parsed_feedback = feedback.text
        pieces.append(parsed_feedback)
        assert parsed_feedback == 'Correct!', f'There is no right message here {link}'
