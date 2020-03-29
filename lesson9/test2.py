import unittest, os, io
from unittest import mock

class  CheckHW2(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.join(os.path.dirname(os.path.realpath(__file__)), "hw2.py"), "Файл hw1.py не создан")
    
    def test_function_exists(self):
        from hw2 import mymath
        self.assertTrue('mymath' in dir(), "Функция не определена")
    def test_function_ok(self):
        from hw2 import mymath
        self.assertEqual(mymath(2,2), 2)

    def test_function_valueerror(self):
        from hw2 import mymath
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            mymath("123", "qaz")
        self.assertEqual(fake_stdout.getvalue().strip(), "Произошла ошибка при приведении типа")
        
    def test_function_valueerror(self):
        from hw2 import mymath
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            mymath("4", "0")
        self.assertEqual(fake_stdout.getvalue().strip(), "Деление на ноль дает бесконечность, а ее нам не в чем хранить")

if __name__ == '__main__':
    unittest.main()
