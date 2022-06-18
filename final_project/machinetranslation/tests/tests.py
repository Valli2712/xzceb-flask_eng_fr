import unittest

from translator import englishToFrench, frenchToEnglish

class TestenglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') # test when 2 is given as input the output is 4.
        self.assertNotEqual(englishToFrench('None'), '')  # test when -3 is given as input the output is not -9.

class TestfrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') # test when 2 is given as input the output is 4.
        self.assertNotEqual(frenchToEnglish('None'), '') # test when 0 is given as input the output is 0.

unittest.main()