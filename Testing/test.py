import unittest
from Testing import main


class TestMain(unittest.TestCase):
    # def test_do_stuff(self):
    #     test_param = 10
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 15)  # Ran 1 test in 0.002s, OK
    #
    # def test_do_stuff2(self):
    #     test_param = 10
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, 10)  # AssertionError: 15 != 10

    # def test_do_stuff3(self):
    #     test_param = 'asdf'
    #     result = main.do_stuff(test_param)
    #     self.assertEqual(result, ValueError)  # AssertionError: ValueError("invalid literal for int() with base 10: 'asdf'") != <class 'ValueError'>

    def test_do_stuff4(self):
        test_param = 'asdf'
        result = main.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))  # Ran 1 test in 0.001s, OK