# 8_step
# asserts
# def test_input_text(expected_result, actual_result):
#     assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"
#
# # 9_step
# def test_substring(full_string, substring):
#     assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

# 10_step
# Созданные тесты нужно сохранить в файле, чтобы его было удобно запускать и хранить в системе контроля версий.
# Давайте создадим файл test_abs_project.py и напишем в нём следующий код:
#
# def test_abs1():
#     assert abs(-42) == 42, "Should be absolute value of a number"
#
# if __name__ == "__main__":
#     test_abs1()
#     print("All tests passed!")
# Мы поместили тестовый сценарий в функцию для разделения тест-кейсов и возможности их независимого запуска.
#
# Не вдаваясь в подробности, скажем только, что конструкция if __name__ == "__main__" служит для подтверждения того,
# что данный скрипт был запущен напрямую, а не вызван внутри другого файла в качестве модуля.
# Весь код написанный в теле этого условия будет выполнен только если пользователь запустил файл самостоятельно.

# Using unittest
# Импортировать unittest в файл: import unittest
# Создать класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
# Превратить тестовые функции в методы, добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
# Изменить assert на self.assertEqual()
# Заменить строку запуска программы на unittest.main()
#
# import unittest
#
#
# class TestAbs(unittest.TestCase):
#     def test_abs1(self):
#         self.assertEqual(abs(-42), 42, "Should be absolute value of a number")
#
#     def test_abs2(self):
#         self.assertEqual(abs(-42), -42, "Should be absolute value of a number")
#
#
# if __name__ == "__main__":
#     unittest.main()

# 13_step in the other file