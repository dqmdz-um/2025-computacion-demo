import unittest

def suma(a, b):
    return a + b

class DemoTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(suma(1, 2), 3)

if __name__ == '__main__':
    unittest.main()