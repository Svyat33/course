import unittest
from unittest import mock
import os, io

class  CheckHW3(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.join(os.path.dirname(os.path.realpath(__file__)), "hw3.py"), "Файл hw3.py не создан")
    
    def test_function_exists(self):
        from hw3 import make_operation
        self.assertTrue('make_operation' in dir(), "Функция не определена")
    
    def test_function_add(self):
        from hw3 import make_operation
        self.assertEqual(make_operation("+", 1,2,3), 6, "Сложение выполнено неверно")
        self.assertEqual(make_operation("+", 7, -7, 1, 0), 1, "Сложение выполнено неверно")

    def test_function_rem(self):
        from hw3 import make_operation
        self.assertEqual(make_operation("-", 100, 20, 30), 50, "Вычитание выполнено неверно")
        self.assertEqual(make_operation("-", 10, 20, 30), -40, "Вычитание выполнено неверно")

    def test_function_mul(self):
        from hw3 import make_operation
        self.assertEqual(make_operation("*", 1, 1, 1), 1, "Умножение выполнено неверно")
        self.assertEqual(make_operation("*", 7, 6), 42)
if __name__ == '__main__':
    unittest.main()
