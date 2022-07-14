from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        # 1_test
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input_first_name.send_keys("Paulig")
        input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input_last_name.send_keys("coffee")
        input_Email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input_Email.send_keys("Paulig.coffee@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        browser.quit()

    def test_abs2(self):
        # 2_test
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input_first_name.send_keys("Paulig")
        input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input_last_name.send_keys("coffee")
        input_Email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input_Email.send_keys("Paulig.coffee@mail.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(2)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        browser.quit()

if __name__ == "__main__":
    unittest.main()

# python -m unittest {test}.py