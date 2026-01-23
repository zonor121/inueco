import unittest

class TestList(unittest.TestCase):

    def setUp(self):
        self.data = [1, 2, 3]

    def test_length(self):
        self.assertEqual(len(self.data), 3)

    def test_append(self):
        self.data.append(4)
        self.assertEqual(self.data, [1, 2, 3, 4])

def setUp(self):
    self.data = [1, 2, 3]

def test_sum(self):
    result = sum(self.data)
    self.assertEqual(result, 6)
