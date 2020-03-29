import unittest
import os

class  CheckHW1(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.join(os.path.dirname(os.path.realpath(__file__)), "hw1.py"), "Файл hw1.py не создан")
    
    def test_function_exists(self):
        from hw1 import oops
        self.assertTrue('oops' in dir(), "Функция не определена")
    
    def test_function_work(self):
        from hw1 import oops
        with self.assertRaises(Exception): 
            oops()
        
if __name__ == '__main__':
    unittest.main()
