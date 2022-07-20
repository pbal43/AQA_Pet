from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


def test_abs1():
    # 1_test
    try:
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

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:

        browser.quit()

def test_abs2():
    # 2_test
    try:
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

        assert "Congratulations! You have successfully registered!" == welcome_text

    finally:

        browser.quit()

if __name__ == "__main__":
    pytest.main()

# pytest {test}.py

# Количество пакетов в нашем проекте растет, а мы тем временем все дальше уходим от учебных кусочков скриптов в сторону настоящего тестового проекта, поэтому в этом шаге давайте зафиксируем все пакеты, которые мы используем. Это стандартная практика, которая позволяет быстро переключаться в свежее виртуальное окружение, а также работать нескольким людям над одним проектом, получая одинаковые результаты.
#
# Откройте терминал, перейдите в директорию, в которой вы работаете с автотестами, и активируйте виртуальное окружение.
#
# После чего выполните в терминале команду:
#
# pip freeze > requirements.txt
# Эта команда сохранит все версии пакетов в специальный файл requirements.txt.
#
# Как их оттуда достать? Попробуйте создать новое виртуальное окружение (если нужно, вернитесь в модуль 1 за инструкциями) и активировать. После чего выполните команду:
#
# pip install -r requirements.txt
# В свежем окружении все пакеты установлены одной командой!

# -v --tb=line - улучшит отображение. Также pytest можно не импортировать -s выведет принт