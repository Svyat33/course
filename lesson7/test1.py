import unittest
import os

class  CheckHW1(unittest.TestCase):

    def test_file_exists(self):
        self.assertTrue(os.path.join(os.path.dirname(os.path.realpath(__file__)), "hw1.py"), "Файл hw1.py не создан")
    
    def test_function_exists(self):
        from hw1 import favorite_movie
        self.assertTrue('favorite_movie' in dir(), "Функция не определена")
    
    def test_function_work(self):
        from hw1 import favorite_movie
        self.assertEqual(favorite_movie("Terminator 1"), 
        "My favorite movie is named Terminator 1", 
        "Функция возвращает не такой ответ как должна.")

if __name__ == '__main__':
    unittest.main()
