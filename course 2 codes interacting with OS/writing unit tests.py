#example of writing unit tests in Python

from file import file function
import unittest

class Testfilename(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(file function(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(file function(testcase), expected)

        #we have a bug with Typeerror None
        #we have to put condition like if ... is None: return ""

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(file function(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(file function(testcase), expected)

        #we have an Assertation error
        #again, put condition if .... is None: return name
    
    
unittest.main
