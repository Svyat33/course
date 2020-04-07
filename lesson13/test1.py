import unittest
from unittest import mock
import os, io

class  CheckHW1(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.join(os.path.dirname(os.path.realpath(__file__)), "hw1.py"), "Файл hw1.py не создан")
    
    def test_function_exists(self):
        from hw1 import myprint
        self.assertTrue('myprint' in dir(), "Функция не определена")
    
    def test_print_function(self):
        from hw1 import myprint
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            myprint("", "22", "32")
        d = fake_stdout.getvalue().strip().split("\n")
        self.assertEqual(d[0], '3')
        self.assertEqual(d[1], ' 22 32')
        
    def test_print_function2(self):
        '''
        тест принта с разделителем
        '''
        from hw1 import myprint
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            myprint((1,2,3), {"22", "33"}, "4", sep="||")
        d = fake_stdout.getvalue().strip().split("\n")
        self.assertEqual(d[0], '4')
        self.assertEqual(d[1], "(1, 2, 3)||{'22', '33'}||4")

if __name__ == '__main__':
    unittest.main()
