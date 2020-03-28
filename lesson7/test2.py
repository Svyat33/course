import unittest
from unittest import mock
import os, io

class  CheckHW2(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.join(os.path.dirname(os.path.realpath(__file__)), "hw2.py"), "Файл hw2.py не создан")
    
    def test_function_exists(self):
        from hw2 import make_country
        self.assertTrue('make_country' in dir(), "Функция не определена")
    
    def test_function_work(self):
        from hw2 import make_country
        rez = make_country("Ukraine", "Kyiv")
        self.assertDictEqual(rez, {"name":"Ukraine", "capital":"Kyiv"}, "Функция вернула неправильный словарь")

    def test_print_function(self):
        from hw2 import print_country, make_country
        rez = make_country("Ukraine", "Kyiv")
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            print_country(rez)
        self.assertEqual(fake_stdout.getvalue().strip(), "Страна: Ukraine столица: Kyiv")


if __name__ == '__main__':
    unittest.main()
