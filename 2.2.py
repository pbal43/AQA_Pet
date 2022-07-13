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

# from selenium import webdriver
# browser = webdriver.Chrome()
# browser.execute_script("document.title='Script executing';alert('Robots at work');")

# 6_step
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import math
#
# def calc(x):
#   return str(math.log(abs(12*math.sin(int(x)))))
#
# try:
#     link = "http://suninjuly.github.io/execute_script.html"
#     browser = webdriver.Chrome()
#     browser.get(link)
#
#     x_element = browser.find_element(By.ID, "input_value")
#     x = x_element.text
#     solution = calc(x)
#
#     answer = browser.find_element(By.ID, "answer")
#     browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
#     answer.send_keys(solution)
#     robot_check = browser.find_element(By.ID, "robotCheckbox")
#     robot_check.click()
#     robot_ruler = browser.find_element(By.ID, "robotsRule")
#     robot_ruler.click()
#     button = browser.find_element(By.CSS_SELECTOR, "button.btn")
#     button.click()
#
# finally:
#     time.sleep(15)
#     browser.quit()

# Для загрузки файла на веб - страницу, используем метод send_keys("путь к файлу")
# Три способа задать путь к файлу:
# 1. вбить руками
# element.send_keys("/home/user/stepik/Chapter2/file_example.txt")
# 2. задать с помощью переменных, указывая директорию,где лежит файлу.txt, в конце должен быть /
# directory = "/home/user/stepik/Chapter2/"
# имя файла, который будем загружать на сайт
# file_name = "file_example.txt"
# собираем путь к файлу
# file_path = os.path.join(directory, file_name)
# # отправляем файл
# element.send_keys(file_path)
# 3. путь автоматизатора. (Через Виртуальное окружение и консоль) если файлы lesson2_7.py и file_example.txt" лежат в одном каталоге, импортируем модуль
# import os
# получаем путь к директории текущего исполняемого скрипта lesson2_7.py
# current_dir = os.path.abspath(os.path.dirname(__file__))
# имя файла, который будем загружать на сайт
# file_name = "file_example.txt"
# получаем путь к file_example.txt
# file_path = os.path.join(current_dir, file_name)
# отправляем файл
# element.send_keys(file_path)

# 8_step (через Виртуальное окружение и консоль для отработки поиска пути
# к текущей директории со скриптом и файлом через OS)
# source environments/selenium_env/bin/activate - в консоли
# python 2.2.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "file_example.txt"
create_file = "touch" + " " + file_name
x = os.system(create_file)
file_path = os.path.join(current_dir, file_name)

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    first_name = browser.find_element(By.NAME, 'firstname')
    first_name.send_keys('Pavlik')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Sniffer')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('Pavlik_sniffer@snifsnif.com')
    file_sender = browser.find_element(By.ID, 'file')
    file_sender.send_keys(file_path)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

finally:
    time.sleep(15)
    browser.quit()