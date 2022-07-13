# 5_step

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#
#     link = "http://suninjuly.github.io/math.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#     x = x_element.text
#     solution = calc(x)
#
#     input_text = browser.find_element(By.CSS_SELECTOR, "#answer")
#     input_text.send_keys(solution)
#     input_checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
#     input_checkbox.click()
#     input_radio = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
#     input_radio.click()
#     submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     submit_button.click()
#
# finally:
#
#     time.sleep(15)
#     browser.quit()

# 7_step

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    solution = calc(x)

    input_text = browser.find_element(By.ID, "answer")
    input_text.send_keys(solution)
    input_checkbox = browser.find_element(By.ID, "robotCheckbox")
    input_checkbox.click()
    input_radio = browser.find_element(By.ID, "robotsRule")
    input_radio.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_button.click()

finally:

    time.sleep(15)
    browser.quit()