
import unittest

class Tests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

    def test_false(self):
        self.assertFalse(False)

    def test_42(self):
        self.assertEqual(42, 42)