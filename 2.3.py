# 4_step
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/alert_accept.html"
#
# try:
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     button_1 = browser.find_element(By.CSS_SELECTOR, ".container button.btn")
#     button_1.click()
#
#     confirm = browser.switch_to.alert
#     confirm.accept()
#
#     time.sleep(0.5)
#
#     x = browser.find_element(By.ID, "input_value")
#     value_x = x.text
#     solution = calc(value_x)
#
#     ans = browser.find_element(By.ID, "answer")
#     ans.send_keys(solution)
#
#     button_2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button_2.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

# 6_step
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button_1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_1.click()

    time.sleep(0.5)

    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value")
    value_x = x.text
    solution = calc(value_x)

    ans = browser.find_element(By.ID, "answer")
    ans.send_keys(solution)

    button_2 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button_2.click()

finally:
    time.sleep(15)
    browser.quit()
