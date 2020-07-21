import unittest
from Testing import main


class TestMain(unittest.TestCase):
    def setUp(self):
        print('about to test a function')

    def test_do_stuff(self):
        """You can add docstrings within test functions"""
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)  # Ran test in 0.002s, OK

    def test_do_stuff2(self):
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 10)  # AssertionError: 15 != 10

    def test_do_stuff3(self):
        test_param = 'asdf'
        result = main.do_stuff(test_param)
        self.assertEqual(result, ValueError)  # AssertionError: ValueError("invalid literal for int() with base 10: 'asdf'") != <class 'ValueError'>

    def test_do_stuff4(self):
        test_param = 'asdf'
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)  # Ran test in 0.001s, OK

    def test_do_stuff5(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, ValueError)  # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'

    def test_do_stuff6(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')  # Ran test in 0.001s, OK

    def test_do_stuff7(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')  # Ran test in 0.001s, OK

    def test_do_stuff8(self):
        test_param = 0
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')  # Ran test in 0.001s, OK

    def tearDown(self):
        print('cleaning up')


if __name__ == '__main__':
    unittest.main()
