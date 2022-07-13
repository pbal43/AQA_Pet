# 3_step
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
# import time
#
# try:
#     link = "http://suninjuly.github.io/selects1.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#     number_1 = int((browser.find_element(By.ID, "num1")).text)
#     number_2 = int((browser.find_element(By.ID, "num2")).text)
#     summary = str(number_1 + number_2)
#     select = Select(browser.find_element(By.ID, "dropdown"))
#     select.select_by_value(summary)
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

# 6_step
